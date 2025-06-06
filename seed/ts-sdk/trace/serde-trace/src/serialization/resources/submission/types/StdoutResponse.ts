/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index.js";
import * as SeedTrace from "../../../../api/index.js";
import * as core from "../../../../core/index.js";
import { SubmissionId } from "./SubmissionId.js";

export const StdoutResponse: core.serialization.ObjectSchema<serializers.StdoutResponse.Raw, SeedTrace.StdoutResponse> =
    core.serialization.object({
        submissionId: SubmissionId,
        stdout: core.serialization.string(),
    });

export declare namespace StdoutResponse {
    export interface Raw {
        submissionId: SubmissionId.Raw;
        stdout: string;
    }
}
