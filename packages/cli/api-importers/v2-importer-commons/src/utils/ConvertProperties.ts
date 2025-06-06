import { OpenAPIV3_1 } from "openapi-types";

import { ObjectProperty, TypeId } from "@fern-api/ir-sdk";

import { Extensions } from "..";
import { AbstractConverterContext } from "../AbstractConverterContext";
import { ErrorCollector } from "../ErrorCollector";
import { SchemaConverter } from "../converters/schema/SchemaConverter";
import { SchemaOrReferenceConverter } from "../converters/schema/SchemaOrReferenceConverter";

export function convertProperties({
    properties,
    required,
    breadcrumbs,
    context,
    errorCollector
}: {
    properties: Record<string, OpenAPIV3_1.SchemaObject | OpenAPIV3_1.ReferenceObject>;
    required: string[];
    breadcrumbs: string[];
    context: AbstractConverterContext<object>;
    errorCollector: ErrorCollector;
}): {
    convertedProperties: ObjectProperty[];
    propertiesByAudience: Record<string, Set<string>>;
    inlinedTypesFromProperties: Record<TypeId, SchemaConverter.ConvertedSchema>;
    referencedTypes: Set<string>;
} {
    const convertedProperties: ObjectProperty[] = [];
    let inlinedTypesFromProperties: Record<TypeId, SchemaConverter.ConvertedSchema> = {};
    const propertiesByAudience: Record<string, Set<string>> = {};
    const referencedTypes: Set<string> = new Set();
    for (const [propertyName, propertySchema] of Object.entries(properties ?? {})) {
        const propertyBreadcrumbs = [...breadcrumbs, "properties", propertyName];
        if (typeof propertySchema !== "object") {
            errorCollector.collect({
                message: `Schema property ${propertyName} should be an object`,
                path: propertyBreadcrumbs
            });
            continue;
        }
        const propertyId =
            maybeGetFernTypeNameExtension(breadcrumbs, propertySchema, context) ??
            context.convertBreadcrumbsToName(propertyBreadcrumbs);
        const isNullable = "nullable" in propertySchema ? (propertySchema.nullable as boolean) : false;

        const propertySchemaConverter = new SchemaOrReferenceConverter({
            context,
            breadcrumbs: propertyBreadcrumbs,
            schemaOrReference: propertySchema,
            schemaIdOverride: propertyId,
            wrapAsOptional: !required.includes(propertyName),
            wrapAsNullable: isNullable
        });
        const convertedProperty = propertySchemaConverter.convert();
        if (convertedProperty != null) {
            convertedProperties.push({
                name: context.casingsGenerator.generateNameAndWireValue({
                    name: propertyName,
                    wireValue: propertyName
                }),
                valueType: convertedProperty.type,
                docs: propertySchema.description,
                availability: convertedProperty.availability,
                propertyAccess: context.getPropertyAccess(propertySchema),
                v2Examples: convertedProperty.schema?.typeDeclaration?.v2Examples ?? {
                    userSpecifiedExamples: {},
                    autogeneratedExamples: {}
                }
            });
            inlinedTypesFromProperties = {
                ...inlinedTypesFromProperties,
                ...convertedProperty.inlinedTypes
            };

            if (convertedProperty.schema?.typeDeclaration.referencedTypes != null) {
                convertedProperty.schema.typeDeclaration.referencedTypes.forEach((type) => {
                    referencedTypes.add(type);
                });
            }
            for (const audience of convertedProperty.schema?.audiences ?? []) {
                if (propertiesByAudience[audience] == null) {
                    propertiesByAudience[audience] = new Set<string>();
                }
                propertiesByAudience[audience].add(propertyName);
            }
        }
    }
    for (const typeId of Object.keys(inlinedTypesFromProperties)) {
        referencedTypes.add(typeId);
    }
    return { convertedProperties, propertiesByAudience, inlinedTypesFromProperties, referencedTypes };
}

function maybeGetFernTypeNameExtension(
    breadcrumbs: string[],
    schema: OpenAPIV3_1.SchemaObject,
    context: AbstractConverterContext<object>
): string | undefined {
    if (context.isReferenceObject(schema)) {
        return undefined;
    }
    const fernTypeNameConverter = new Extensions.FernTypeNameExtension({
        breadcrumbs,
        schema,
        context
    });
    return fernTypeNameConverter.convert();
}
