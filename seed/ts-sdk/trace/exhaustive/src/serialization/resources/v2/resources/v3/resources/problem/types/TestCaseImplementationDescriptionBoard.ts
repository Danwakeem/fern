/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../../../../..";
import * as SeedTrace from "../../../../../../../../api";
import * as core from "../../../../../../../../core";

export const TestCaseImplementationDescriptionBoard: core.serialization.Schema<
    serializers.v2.v3.TestCaseImplementationDescriptionBoard.Raw,
    SeedTrace.v2.v3.TestCaseImplementationDescriptionBoard
> = core.serialization
    .union("type", {
        html: core.serialization.object({
            value: core.serialization.string(),
        }),
        paramId: core.serialization.object({
            value: core.serialization.lazy(async () => (await import("../../../../../../..")).v2.v3.ParameterId),
        }),
    })
    .transform<SeedTrace.v2.v3.TestCaseImplementationDescriptionBoard>({
        transform: (value) => {
            switch (value.type) {
                case "html":
                    return SeedTrace.v2.v3.TestCaseImplementationDescriptionBoard.html(value.value);
                case "paramId":
                    return SeedTrace.v2.v3.TestCaseImplementationDescriptionBoard.paramId(value.value);
                default:
                    return SeedTrace.v2.v3.TestCaseImplementationDescriptionBoard._unknown(value);
            }
        },
        untransform: ({ _visit, ...value }) => value as any,
    });

export declare namespace TestCaseImplementationDescriptionBoard {
    type Raw = TestCaseImplementationDescriptionBoard.Html | TestCaseImplementationDescriptionBoard.ParamId;

    interface Html {
        type: "html";
        value: string;
    }

    interface ParamId {
        type: "paramId";
        value: serializers.v2.v3.ParameterId.Raw;
    }
}
