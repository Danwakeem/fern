# frozen_string_literal: true

require_relative "lib/gemconfig"

Gem::Specification.new do |spec|
  spec.name = "seed_http_head_client"
  spec.version = SeedHttpHeadClient::Gemconfig::VERSION
  spec.authors = SeedHttpHeadClient::Gemconfig::AUTHORS
  spec.email = SeedHttpHeadClient::Gemconfig::EMAIL
  spec.summary = SeedHttpHeadClient::Gemconfig::SUMMARY
  spec.description = SeedHttpHeadClient::Gemconfig::DESCRIPTION
  spec.homepage = SeedHttpHeadClient::Gemconfig::HOMEPAGE
  spec.required_ruby_version = ">= 2.7.0"
  spec.metadata["homepage_uri"] = spec.homepage
  spec.metadata["source_code_uri"] = SeedHttpHeadClient::Gemconfig::SOURCE_CODE_URI
  spec.metadata["changelog_uri"] = SeedHttpHeadClient::Gemconfig::CHANGELOG_URI
  spec.files = Dir.glob("lib/**/*")
  spec.bindir = "exe"
  spec.executables = spec.files.grep(%r{\Aexe/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]
end
