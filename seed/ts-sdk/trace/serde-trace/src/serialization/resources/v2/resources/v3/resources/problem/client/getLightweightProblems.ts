/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../../../index.js";
import * as SeedTrace from "../../../../../../../../api/index.js";
import * as core from "../../../../../../../../core/index.js";
import { LightweightProblemInfoV2 } from "../types/LightweightProblemInfoV2.js";

export const Response: core.serialization.Schema<
    serializers.v2.v3.problem.getLightweightProblems.Response.Raw,
    SeedTrace.v2.v3.LightweightProblemInfoV2[]
> = core.serialization.list(LightweightProblemInfoV2);

export declare namespace Response {
    export type Raw = LightweightProblemInfoV2.Raw[];
}
