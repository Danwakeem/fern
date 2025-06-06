/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index.js";
import * as SeedTrace from "../../../../api/index.js";
import * as core from "../../../../core/index.js";
import { SubmissionId } from "./SubmissionId.js";
import { Language } from "../../commons/types/Language.js";
import { SubmissionFileInfo } from "./SubmissionFileInfo.js";
import { ProblemId } from "../../commons/types/ProblemId.js";

export const SubmitRequestV2: core.serialization.ObjectSchema<
    serializers.SubmitRequestV2.Raw,
    SeedTrace.SubmitRequestV2
> = core.serialization.object({
    submissionId: SubmissionId,
    language: Language,
    submissionFiles: core.serialization.list(SubmissionFileInfo),
    problemId: ProblemId,
    problemVersion: core.serialization.number().optional(),
    userId: core.serialization.string().optional(),
});

export declare namespace SubmitRequestV2 {
    export interface Raw {
        submissionId: SubmissionId.Raw;
        language: Language.Raw;
        submissionFiles: SubmissionFileInfo.Raw[];
        problemId: ProblemId.Raw;
        problemVersion?: number | null;
        userId?: string | null;
    }
}
