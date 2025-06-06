/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../../../../index";

export type InlinedRequestBody =
    | FernIr.dynamic.InlinedRequestBody.Properties
    | FernIr.dynamic.InlinedRequestBody.Referenced
    | FernIr.dynamic.InlinedRequestBody.FileUpload;

export namespace InlinedRequestBody {
    export interface Properties extends _Utils {
        type: "properties";
        value: FernIr.dynamic.NamedParameter[];
    }

    export interface Referenced extends FernIr.dynamic.ReferencedRequestBody, _Utils {
        type: "referenced";
    }

    export interface FileUpload extends FernIr.dynamic.FileUploadRequestBody, _Utils {
        type: "fileUpload";
    }

    export interface _Utils {
        _visit: <_Result>(visitor: FernIr.dynamic.InlinedRequestBody._Visitor<_Result>) => _Result;
    }

    export interface _Visitor<_Result> {
        properties: (value: FernIr.dynamic.NamedParameter[]) => _Result;
        referenced: (value: FernIr.dynamic.ReferencedRequestBody) => _Result;
        fileUpload: (value: FernIr.dynamic.FileUploadRequestBody) => _Result;
        _other: (value: { type: string }) => _Result;
    }
}

export const InlinedRequestBody = {
    properties: (value: FernIr.dynamic.NamedParameter[]): FernIr.dynamic.InlinedRequestBody.Properties => {
        return {
            value: value,
            type: "properties",
            _visit: function <_Result>(
                this: FernIr.dynamic.InlinedRequestBody.Properties,
                visitor: FernIr.dynamic.InlinedRequestBody._Visitor<_Result>,
            ) {
                return FernIr.dynamic.InlinedRequestBody._visit(this, visitor);
            },
        };
    },

    referenced: (value: FernIr.dynamic.ReferencedRequestBody): FernIr.dynamic.InlinedRequestBody.Referenced => {
        return {
            ...value,
            type: "referenced",
            _visit: function <_Result>(
                this: FernIr.dynamic.InlinedRequestBody.Referenced,
                visitor: FernIr.dynamic.InlinedRequestBody._Visitor<_Result>,
            ) {
                return FernIr.dynamic.InlinedRequestBody._visit(this, visitor);
            },
        };
    },

    fileUpload: (value: FernIr.dynamic.FileUploadRequestBody): FernIr.dynamic.InlinedRequestBody.FileUpload => {
        return {
            ...value,
            type: "fileUpload",
            _visit: function <_Result>(
                this: FernIr.dynamic.InlinedRequestBody.FileUpload,
                visitor: FernIr.dynamic.InlinedRequestBody._Visitor<_Result>,
            ) {
                return FernIr.dynamic.InlinedRequestBody._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(
        value: FernIr.dynamic.InlinedRequestBody,
        visitor: FernIr.dynamic.InlinedRequestBody._Visitor<_Result>,
    ): _Result => {
        switch (value.type) {
            case "properties":
                return visitor.properties(value.value);
            case "referenced":
                return visitor.referenced(value);
            case "fileUpload":
                return visitor.fileUpload(value);
            default:
                return visitor._other(value as any);
        }
    },
} as const;
