# SAOS-ADR-002 — Reduce Governance Overhead and Bias Toward Useful Capability

**Status:** Accepted direction  
**Effective:** 2026-09-04  
**Authority:** Jesse direct agreement with Fable 5.1 assessment, reconciled by Atlas

## Problem

The program accumulated unusually strong evidence, review, and provenance discipline, but the governance-to-utility ratio became inverted. Multi-model review loops, restacks, repeated re-verification, repository-orientation work, and access-surface mismatches were consuming frontier-model time that should increasingly produce useful capability and exercise local AI infrastructure.

This is not a rejection of exact evidence or independent review. It is a decision to use them proportionately to consequence.

## Ruling

1. **Bias toward useful capability.** New work should identify what concrete capability it unlocks or proves.
2. **Use frontier models for judgment.** Architecture, security, authority, ambiguous synthesis, novel design, and consequential review.
3. **Use local/cheaper workers aggressively.** Bounded drafting, fixtures, deterministic validation, routine implementation, classification, low-risk refactors, and maintenance.
4. **Tier review by consequence.** Documentation/routing should not receive the same ceremony as identity/RLS/protocol/production changes.
5. **One integrated owner, bounded reviewers.** Avoid multiple frontier models independently co-authoring the same artifact.
6. **Repository count is a tax.** A repo should justify an independent trust, publication, release, evidence, licensing, or implementation lifecycle.
7. **Do not optimize to a numeric repo target.** Consolidate weak boundaries; preserve real ones.

## Review tiers

### Tier 1 — routine / presentation / routing

Examples: README prose, route links, formatting, non-normative context docs.

Default: one reviewer or simple deterministic validation.

### Tier 2 — shared implementation / contracts

Examples: reusable APIs, context/planning contracts, connector behavior, significant refactors, non-production migrations.

Default: implementing owner plus one bounded reviewer selected for the risk.

### Tier 3 — authority / security / custody / production

Examples: identity, RLS/grants, credentials, protocol semantics, schema authority, production migrations, recovery claims, consequential actuation/release claims.

Default: exact-head evidence and independent review remain required; dual review only when the acceptance contract warrants it.

## Parent-repo consequence

The public parent should stay deliberately small and human-first:

```text
README.md
THESIS.md
HORIZON.md
ROUTES.md
CONTEXT.md
decisions/
```

No machine-readable program manifest is required in v0.1 merely because one can be designed. Add one when a real second consumer demonstrates the need.

## Local AI consequence

The intended operating asymmetry is:

```text
frontier judgment is scarce
local execution is abundant
```

Local workers should increasingly handle continuous and bounded work such as nightly reconciliation/preparation, fixture generation, repository maintenance, classification, low-risk implementation, preflight review, and drift/data-quality checks.

Cheap execution does not create authority.

## Naming consequence

A protocol-name freeze was strongly recommended to stop an expensive naming loop. Until Jesse makes a specific naming ruling, do not spend active development cycles on protocol naming unless the name becomes a concrete blocker.

## Internal lineage

Canonical governed decision: `SAOS-ADR-002` / `projects/sovereign-ai-os/decisions/operating-model-simplification`.

This file is a public pointer. It does not create permission or replace the canonical decision record.