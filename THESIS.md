# Sovereign AI Platform — Governing Thesis

**Status:** Canonical public program thesis  
**Effective:** 2026-09-04  
**Source lineage:** consolidates the earlier data-sovereignty thesis, mission/alignment work, Sovereign AI OS charter, and subsequent principal corrections. It is intended to preserve the mission, not erase the history that produced it.

## Thesis in one sentence

Build a **long-lived, owner-controlled AI operating substrate** that preserves durable meaning, evidence, authority, context, work, and action history across changes in models, vendors, applications, runtimes, storage systems, and deployment domains, so an authorized AI can become deeply useful without becoming the owner of the person or organization it serves.

## Why this project exists

AI is still in its infancy.

The models, interfaces, agent runtimes, memory systems, storage products, integration standards, and dominant vendors of today will not define the next several decades.

The mistake would be to build a life, household, or business around whichever AI application happens to be best this year.

The deeper problem is not simply that chats forget. Useful context, decisions, corrections, evidence, relationships, project state, permissions, workflows, and history are repeatedly trapped inside systems the user does not control. Each new model arrives partially blind. Each provider invents its own memory. Each application creates another silo.

As AI becomes more capable, this fragmentation matters more because AI increasingly does not just answer questions. It acts.

This project exists to make models, providers, applications, runtimes, and storage systems **replaceable while the durable organizational understanding survives**.

## This is not a financial endeavor

This program is not being built as a startup thesis, monetization strategy, investment vehicle, or attempt to capture a market category.

It is a **functional sovereignty project**: build infrastructure expected to remain useful for decades, first for a person and household and also for organizations that choose to operate under the same principles.

Commercial businesses can consume the architecture. Wirespeed can dogfood it. Individual components may eventually have licenses, hosted services, enterprise arrangements, or other economics around them. Those are downstream governance questions.

They do not define the mission and should not distort the architecture toward lock-in, artificial scarcity, growth metrics, or commercial fashion at the expense of sovereignty and function.

The primary measure is:

> **Does this make the human or organization more capable, continuous, accurate, autonomous, and less dependent on any single AI vendor?**

## The governing principle

> **Own the durable meaning, evidence, authority, and action history. Treat models, applications, providers, storage engines, and integrations as replaceable clients and workers.**

An earlier formulation was:

> **We own the durable data layer, not the application layer.**

That remains correct, but *data* is too narrow. The durable asset is not merely rows. It is the meaning surrounding those rows:

- what an entity is;
- what is believed about it;
- why that belief exists;
- who or what observed or asserted it;
- when it was true;
- what conflicts with it;
- what superseded it;
- who may see or change it;
- what work was intended;
- what action was taken;
- what happened afterward;
- whether the outcome was verified.

That meaning must outlive the current model, database, application, and provider.

## The intended end state

For an authorized principal, the system should eventually be able to:

- answer essentially any question that can be answered from the organization's permitted knowledge and connected evidence;
- understand fuzzy human references in context rather than require database-language precision;
- know people, places, assets, projects, commitments, policies, relationships, history, preferences, and current operational state;
- assemble the **smallest sufficient context** for the task instead of dumping an archive into a context window;
- explain why it believes an answer and expose material uncertainty, conflict, provenance, and staleness;
- notice when prior understanding is contradicted and propose correction rather than silently overwrite history;
- plan work, track dependencies, delegate bounded tasks, and preserve handoffs;
- select an appropriate qualified local model, hosted model, specialized tool, application, or human worker;
- perform authorized tasks through integrations;
- obtain required approval before consequential actions;
- preserve receipts for actions, side effects, failures, reversals, and reconciliation;
- learn from verified outcomes and corrections without promoting model inference into truth;
- operate locally or offline where useful;
- survive provider failure, model replacement, database migration, interface change, and organizational growth;
- export and reconstruct durable state in an intelligible form outside the current stack.

The aspiration is not a chatbot with a very large memory. It is an **operating substrate for an organization that includes AI participants**.

## Accuracy is an architectural property

“Wildly accurate” cannot mean selecting a smarter model and trusting it harder.

Accuracy comes from the system around the model:

1. preserve original evidence;
2. retain provenance at the level needed to explain material claims;
3. distinguish observation, assertion, derivation, inference, proposal, acceptance, verification, dispute, rejection, supersession, and unknown;
4. preserve multiple clocks where they matter: observed, effective, recorded, accepted, superseded;
5. keep conflicting evidence visible;
6. resolve entity identity separately from attribute value;
7. require authority for promotion and consequential change;
8. test important invariants mechanically;
9. record actions and outcomes;
10. feed verified corrections back into future context assembly.

Self-correction is therefore not a personality trait of the AI. It is a system property produced by provenance, contradiction visibility, proposal/review, supersession, tests, receipts, and reconciliation.

**Unknown is preferable to plausible fiction.**

## Context is assembled, not accumulated

Continuity should not be solved by giving every model every stored record.

Contextual awareness means resolving the current request against the organization's governed state:

```text
principal + request + intent + authority
        ↓
resolve subjects and relationships
        ↓
retrieve relevant durable knowledge
and current observations
        ↓
attach provenance, conflict, history,
policy, capabilities, and staleness
        ↓
produce a bounded context envelope
        ↓
reason / plan / answer / act
```

Embeddings, vector indexes, caches, summaries, rankings, and model-specific context formats are disposable projections.

They are not the durable truth.

## Knowledge, state, planning, action, and evidence are different

The platform must resist turning everything into one generic memory system.

- **Knowledge** is durable understanding of reality and history.
- **Operational state** is what is happening now and may become irrelevant quickly.
- **Planning** is intended work, dependency, ownership, sequencing, review, and acceptance.
- **Action** is an authorized attempt to change reality.
- **Evidence and receipts** support claims about what occurred.

These things connect, but they have different lifecycles and authorities.

That is why Home Assistant telemetry, household assets, a family kanban, financial history, model coordination, and action receipts should not become one giant table simply because one AI may reason across them.

## Presentation and presence are first-class behavior

A technically correct answer delivered on the wrong surface, at the wrong time, or with unnecessary user effort is an incomplete outcome.

The system therefore needs to reason about **how, where, and when** useful context or action should meet the user.

Given an intent and authorized context, it should consider:

- who the user or audience is;
- what the user is actually trying to accomplish;
- what device or surface is available: chat, phone, calendar, smart display, voice, dashboard, Home Assistant, email, shared board, business workspace, or future interface;
- timing, urgency, interruption cost, persistence, privacy, and reversibility;
- whether the best outcome is a simple answer, visualization, reminder, calendar item, shared task, notification, automation, integration, offer, or no additional presentation at all;
- what authority exists to present, propose, schedule, share, or act.

The governing interaction principle is friction reduction: **take the shortest trustworthy path from human intent to a useful outcome**.

The human should not have to understand the plumbing or translate the same intent across five applications.

Presentation remains a consumer of authority, not a source of it. A calendar, smart display, dashboard, notification, or Home Assistant surface does not become canonical truth because information appears there.

## Authority belongs below the model

Models and agents are workers, not self-authorizing principals.

Prompts may improve behavior, but they are not security boundaries.

Real authority must ultimately be represented and enforced through appropriate mechanisms such as:

- authenticated human and agent identity;
- scoped credentials and tokens;
- database grants and row-level policy;
- capability-specific tools;
- integration scopes;
- sandbox boundaries;
- approvals;
- revocation and expiry;
- audit and receipts.

The current privileged Supabase MCP is intentionally the **build/control plane**. It exists because the system is still being constructed, migrated, inspected, repaired, and recovered.

It is not the eventual ordinary user or agent runtime access model.

`Supabase_user_MCP` is the intended principal-bound runtime data plane. RLS/grant enforcement is prepared while the system is built, then activated as a coordinated runtime cutover once the access path can exercise and prove those policies.

This is sequencing, not abandonment of security.

## One kernel, different organizations

The household and business systems should not be one schema copied twice.

They are separate organizational deployments over shared architectural primitives.

### Household

A household implementation can model people, family roles, rooms, places, devices, vehicles, appliances, infrastructure, services, school, activities, events, chores, maintenance, projects, purchases, errands, food, preferences, household history, troubleshooting, planning, and household agents.

Per-person private domains remain distinct from shared household knowledge.

The practical test is whether questions such as:

> “The living-room TV won't work.”

> “What's lunch at school Tuesday?”

> “Which furnace filter do I need?”

> “What needs attention this weekend?”

can be answered from the household's actual context and history rather than generic internet advice.

### Business

A business implementation may model people, teams, contractors, products, suppliers, quotes, orders, inventory, customers, projects, incidents, approvals, compliance, evidence, meetings, planning, and operational workflows.

Its ontology, policies, credentials, integrations, and operational authority remain business-owned.

Household OS and Business OS are therefore **organizational peers in end-state function**. Both seek continuity, context, correction, planning, safe action, and audit.

They do not need identical tables, product behavior, or policy.

### Wirespeed and the upstream program

There is a second relationship axis.

Wirespeed is a **downstream business dogfood consumer** of the shared upstream development program.

Its discoveries can produce generic improvements upstream, but only through deliberate genericization and normal review:

```text
upstream contracts and reference components
        ↓
Wirespeed business adaptation
        ↓
real dogfood observations and defects
        ↓
public-safe generic proposal
        ↓
owning upstream repository review
        ↓
accepted generic improvement
        ↓
optional downstream adoption
```

A downstream finding does not self-promote into upstream truth.

An upstream change does not automatically become business policy.

Private business data, deployment authority, customer information, topology, credentials, and migration bodies do not travel upstream merely because a useful generic idea was discovered downstream.

## Why there are multiple repositories

The repository count is not purely accidental fragmentation. The system has been decomposed along real boundaries that sometimes need independent development, proof, publication, replacement, trust, licensing, or release cycles.

Those concerns include protocol semantics, PostgreSQL reference implementation, principal-bound access, household architecture, business architecture, private deployment overlays, planning, runtime orchestration, model qualification, portable storage, ingestion, review interfaces, reusable skills, integrations, recovery, and evidence.

But repository count is also a tax.

A repository should earn its existence through a real independent trust boundary, publication boundary, release lifecycle, evidence role, licensing boundary, or implementation lifecycle. Weak boundaries should consolidate or archive rather than survive forever because they already exist.

No child repository is the entire project.

## The role of this parent repository

The public parent is the **human and agent front door** to the program.

It should answer:

1. What are we building and why?
2. Which principles must survive implementation changes?
3. Which public components own which concerns?
4. What should a new human or AI read next?
5. What private coverage is intentionally omitted?

It is a router and public framing layer.

It is **not** a monorepo, second implementation repository, duplicate planning database, copy of every child roadmap, private topology mirror, filesystem replacement for database authority, or source of permission because Markdown says an agent may act.

**Routes point to authority. They do not create authority.**

## Open by design

AI technology is too young for this architecture to assume today's winner will remain tomorrow's winner.

The program should **use and translate rather than compete and replace**.

When standards, protocols, formats, transports, runtimes, or models emerge:

- use them where they fit;
- profile meaningful differences;
- translate between them;
- disclose lossiness;
- retain provenance through translation;
- support multiple approaches where the ecosystem has not converged;
- avoid intentional incompatibility and walled gardens;
- contribute generic improvements upstream when possible.

The goal is not to make one project component “win.”

The goal is for the user's durable meaning and authority to survive **whichever technologies eventually win**.

## The evolutionary progression

The system is easier to understand as a progression driven by what the frontier makes possible:

```text
protocol / durable meaning / custody
        ↓
reference implementation + restore/conformance proof
        ↓
principal-bound user and agent access
        ↓
household and business domain models
        ↓
planning + context + worker/runtime coordination
        ↓
presentation and presence
        ↓
ambient stewardship
        ↓
sanitary steward-to-steward exchange across trust domains
        ↓
external agent/service networks
        ↓
physical sensing and actuation where useful
```

Some later pieces have not been invented yet.

That is expected.

The architecture should build useful capability now while leaving clean seams for capabilities that appear as the frontier evolves.

## Building the spaceship while flying it

This platform is already producing useful results while foundational pieces are under construction.

That reality should be represented honestly.

A privileged build credential can be necessary today without being acceptable as permanent runtime identity.

RLS can be prepared before activation without claiming that multi-principal isolation is currently enforced.

A context map can be useful while remaining explicitly non-authoritative.

A dogfood deployment can expose an upstream-quality defect without gaining authority over the upstream architecture.

An agent can perform bounded implementation work without acquiring merge, deployment, credential, or policy authority.

Premature claims of completeness are defects.

But freezing useful development merely because an end-state control cannot yet be safely activated is also a mistake.

The project must preserve **explicit transition states**.

## Durable over fashionable

If this system is intended to last for decades, optimize for what survives.

Durable:

```text
stable identity
source evidence
provenance
accepted decisions
temporal lineage
authority
schema semantics
versioned contracts
action receipts
exports
restore proof
migration history
source lineage
```

Disposable and rebuildable:

```text
embeddings
vector indexes
caches
summaries
model-specific prompts
hot-context rankings
current user interfaces
current model routes
current providers
current orchestration runtimes
```

A future frontier model should be able to become dramatically more capable than today's models without requiring the human or organization to surrender or rewrite its history.

## Anti-goals

The program must not become:

- a financial project whose architecture is optimized for monetization;
- a monolithic everything-app;
- a vendor-owned memory silo or proprietary walled garden;
- generic RAG mistaken for organizational memory;
- an AI agent with unrestricted owner credentials;
- a flat archive that loses source, time, authority, conflict, and correction;
- a hand-maintained context tree that becomes a competing authority;
- a system where model confidence becomes authority;
- a system where one deployment's private policy silently becomes universal protocol;
- governance machinery that consumes more effort than the useful capability it protects;
- a permanent architecture exercise that fails to make ordinary life and work more useful.

## Design test

Every substantial addition should be challenged with the same questions:

1. Does the human or organization retain ownership of canonical meaning and evidence?
2. Can today's model, provider, runtime, application, or storage substrate be replaced?
3. Is provenance retained through observation, transformation, inference, acceptance, and action?
4. Is authority explicit and enforced outside the model where consequences require it?
5. Are time, correction, conflict, and supersession represented honestly?
6. Does the component have a clear source of truth instead of creating another authority?
7. Can private deployment boundaries survive public documentation and generic contribution?
8. Can durable state be exported, restored, and independently reconstructed?
9. Does this improve concrete capability, continuity, accuracy, or sovereignty?
10. Does it preserve more future options rather than locking the program into today's answer?

## Definition of success

The project succeeds when a new authorized frontier model can be introduced years from now and, without Jesse retelling his life or an organization rebuilding its institutional memory, it can:

- understand what the organization is;
- discover the relevant context without reading everything;
- distinguish evidence from inference and present state from history;
- understand what it may access and what it may do;
- locate the component or integration that owns the task;
- answer with provenance and calibrated uncertainty;
- perform authorized work through bounded tools;
- leave durable receipts;
- accept correction without erasing history;
- hand work to another model or human without losing continuity;
- and itself be replaced without taking the organization's memory, authority, or operational history with it.

**That is the north star.**

## Orientation contract for a new frontier AI

A new model should not begin by recursively reading every repository.

Follow the cold-start order in `CONTEXT.md` (routes before thesis or
horizon payload). Then load the minimum additional source required to
act safely.

When sources conflict, preserve the conflict and follow the real authority hierarchy.

When evidence is stale or absent, report `unknown` rather than manufacture continuity.

When a task crosses personal, household, business, or administrative trust boundaries, resolve the authority boundary before combining context or acting.
