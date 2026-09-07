# Sovereign AI OS

User-controlled memory and bounded tools that work across AI assistants.

WIRE SPEED COMPUTING LLC maintains this program, led by Jesse Ryski.
The aim is to keep evidence, decisions, permissions and work history usable
when models, applications or providers change.

[Website and development notes](https://www.wirespeedcomputers.com/) |
[Component routes](ROUTES.md) | [Project principles](THESIS.md)

## What we are building

The components separate durable records from the tools that use them:

1. Keep source evidence, changes and decisions in a store the user controls.
2. Give each authorized person or agent a limited path to that data.
3. Build household and business workflows on those shared foundations.
4. Use existing models, standards and services where they fit.

A frontend outside any single model provider is a future direction, not a
delivered application. This is not an attempt to replace every assistant,
memory engine or integration.

## SMP is the foundation

Sovereign Memory Protocol (SMP) is the protocol work behind these projects.
Its purpose is to preserve user authority and the provenance of information
when models, applications, databases or providers change.

It separates shared meaning from implementation: source evidence, changes,
corrections, authority and recovery should remain understandable across systems.
It does not prescribe a retrieval engine or require one database.

Core provides a PostgreSQL reference implementation. User MCP develops bounded
access. Household OS and Vault apply the shared foundations to different domains.
The parent repository explains those relationships; it does not define the protocol.

SMP remains under development, not a published standard or a blanket conformance
claim. Start with the
[public architecture explanation](https://github.com/jryski/sovereign-memory-core/blob/main/docs/positioning.md).
That explanatory document is not a normative specification.

## Current state

The complete system is not built. Component repositories own their code,
tests, decisions and release status. Their green checks do not establish
production readiness for a deployment.

| Component | Purpose | Current limit |
| --- | --- | --- |
| [Sovereign Memory Core](https://github.com/jryski/sovereign-memory-core) | PostgreSQL reference implementation | v0.3-alpha released with bounded PostgreSQL restore evidence; deployment readiness remains scope-specific |
| [Supabase User MCP](https://github.com/jryski/Supabase_user_MCP) | Limited application-data access under user/client database permissions | Accepted local, read-only, synthetic-data profile; remote OAuth remains under review |
| [Household OS](https://github.com/jryski/Household-OS) | Household planning and integration patterns | Early implementation with synthetic examples; not a ready-to-run household product |
| [Sovereign Vault](https://github.com/WireSpeedComputing/Sovereign-Vault) | Business knowledge and operations schemas | Shared credentials do not prove separate human and agent identity |
| [Public AI Skills](https://github.com/jryski/Public_AI_SKills) | Reusable problem-solving skills | Personal-use license; organizational use needs separate written permission |

User MCP's alpha release-candidate metadata is merged. Remote access is tracked
in [draft PR #64](https://github.com/jryski/Supabase_user_MCP/pull/64);
publication remains a separate decision under
[issue #61](https://github.com/jryski/Supabase_user_MCP/issues/61).
Read the component's current evidence before using it.

Core's [v0.3-alpha release](https://github.com/jryski/sovereign-memory-core/releases/tag/v0.3-alpha)
records PostgreSQL 15/16 conformance and perimeter evidence, plus an independent
clean provider-exit restore on PostgreSQL 16. Its stated limits still apply.

## Where to start

- [THESIS.md](THESIS.md): purpose and principles.
- [ROUTES.md](ROUTES.md): the repository that owns each concern.
- [CONTEXT.md](CONTEXT.md): a short routing guide for agents and contributors.
- [HORIZON.md](HORIZON.md): possible future capabilities, not present features.
- [decisions/](decisions/): public decision pointers.

For implementation work, follow the owning repository's issue, code and
review process. This parent is an orientation guide, not another task
database or source of runtime permission.

## Company, funding and licensing

WIRE SPEED COMPUTING LLC provides the business home for development,
cost tracking and future support or licensing arrangements. The technical
goal remains user control and interoperability, not dependence on one vendor.

Company maintenance does not change existing license terms or assign
contributors' rights. Check each repository's license and notices; do not
assume every component has the same terms.

## Public and private boundaries

Public material contains code, architecture, synthetic fixtures and sanitized
lessons. Credentials, real household or business records, private deployment
details and restricted review evidence stay out.

Household and business deployments may use different schemas and policies.
A useful local finding becomes a generic contribution only after review.
A public link does not grant access to a private system.

## Development process

Use one implementation owner per task and independent review where needed.
Keep planned, implemented, tested and released states distinct. Merge,
deployment and publication require their own approval.

The website explains the work for readers. Repositories provide the evidence.
