/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernDocsConfig from "../../../index";

export interface ProductConfig extends FernDocsConfig.WithPermissions, FernDocsConfig.WithFeatureFlags {
    displayName: string;
    /** The relative path to the version's docs.yml file. */
    path: string;
    subtitle?: string;
    icon?: string;
    /** The image to display in the product card. This will override the icon field if both are set. */
    image?: string;
    /** The "slug" is this version's basePath. If not set, the slug will be generated from the display-name. */
    slug?: string;
    versions?: FernDocsConfig.VersionConfig[];
}
