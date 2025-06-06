/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../../index";

export type ExampleRequestBody = FernIr.ExampleRequestBody.InlinedRequestBody | FernIr.ExampleRequestBody.Reference;

export namespace ExampleRequestBody {
    export interface InlinedRequestBody extends FernIr.ExampleInlinedRequestBody, _Utils {
        type: "inlinedRequestBody";
    }

    export interface Reference extends FernIr.ExampleTypeReference, _Utils {
        type: "reference";
    }

    export interface _Utils {
        _visit: <_Result>(visitor: FernIr.ExampleRequestBody._Visitor<_Result>) => _Result;
    }

    export interface _Visitor<_Result> {
        inlinedRequestBody: (value: FernIr.ExampleInlinedRequestBody) => _Result;
        reference: (value: FernIr.ExampleTypeReference) => _Result;
        _other: (value: { type: string }) => _Result;
    }
}

export const ExampleRequestBody = {
    inlinedRequestBody: (value: FernIr.ExampleInlinedRequestBody): FernIr.ExampleRequestBody.InlinedRequestBody => {
        return {
            ...value,
            type: "inlinedRequestBody",
            _visit: function <_Result>(
                this: FernIr.ExampleRequestBody.InlinedRequestBody,
                visitor: FernIr.ExampleRequestBody._Visitor<_Result>,
            ) {
                return FernIr.ExampleRequestBody._visit(this, visitor);
            },
        };
    },

    reference: (value: FernIr.ExampleTypeReference): FernIr.ExampleRequestBody.Reference => {
        return {
            ...value,
            type: "reference",
            _visit: function <_Result>(
                this: FernIr.ExampleRequestBody.Reference,
                visitor: FernIr.ExampleRequestBody._Visitor<_Result>,
            ) {
                return FernIr.ExampleRequestBody._visit(this, visitor);
            },
        };
    },

    _visit: <_Result>(
        value: FernIr.ExampleRequestBody,
        visitor: FernIr.ExampleRequestBody._Visitor<_Result>,
    ): _Result => {
        switch (value.type) {
            case "inlinedRequestBody":
                return visitor.inlinedRequestBody(value);
            case "reference":
                return visitor.reference(value);
            default:
                return visitor._other(value as any);
        }
    },
} as const;
