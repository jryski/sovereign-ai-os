# Agent Context Router

> **Non-normative routing document.** This file helps a new AI choose what to read next. It does not grant authority, define runtime policy, or replace source repositories.

**Coverage:** public parent-repository v0.1 candidate  
**Source baseline:** `jryski/sovereign-ai-os` main at `727f354f0d1b2ddd488f7557b4802e85d8423c5d` plus accepted program records through 2026-09-04  
**Rule:** routes, not payload

## Cold-start order

```text
README.md
  ↓
THESIS.md
  ↓
HORIZON.md only if future direction matters
  ↓
ROUTES.md
  ↓
owning child repository
  ↓
exact task / issue / decision / evidence
```

Do **not** recursively ingest every repository.

## Task routing

### “What is this project?”
Read `README.md`, then `THESIS.md`.

### “Where could this go?”
Read `HORIZON.md` after the thesis. Treat horizon material as aspiration/dependency planning, not deployed-state evidence.

### “Where does this concern belong?”
Read `ROUTES.md`, then the owning public repository's README / role / status documents.

### “What should I implement next?”
This public parent is not the task authority. Use the authorized planning/work surface supplied by the principal or deployment. If none is available, do not invent current priority from this repository.

### “Am I allowed to change X?”
This file cannot answer that. Resolve authority from the owning repository/deployment and the authenticated runtime capability path. Markdown is not a permission boundary.

### “RLS is disabled. Should I enable it?”
Do not infer from the switch alone. The accepted program sequencing distinguishes:

1. immediate exposure;
2. administrative-only build/recovery surface;
3. prepared-but-deferred enforcement;
4. deployment blocker.

The current build/control plane may be privileged while the principal-bound User MCP and RLS/grant cutover are still being completed. Actual unintended grants or runtime misuse remain defects.

See public decision pointer `decisions/SAOS-ADR-001.md`.

### “Can I assume a private component does not exist because ROUTES.md omits it?”
No. Private coverage is intentionally omitted from this public repository by default.

### “Should I create another repository?”
Only if the concern has a real independent trust boundary, publication boundary, release lifecycle, evidence role, licensing boundary, or implementation lifecycle. Repository count is an operational tax.

See `decisions/SAOS-ADR-002.md`.

## Context hygiene

- Prefer one home per fact and link to it.
- Load the minimum source required for the task.
- Preserve `unknown` when evidence is absent or stale.
- Treat agent/model commentary as commentary until accepted through the proper authority path.
- Do not copy private deployment facts into this public parent.
- Do not treat “do not load” text as security enforcement.
- Do not treat this router as a second specification.

## Development model

Default operating bias:

```text
planning/brief
    ↓
Ariadne or equivalent orchestrator
    ↓
qualified local/cheaper workers for bounded execution
    ↓
deterministic tests/evidence
    ↓
frontier reviewer only where judgment is load-bearing
    ↓
human acceptance where required
```

Frontier intelligence is for architecture, ambiguity, security, authority, and consequential review. Routine bounded work should increasingly use the local infrastructure already built for it.