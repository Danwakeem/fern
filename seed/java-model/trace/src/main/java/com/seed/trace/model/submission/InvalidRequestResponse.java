/**
 * This file was auto-generated by Fern from our API Definition.
 */

package com.seed.trace.model.submission;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.seed.trace.core.ObjectMappers;
import java.lang.Object;
import java.lang.String;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_ABSENT)
@JsonDeserialize(
    builder = InvalidRequestResponse.Builder.class
)
public final class InvalidRequestResponse {
  private final SubmissionRequest request;

  private final InvalidRequestCause cause;

  private InvalidRequestResponse(SubmissionRequest request, InvalidRequestCause cause) {
    this.request = request;
    this.cause = cause;
  }

  @JsonProperty("request")
  public SubmissionRequest getRequest() {
    return request;
  }

  @JsonProperty("cause")
  public InvalidRequestCause getCause() {
    return cause;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof InvalidRequestResponse && equalTo((InvalidRequestResponse) other);
  }

  private boolean equalTo(InvalidRequestResponse other) {
    return request.equals(other.request) && cause.equals(other.cause);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.request, this.cause);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static RequestStage builder() {
    return new Builder();
  }

  public interface RequestStage {
    CauseStage request(SubmissionRequest request);

    Builder from(InvalidRequestResponse other);
  }

  public interface CauseStage {
    _FinalStage cause(InvalidRequestCause cause);
  }

  public interface _FinalStage {
    InvalidRequestResponse build();
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder implements RequestStage, CauseStage, _FinalStage {
    private SubmissionRequest request;

    private InvalidRequestCause cause;

    private Builder() {
    }

    @java.lang.Override
    public Builder from(InvalidRequestResponse other) {
      request(other.getRequest());
      cause(other.getCause());
      return this;
    }

    @java.lang.Override
    @JsonSetter("request")
    public CauseStage request(SubmissionRequest request) {
      this.request = Objects.requireNonNull(request, "request must not be null");
      return this;
    }

    @java.lang.Override
    @JsonSetter("cause")
    public _FinalStage cause(InvalidRequestCause cause) {
      this.cause = Objects.requireNonNull(cause, "cause must not be null");
      return this;
    }

    @java.lang.Override
    public InvalidRequestResponse build() {
      return new InvalidRequestResponse(request, cause);
    }
  }
}
