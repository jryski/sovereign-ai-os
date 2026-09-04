# Sovereign AI OS

**A sovereign operating substrate for people and organizations in an age of abundant intelligence.**

Sovereign AI OS is a long-lived, owner-controlled foundation for AI that preserves durable meaning, evidence, authority, context, work, and action history while models, vendors, applications, runtimes, and storage systems remain replaceable.

This is a **functional sovereignty project**, not a startup thesis or financial endeavor. The goal is to build infrastructure that can grow with AI for decades without requiring a person, household, or organization to surrender its accumulated context to whichever vendor has the best assistant this year.

> **If intelligence becomes cheap, abundant, persistent, multimodal, agentic, networked, and eventually embodied, what infrastructure must a human or organization own so that intelligence reliably acts in their interest?**

This repository is the public front door to that work.

## Start here

1. **[THESIS.md](THESIS.md)** — why the project exists and the principles that should survive changes in technology.
2. **[HORIZON.md](HORIZON.md)** — the plausible future the architecture is trying to keep open. This is directional, not a claim about current capability.
3. **[ROUTES.md](ROUTES.md)** — where public implementation concerns live and which repository owns them.
4. **[CONTEXT.md](CONTEXT.md)** — a thin, non-normative routing guide for new AI agents and contributors.
5. **[decisions/](decisions/)** — concise public decision pointers. They summarize rulings; they do not create authority.

## The progression

The repositories make more sense as an evolutionary dependency chain than as independent projects:

```text
sovereign memory / protocol semantics
        ↓
reference implementation + recovery/conformance proof
        ↓
principal-bound user/agent data access
        ↓
household and business domain deployments
        ↓
planning + context + worker/runtime routing
        ↓
presentation and presence
        ↓
ambient stewardship
        ↓
sanitized steward-to-steward exchange
        ↓
external agent/service networks
        ↓
physical sensing and actuation where useful
```

Not every layer is implemented yet. Some capabilities have not been invented yet. The architectural goal is to build useful capability now while leaving clean seams for the frontier to evolve.

## What this parent repository is

This repository exists to answer:

- What are we building and why?
- What principles are invariant?
- Which public component owns a concern?
- What should a new human or AI read next?
- What private coverage is intentionally omitted?

It is a **router and human-readable program front door**.

## What this parent repository is not

It is not:

- a monorepo;
- a second implementation authority;
- a duplicate planning/task database;
- a mirror of private deployment topology;
- a source of runtime permission;
- a replacement for the owning repository's code, tests, issues, releases, or evidence;
- a claim that every horizon idea already works.

**Routes point to authority. They do not create it.**

## Two organizational deployment families

The same kernel ideas can serve very different organizations without forcing schema parity.

### Household OS

The household deployment can model people, rooms, devices, vehicles, school, events, maintenance, food, preferences, projects, routines, shared planning, and household history while preserving per-person private trust domains.

### Business OS

The business deployment can model people, teams, products, suppliers, customers, projects, incidents, compliance, approvals, planning, and business-specific integrations under a different trust and policy model.

Household and Business OS are peers in end-state function. Their tables, policies, stores, principals, and integrations are allowed to diverge.

Wirespeed additionally serves as downstream business dogfood: useful generic lessons can be contributed upstream through normal public-safe review without moving private business data or authority with them.

## Build the spaceship while flying it

This platform is already useful while foundational pieces are still under construction. Transitional states must therefore be explicit.

For example, the current privileged Supabase MCP is a build/control-plane tool. The intended runtime path is principal-bound through the User MCP, with database-enforced policy activated through a coordinated cutover once it can actually be exercised and proven.

Premature claims of completeness are defects. So is freezing useful development because an end-state mechanism cannot yet be safely activated.

## Public/private boundary

Public repositories contain generic architecture, code, synthetic fixtures, tests, and sanitized lessons.

Private deployments, private repository locators, credentials, real household/business data, topology, private planning state, and restricted evidence are omitted from this parent by default.

Absence from this public router does **not** mean a private component does not exist.

## Current status

This parent repository is being established as the single maintained public cross-program orientation surface. Child repositories remain authoritative for their own implementation. Cross-program umbrella material previously living in Sovereign Memory Core will be reduced to compatibility pointers after this parent is accepted.

The project deliberately favors useful capability over governance theater: frontier models for architecture/security/judgment, local and cheaper models for bounded execution, and review depth proportional to consequence.
