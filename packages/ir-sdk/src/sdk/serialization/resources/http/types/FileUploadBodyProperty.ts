/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernIr from "../../../../api/index";
import * as core from "../../../../core";
import { FileUploadBodyPropertyEncoding } from "./FileUploadBodyPropertyEncoding";
import { InlinedRequestBodyProperty } from "./InlinedRequestBodyProperty";
import { WithContentType } from "../../commons/types/WithContentType";

export const FileUploadBodyProperty: core.serialization.ObjectSchema<
    serializers.FileUploadBodyProperty.Raw,
    FernIr.FileUploadBodyProperty
> = core.serialization
    .objectWithoutOptionalProperties({
        style: FileUploadBodyPropertyEncoding.optional(),
    })
    .extend(InlinedRequestBodyProperty)
    .extend(WithContentType);

export declare namespace FileUploadBodyProperty {
    export interface Raw extends InlinedRequestBodyProperty.Raw, WithContentType.Raw {
        style?: FileUploadBodyPropertyEncoding.Raw | null;
    }
}
