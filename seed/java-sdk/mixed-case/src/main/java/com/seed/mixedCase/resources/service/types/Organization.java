/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.mixedCase.resources.service.types;

import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.mixedCase.core.ObjectMappers;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import org.jetbrains.annotations.NotNull;

@JsonInclude(JsonInclude.Include.NON_ABSENT)
@JsonDeserialize(builder = Organization.Builder.class)
public final class Organization {
    private final String name;

    private final Map<String, Object> additionalProperties;

    private Organization(String name, Map<String, Object> additionalProperties) {
        this.name = name;
        this.additionalProperties = additionalProperties;
    }

    @JsonProperty("name")
    public String getName() {
        return name;
    }

    @java.lang.Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof Organization && equalTo((Organization) other);
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    private boolean equalTo(Organization other) {
        return name.equals(other.name);
    }

    @java.lang.Override
    public int hashCode() {
        return Objects.hash(this.name);
    }

    @java.lang.Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }

    public static NameStage builder() {
        return new Builder();
    }

    public interface NameStage {
        _FinalStage name(@NotNull String name);

        Builder from(Organization other);
    }

    public interface _FinalStage {
        Organization build();
    }

    @JsonIgnoreProperties(ignoreUnknown = true)
    public static final class Builder implements NameStage, _FinalStage {
        private String name;

        @JsonAnySetter
        private Map<String, Object> additionalProperties = new HashMap<>();

        private Builder() {}

        @java.lang.Override
        public Builder from(Organization other) {
            name(other.getName());
            return this;
        }

        @java.lang.Override
        @JsonSetter("name")
        public _FinalStage name(@NotNull String name) {
            this.name = Objects.requireNonNull(name, "name must not be null");
            return this;
        }

        @java.lang.Override
        public Organization build() {
            return new Organization(name, additionalProperties);
        }
    }
}
