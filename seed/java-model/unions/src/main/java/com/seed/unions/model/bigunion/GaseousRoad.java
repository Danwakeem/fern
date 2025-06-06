/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.unions.model.bigunion;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.unions.core.ObjectMappers;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_ABSENT)
@JsonDeserialize(builder = GaseousRoad.Builder.class)
public final class GaseousRoad {
    private final String value;

    private GaseousRoad(String value) {
        this.value = value;
    }

    @JsonProperty("value")
    public String getValue() {
        return value;
    }

    @java.lang.Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof GaseousRoad && equalTo((GaseousRoad) other);
    }

    private boolean equalTo(GaseousRoad other) {
        return value.equals(other.value);
    }

    @java.lang.Override
    public int hashCode() {
        return Objects.hash(this.value);
    }

    @java.lang.Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static ValueStage builder() {
        return new Builder();
    }

    public interface ValueStage {
        _FinalStage value(String value);

        Builder from(GaseousRoad other);
    }

    public interface _FinalStage {
        GaseousRoad build();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder implements ValueStage, _FinalStage {
        private String value;

        private Builder() {}

        @java.lang.Override
        public Builder from(GaseousRoad other) {
            value(other.getValue());
            return this;
        }

        @java.lang.Override
        @JsonSetter("value")
        public _FinalStage value(String value) {
            this.value = Objects.requireNonNull(value, "value must not be null");
            return this;
        }

        @java.lang.Override
        public GaseousRoad build() {
            return new GaseousRoad(value);
        }
    }
}
