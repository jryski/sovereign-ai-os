# Agent Context Router

> **Non-normative routing document.** This file helps a new AI choose
> what to read next. It does not grant authority, define runtime policy,
> or replace source repositories.

**Coverage:** public parent-repository orientation surface
**Rule:** routes, not payload. Generate or omit moving/current state.

## Cold-start order

```text
README.md
  ↓
ROUTES.md
  ↓
owning child repo / exact task evidence
  ↓
THESIS.md when mission/invariants are needed
  ↓
HORIZON.md only when future direction matters
```

Do **not** recursively ingest every repository.

## Task routing

### “What is this project?”

Read `README.md`. Read `THESIS.md` when mission or invariant principles
are needed.

### “Where could this go?”

Read `HORIZON.md` after the thesis when future direction matters. Treat
horizon material as aspiration/dependency planning, not deployed-state
evidence.

### “Where does this concern belong?”

Read `ROUTES.md`, then the owning public repository's README / role /
status documents.

### “What should I implement next?”

This public parent is not the task authority. Use the authorized
planning/work surface supplied by the principal or deployment. If none
is available, do not invent current priority from this repository.

### “Am I allowed to change X?”

This file cannot answer that. Resolve authority from the owning
repository/deployment and the authenticated runtime capability path.
Markdown is not a permission boundary.

### “RLS is disabled. Should I enable it?”

Do not infer from the switch alone. The accepted program sequencing
distinguishes:

1. immediate exposure;
2. administrative-only build/recovery surface;
3. prepared-but-deferred enforcement;
4. `prepared_not_exercised` — structurally prepared, but never
   successfully resolved a real authenticated principal;
5. deployment blocker.

`prepared_not_exercised` is materially weaker than prepared/deferred.
Do not treat it as testable on demand.

The current build/control plane may be privileged while the
principal-bound User MCP and RLS/grant cutover are still being
completed. Actual unintended grants or runtime misuse remain defects.

See public decision pointer `decisions/SAOS-ADR-001.md`.

### “Can I assume a private component does not exist because ROUTES.md omits it?”

No. Private coverage is intentionally omitted from this public
repository by default.

### “Is this business-specific work or generic upstream contribution?”

Business-specific policy, private data, deployment topology, and
downstream-only behavior stay in the authorized business deployment.
Genericize and remove private payload before opening an issue or PR
against the owning public upstream repository. See `CONTRIBUTING.md`
and `ROUTES.md`.

### “Should I create another repository?”

Only if the concern has a real independent trust boundary, publication
boundary, release lifecycle, evidence role, licensing boundary, or
implementation lifecycle. Repository count is an operational tax.

See `decisions/SAOS-ADR-002.md`.

## Context hygiene

- Prefer one home per fact and link to it.
- Load the minimum source required for the task.
- Preserve `unknown` when evidence is absent or stale.
- Treat agent/model commentary as commentary until accepted through the
  proper authority path.
- Do not copy private deployment facts into this public parent.
- Do not treat “do not load” text as security enforcement.
- Do not treat this router as a second specification.
- Do not cite a commit hash from a file contained in that commit.

## Development model

Default operating bias:

```text
planning/brief
    ↓
qualified orchestrator
    ↓
qualified local/cheaper workers for bounded execution
    ↓
deterministic tests/evidence
    ↓
frontier reviewer only where judgment is load-bearing
    ↓
human acceptance where required
```

Frontier intelligence is for architecture, ambiguity, security,
authority, and consequential review. Routine bounded work should
increasingly use the local infrastructure already built for it.
