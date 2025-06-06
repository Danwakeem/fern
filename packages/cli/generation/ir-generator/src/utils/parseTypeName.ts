import { DeclaredTypeName } from "@fern-api/ir-sdk";
import { IdGenerator } from "@fern-api/ir-utils";

import { FernFileContext } from "../FernFileContext";
import { convertToFernFilepath } from "./convertToFernFilepath";
import { parseReferenceToTypeName } from "./parseReferenceToTypeName";

export function parseTypeName({ typeName, file }: { typeName: string; file: FernFileContext }): DeclaredTypeName {
    const reference = parseReferenceToTypeName({
        reference: typeName,
        referencedIn: file.relativeFilepath,
        imports: file.imports
    });
    if (reference == null) {
        throw new Error("Failed to locate type: " + typeName);
    }

    const nameWithoutId = {
        name: file.casingsGenerator.generateName(reference.typeName),
        fernFilepath: convertToFernFilepath({
            relativeFilepath: reference.relativeFilepath,
            casingsGenerator: file.casingsGenerator
        }),
        displayName: undefined
    };

    return {
        ...nameWithoutId,
        typeId: IdGenerator.generateTypeId(nameWithoutId)
    };
}
