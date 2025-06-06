/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index.js";
import * as SeedTrace from "../../../../api/index.js";
import * as core from "../../../../core/index.js";
import { ProblemId } from "../../commons/types/ProblemId.js";
import { ProblemDescription } from "./ProblemDescription.js";
import { ProblemFiles } from "./ProblemFiles.js";
import { Language } from "../../commons/types/Language.js";
import { VariableTypeAndName } from "./VariableTypeAndName.js";
import { TestCaseWithExpectedResult } from "../../commons/types/TestCaseWithExpectedResult.js";

export const ProblemInfo: core.serialization.ObjectSchema<serializers.ProblemInfo.Raw, SeedTrace.ProblemInfo> =
    core.serialization.object({
        problemId: ProblemId,
        problemDescription: ProblemDescription,
        problemName: core.serialization.string(),
        problemVersion: core.serialization.number(),
        files: core.serialization.record(Language, ProblemFiles.optional()),
        inputParams: core.serialization.list(VariableTypeAndName),
        outputType: core.serialization.lazy(() => serializers.VariableType),
        testcases: core.serialization.list(TestCaseWithExpectedResult),
        methodName: core.serialization.string(),
        supportsCustomTestCases: core.serialization.boolean(),
    });

export declare namespace ProblemInfo {
    export interface Raw {
        problemId: ProblemId.Raw;
        problemDescription: ProblemDescription.Raw;
        problemName: string;
        problemVersion: number;
        files: Record<Language.Raw, ProblemFiles.Raw | null | undefined>;
        inputParams: VariableTypeAndName.Raw[];
        outputType: serializers.VariableType.Raw;
        testcases: TestCaseWithExpectedResult.Raw[];
        methodName: string;
        supportsCustomTestCases: boolean;
    }
}
