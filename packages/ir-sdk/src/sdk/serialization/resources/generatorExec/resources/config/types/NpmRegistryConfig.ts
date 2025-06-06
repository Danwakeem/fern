/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../index";
import * as FernIr from "../../../../../../api/index";
import * as core from "../../../../../../core";

export const NpmRegistryConfig: core.serialization.ObjectSchema<
    serializers.generatorExec.NpmRegistryConfig.Raw,
    FernIr.generatorExec.NpmRegistryConfig
> = core.serialization.objectWithoutOptionalProperties({
    registryUrl: core.serialization.string(),
    token: core.serialization.string(),
    scope: core.serialization.string(),
});

export declare namespace NpmRegistryConfig {
    export interface Raw {
        registryUrl: string;
        token: string;
        scope: string;
    }
}
