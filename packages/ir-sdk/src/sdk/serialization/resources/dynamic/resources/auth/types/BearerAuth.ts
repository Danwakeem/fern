/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../index";
import * as FernIr from "../../../../../../api/index";
import * as core from "../../../../../../core";
import { Name } from "../../../../commons/types/Name";

export const BearerAuth: core.serialization.ObjectSchema<
    serializers.dynamic.BearerAuth.Raw,
    FernIr.dynamic.BearerAuth
> = core.serialization.objectWithoutOptionalProperties({
    token: Name,
});

export declare namespace BearerAuth {
    export interface Raw {
        token: Name.Raw;
    }
}
