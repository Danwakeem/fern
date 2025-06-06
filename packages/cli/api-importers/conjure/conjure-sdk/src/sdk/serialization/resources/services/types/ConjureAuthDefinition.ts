/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as FernConjure from "../../../../api/index";
import * as core from "../../../../core";
import { ConjureAuthDefinitionType } from "./ConjureAuthDefinitionType";

export const ConjureAuthDefinition: core.serialization.Schema<
    serializers.ConjureAuthDefinition.Raw,
    FernConjure.ConjureAuthDefinition
> = core.serialization.undiscriminatedUnion([ConjureAuthDefinitionType, core.serialization.string()]);

export declare namespace ConjureAuthDefinition {
    export type Raw = ConjureAuthDefinitionType.Raw | string;
}
