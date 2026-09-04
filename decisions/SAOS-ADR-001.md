# SAOS-ADR-001 — Build Plane, User MCP, and RLS Cutover

**Status:** Accepted
**Effective:** 2026-08-29
**Authority:** Jesse direct ruling
**Public purpose:** prevent fresh reviewers from collapsing a staged
runtime migration into a generic “RLS is off” finding.

## Ruling

RLS activation is not an isolated hardening toggle. It is part of a
coordinated transition from the current privileged **build/control
plane** to a stable principal-bound **runtime data plane**.

The current Supabase MCP is intentionally privileged for schema work,
migrations, inspection, repair, recovery, and administration. It is
**not** the final household/business user or agent access path and
cannot prove multi-principal isolation.

The intended runtime path is `Supabase_user_MCP`, with trusted
human/agent identity, narrow capabilities, revocation/audit, and
PostgreSQL/RLS as the final row-authorization layer.

## Required interpretation

Do not treat `RLS disabled` alone as an instruction to flip live build
tables immediately.

Classify findings as one of:

1. **Immediate exposure** — unintended reachable access, grants,
   credentials, or runtime path that is wrong now.
2. **Administrative-only surface** — intentionally privileged
   build/recovery access.
3. **Prepared-but-deferred enforcement** — policy/schema work is
   required now; activation belongs to the runtime cutover.
4. **`prepared_not_exercised`** — the control is structurally prepared
   but has never successfully resolved a real authenticated principal.
   This is materially weaker than prepared/deferred. Do not treat it as
   testable on demand.
5. **Deployment blocker** — prevents adding an untrusted principal,
   tenant, child, employee, contractor, or runtime surface.

A component that claims prepared enforcement should be able to point to
evidence of a successful real-principal resolution. Until that exists,
the honest class is `prepared_not_exercised`.

## Writer-supplied provenance is not authenticated enforcement

Do not describe writer-supplied `basis` / `source_citation` checks,
including the current Sovereign Vault financial provenance trigger, as
authenticated provenance enforcement.

Those fields are convention and integrity checks until principal
identity exists below the model. A guard that keys on a writer-supplied
discriminator is a self-report check. It is not identity.

This public pointer does not grant access to Vault internals and does
not replace that repository's tests or decision records.

## Order of operations

```text
build schemas/contracts with privileged control plane
        ↓
stable principal-bound User MCP
        ↓
RLS/grant design against real caller identity
        ↓
isolated positive + negative policy testing
        ↓
move ordinary runtime off privileged access
        ↓
coordinated RLS + grants + revocation + audit cutover
        ↓
live verification + rollback-capable receipt
        ↓
privileged MCP retained only for administration/recovery
```

## What this does not excuse

Actual unintended grants, leaked/overbroad credentials, runtime agents
using the build credential as an ordinary user path, or enrolling
unsupported principals remain immediate defects.

## Internal lineage

Canonical governed decision: `SAOS-ADR-001` /
`projects/sovereign-ai-os/decisions/build-plane-to-rls-cutover`.

This file is a public pointer. It does not grant access or replace the
canonical decision record.
