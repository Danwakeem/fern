/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../../../index.js";
import * as SeedTrace from "../../../../../../../../api/index.js";
import * as core from "../../../../../../../../core/index.js";
import { NonVoidFunctionDefinition } from "./NonVoidFunctionDefinition.js";
import { AssertCorrectnessCheck } from "./AssertCorrectnessCheck.js";

export const TestCaseWithActualResultImplementation: core.serialization.ObjectSchema<
    serializers.v2.v3.TestCaseWithActualResultImplementation.Raw,
    SeedTrace.v2.v3.TestCaseWithActualResultImplementation
> = core.serialization.object({
    getActualResult: NonVoidFunctionDefinition,
    assertCorrectnessCheck: AssertCorrectnessCheck,
});

export declare namespace TestCaseWithActualResultImplementation {
    export interface Raw {
        getActualResult: NonVoidFunctionDefinition.Raw;
        assertCorrectnessCheck: AssertCorrectnessCheck.Raw;
    }
}
