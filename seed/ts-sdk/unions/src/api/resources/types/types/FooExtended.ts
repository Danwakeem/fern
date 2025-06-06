/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as SeedUnions from "../../../index.js";

/**
 * @example
 *     {
 *         name: "example1",
 *         age: 5
 *     }
 *
 * @example
 *     {
 *         name: "example2",
 *         age: 10
 *     }
 */
export interface FooExtended extends SeedUnions.Foo {
    age: number;
}
