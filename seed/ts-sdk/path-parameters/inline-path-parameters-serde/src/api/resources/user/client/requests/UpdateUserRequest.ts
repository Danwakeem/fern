/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedPathParameters from "../../../../index.js";

/**
 * @example
 *     {
 *         userId: "user_id",
 *         body: {
 *             name: "name",
 *             tags: ["tags", "tags"]
 *         }
 *     }
 */
export interface UpdateUserRequest {
    userId: string;
    body: SeedPathParameters.User;
}
