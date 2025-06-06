/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedPagination from "../../../index.js";

export interface MultipleFilterSearchRequest {
    operator?: MultipleFilterSearchRequest.Operator;
    value?: MultipleFilterSearchRequest.Value;
}

export namespace MultipleFilterSearchRequest {
    export type Operator = "AND" | "OR";
    export const Operator = {
        And: "AND",
        Or: "OR",
    } as const;
    export type Value = SeedPagination.MultipleFilterSearchRequest[] | SeedPagination.SingleFilterSearchRequest[];
}
