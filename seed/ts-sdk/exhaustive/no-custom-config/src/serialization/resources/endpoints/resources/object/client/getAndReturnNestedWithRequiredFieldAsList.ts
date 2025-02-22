/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../..";
import * as SeedExhaustive from "../../../../../../api";
import * as core from "../../../../../../core";

export const Request: core.serialization.Schema<
    serializers.endpoints.object.getAndReturnNestedWithRequiredFieldAsList.Request.Raw,
    SeedExhaustive.types.NestedObjectWithRequiredField[]
> = core.serialization.list(
    core.serialization.lazyObject(async () => (await import("../../../../..")).types.NestedObjectWithRequiredField)
);

export declare namespace Request {
    type Raw = serializers.types.NestedObjectWithRequiredField.Raw[];
}
