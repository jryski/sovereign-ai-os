# Security Policy

This parent repository is a public routing and orientation surface. It is
not a runtime, credential store, or deployment control plane.

## Do not post sensitive material in public issues or pull requests

Do **not** post any of the following in public issues, pull requests,
comments, or review threads:

- private deployment payloads;
- credentials, tokens, keys, or connection strings;
- private topology, locators, or unpublished repository names;
- real household, business, or customer records;
- restricted evidence, dumps, or recovery artifacts.

Use synthetic examples and redacted language. If a report cannot be made
useful without sensitive evidence, use a private channel instead.

## Report a vulnerability privately

Prefer [GitHub Private Vulnerability Reporting](https://github.com/jryski/sovereign-ai-os/security/advisories/new)
when it is available.

If private reporting is unavailable, contact the maintainer through the
[GitHub profile](https://github.com/jryski) without posting sensitive
details publicly.

Include, where possible:

- affected file or commit;
- why the issue matters on this public surface or in a linked public
  component;
- a synthetic reproduction;
- demonstrated or likely impact;
- a proposed mitigation, if known.

## Scope notes

- Child repositories have their own security files and reporting paths.
  Report implementation issues to the owning public repository.
- Do not treat Markdown, including this file, as a permission boundary
  or as runtime enforcement.
- Historic disclosure of private names in other repositories is not
  treated as contained, retracted, or closed by changes here.
