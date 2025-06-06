/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedTrace from "../../../index.js";
import * as core from "../../../../core/index.js";

export type Error = SeedTrace.submission.createExecutionSession.Error._Unknown;

export namespace Error {
    export interface _Unknown {
        errorName: void;
        content: core.Fetcher.Error;
    }

    export interface _Visitor<_Result> {
        _other: (value: core.Fetcher.Error) => _Result;
    }
}

export const Error = {
    _unknown: (fetcherError: core.Fetcher.Error): SeedTrace.submission.createExecutionSession.Error._Unknown => {
        return {
            errorName: undefined,
            content: fetcherError,
        };
    },

    _visit: <_Result>(
        value: SeedTrace.submission.createExecutionSession.Error,
        visitor: SeedTrace.submission.createExecutionSession.Error._Visitor<_Result>,
    ): _Result => {
        switch (value.errorName) {
            default:
                return visitor._other(value as any);
        }
    },
} as const;
