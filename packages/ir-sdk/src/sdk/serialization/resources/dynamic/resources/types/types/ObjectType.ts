/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../index";
import * as FernIr from "../../../../../../api/index";
import * as core from "../../../../../../core";
import { Declaration } from "../../declaration/types/Declaration";
import { NamedParameter } from "./NamedParameter";

export const ObjectType: core.serialization.ObjectSchema<
    serializers.dynamic.ObjectType.Raw,
    FernIr.dynamic.ObjectType
> = core.serialization.objectWithoutOptionalProperties({
    declaration: Declaration,
    properties: core.serialization.list(NamedParameter),
    additionalProperties: core.serialization.boolean().optional(),
});

export declare namespace ObjectType {
    export interface Raw {
        declaration: Declaration.Raw;
        properties: NamedParameter.Raw[];
        additionalProperties?: boolean | null;
    }
}
