/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernOpenapiIr from "../../../../api";
import * as core from "../../../../core";

export const GlobalHeader: core.serialization.ObjectSchema<serializers.GlobalHeader.Raw, FernOpenapiIr.GlobalHeader> =
    core.serialization.objectWithoutOptionalProperties({
        header: core.serialization.string(),
        name: core.serialization.string().optional(),
        optional: core.serialization.boolean().optional(),
    });

export declare namespace GlobalHeader {
    interface Raw {
        header: string;
        name?: string | null;
        optional?: boolean | null;
    }
}
