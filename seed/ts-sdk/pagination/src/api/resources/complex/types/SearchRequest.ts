/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedPagination from "../../../index.js";

export interface SearchRequest {
    pagination?: SeedPagination.StartingAfterPaging;
    query: SearchRequest.Query;
}

export namespace SearchRequest {
    export type Query = SeedPagination.SingleFilterSearchRequest | SeedPagination.MultipleFilterSearchRequest;
}
