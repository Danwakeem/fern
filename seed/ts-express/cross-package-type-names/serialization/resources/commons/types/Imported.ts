/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedCrossPackageTypeNames from "../../../../api/index";
import * as core from "../../../../core";

export const Imported: core.serialization.Schema<serializers.Imported.Raw, SeedCrossPackageTypeNames.Imported> =
    core.serialization.string();

export declare namespace Imported {
    export type Raw = string;
}
