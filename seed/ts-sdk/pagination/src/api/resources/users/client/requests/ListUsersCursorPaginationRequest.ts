/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedPagination from "../../../../index.js";

/**
 * @example
 *     {
 *         page: 1,
 *         per_page: 1,
 *         order: "asc",
 *         starting_after: "starting_after"
 *     }
 */
export interface ListUsersCursorPaginationRequest {
    /**
     * Defaults to first page
     */
    page?: number;
    /**
     * Defaults to per page
     */
    per_page?: number;
    order?: SeedPagination.Order;
    /**
     * The cursor used for pagination in order to fetch
     * the next page of results.
     */
    starting_after?: string;
}
