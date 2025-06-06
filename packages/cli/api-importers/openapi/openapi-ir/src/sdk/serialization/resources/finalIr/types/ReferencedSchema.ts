/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernOpenapiIr from "../../../../api/index";
import * as core from "../../../../core";
import { SchemaId } from "../../commons/types/SchemaId";
import { WithSdkGroupName } from "../../commons/types/WithSdkGroupName";
import { WithNamespace } from "../../commons/types/WithNamespace";
import { WithName } from "../../commons/types/WithName";
import { WithDescription } from "../../commons/types/WithDescription";
import { WithAvailability } from "../../commons/types/WithAvailability";
import { WithSource } from "../../commons/types/WithSource";
import { WithTitle } from "../../commons/types/WithTitle";

export const ReferencedSchema: core.serialization.ObjectSchema<
    serializers.ReferencedSchema.Raw,
    FernOpenapiIr.ReferencedSchema
> = core.serialization
    .objectWithoutOptionalProperties({
        schema: SchemaId,
    })
    .extend(WithSdkGroupName)
    .extend(WithNamespace)
    .extend(WithName)
    .extend(WithDescription)
    .extend(WithAvailability)
    .extend(WithSource)
    .extend(WithTitle);

export declare namespace ReferencedSchema {
    export interface Raw
        extends WithSdkGroupName.Raw,
            WithNamespace.Raw,
            WithName.Raw,
            WithDescription.Raw,
            WithAvailability.Raw,
            WithSource.Raw,
            WithTitle.Raw {
        schema: SchemaId.Raw;
    }
}
