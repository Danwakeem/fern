/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernDefinition from "../../../../api/index";
import * as core from "../../../../core";

export const GithubSelfhostedSchema: core.serialization.ObjectSchema<
    serializers.GithubSelfhostedSchema.Raw,
    FernDefinition.GithubSelfhostedSchema
> = core.serialization.object({
    uri: core.serialization.string(),
    token: core.serialization.string(),
});

export declare namespace GithubSelfhostedSchema {
    export interface Raw {
        uri: string;
        token: string;
    }
}
