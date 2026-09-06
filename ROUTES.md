# Public Routes

This file is intentionally small. It routes humans and agents to the
public component that owns a concern.

It is **not** a status database, permission file, or complete inventory.
Private components exist and are omitted by default.

| Concern | Public route | Authority there | Contribution |
| --- | --- | --- | --- |
| Program purpose and invariant principles | [`THESIS.md`](THESIS.md) | This parent thesis for public program orientation | orientation |
| Plausible future / bridge to possible | [`HORIZON.md`](HORIZON.md) | Directional horizon only, not current-state evidence | orientation |
| PostgreSQL reference implementation, custody, recovery, conformance, adversarial evidence | [`jryski/sovereign-memory-core`](https://github.com/jryski/sovereign-memory-core) | Repository code, tests, status, releases, exact-head evidence | generic-upstream |
| Principal-bound Supabase user/agent runtime access | [`jryski/Supabase_user_MCP`](https://github.com/jryski/Supabase_user_MCP) | Identity/access implementation and its tests/evidence | generic-upstream |
| Public household-domain architecture and synthetic household patterns | [`jryski/Household-OS`](https://github.com/jryski/Household-OS) | Household reference schemas/contracts/tests only | generic-upstream |
| Public business-domain reference architecture | [`WireSpeedComputing/Sovereign-Vault`](https://github.com/WireSpeedComputing/Sovereign-Vault) | Generic business schemas/contracts/tests only | generic-upstream |
| Reusable AI skills | [`jryski/Public_AI_SKills`](https://github.com/jryski/Public_AI_SKills) | Skill specifications, versions, usage/license terms | generic-upstream |

The `Contribution` column is durable typing, not a status tracker:

- **orientation** — read for purpose, invariants, or horizon; do not treat
  as implementation authority.
- **generic-upstream** — public-safe work belongs in that repository after
  private payload is removed.

## Private and operational coverage

Private runtime, deployment, recovery, model-evaluation, review-UI,
ingestion, and other operational components exist outside this public
route map.

They are intentionally not named here by default. A task that requires
private coverage must enter through an authorized private bootstrap
rather than infer nonexistence from this file.

## Business-specific vs generic upstream

Use the owning public route above only for generic architecture, schemas,
tests, and reusable defects.

- **Generic upstream contribution:** issue or PR to the public repository
  that owns the concern. Follow that repository's review and evidence
  path.
- **Business-specific work:** keep policy, private data, customer facts,
  topology, credentials, and deployment-only behavior in the authorized
  business deployment. Do not open it against this parent or a public
  child until it has been genericized.

Wirespeed is a downstream business dogfood consumer. Downstream evidence
does not self-promote upstream. Upstream acceptance does not force
downstream parity. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## How to choose a route

Use the narrowest owning component:

- **Protocol/meaning question:** follow the accepted protocol/specification
  route from authorized program context. Do not infer protocol semantics
  from a deployment repository.
- **PostgreSQL behavior or custody proof:** Core.
- **User/agent identity, capability, RLS/runtime access:** User MCP.
- **Household ontology, school, assets, family planning, home
  integrations:** Household OS.
- **Business ontology, team operations, business planning:** Sovereign
  Vault for generic public reference; the authorized business deployment
  for business-specific work.
- **Program-wide purpose or cross-repo orientation:** this parent
  (`THESIS.md`, `README.md`, this file). Do not add a circular parent
  repository row to the table above.

If a concern spans repositories, identify the owning contract first. Do
not copy the same fact into multiple repos to make routing easier.

## Source-of-truth rule

- Child repository: its code, tests, releases, issues, and component
  decisions.
- Deployment store: live operational data for that deployment.
- Planning/work store: work state, claims, dependencies, and review
  state.
- This parent: routes and public program framing.

A link from this file does not grant mutation authority in the
destination.
