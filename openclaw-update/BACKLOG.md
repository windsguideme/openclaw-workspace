# Backlog

## Phase 0 — Repo scaffolding

### OCU-001 Create configuration skeleton
**Goal**: add config folders and starter config files for agents, models, and runtime policies.

**Deliverables**
- `config/openclaw.json5`
- `config/models.json`
- `config/agents/main.json`
- `config/agents/research.json`
- `config/agents/coder.json`
- `config/agents/ops.json`
- `config/policies/spawn-governor.json`
- `config/policies/risk-policy.json`
- `config/policies/circuit-breaker.json`
- `config/policies/rollback-policy.json`

**Depends on**: none
**Suggested owner**: Codex

---

## Phase 1 — Core contracts and routing

### OCU-010 Add task framing contract
**Goal**: define `TaskFrame` and frame extraction entrypoint.

### OCU-011 Add compiled plan contract
**Goal**: define `CompiledPlan`, step schema, and execution modes.

### OCU-012 Add route selector
**Goal**: map task frame + plan into `direct | json_step | workflow | specialist`.

### OCU-013 Add spawn governor
**Goal**: enforce when specialist spawning is allowed.

**Depends on**: OCU-001, OCU-010, OCU-011, OCU-012

---

## Phase 2 — Specialist runtime

### OCU-020 Add specialist task/result contracts
**Goal**: define strict JSON input/output contracts for research/coder/ops specialists.

### OCU-021 Add spawn wrapper
**Goal**: implement specialist spawn wrapper with preflight hooks.

### OCU-022 Add announce/result parser
**Goal**: normalize specialist return payloads and reject malformed output.

**Depends on**: OCU-013, OCU-020

---

## Phase 3 — Safety controls

### OCU-030 Add snapshot manager
**Goal**: implement file/workspace snapshot creation before high-risk specialist execution.

### OCU-031 Add restore logic
**Goal**: restore from file or workspace snapshot after failure.

### OCU-032 Add action log for ops
**Goal**: capture reversible/non-reversible side effects.

### OCU-033 Add runtime budget contract
**Goal**: define time/token/tool/retry budgets.

### OCU-034 Add circuit breaker
**Goal**: stop runs on timeout, token limit, tool loops, or unchanged failures.

**Depends on**: OCU-021

---

## Phase 4 — Workflow runtime

### OCU-040 Add workflow step and definition contracts
**Goal**: define workflow step APIs.

### OCU-041 Add workflow engine
**Goal**: execute typed workflows under shared runtime guards.

### OCU-042 Add first workflow: research.compare.multi-source
**Goal**: implement gather → normalize → compare → compose → verify.

**Depends on**: OCU-034, OCU-040

---

## Phase 5 — Skill loading and telemetry

### OCU-050 Add skill catalog loader
**Goal**: support level-1 catalog loading.

### OCU-051 Add guide/resource loader
**Goal**: support level-2 guide and level-3 resource loading.

### OCU-052 Add execution telemetry
**Goal**: log route, failures, retries, token/tool/time usage.

### OCU-053 Add skill observation recorder
**Goal**: collect data for future skill patch proposals.

### OCU-054 Add skill patch proposal generator
**Goal**: generate offline candidate patches only; no auto-apply.

**Depends on**: OCU-041

---

## Phase 6 — Tests and migration

### OCU-060 Add unit tests for spawn governor
### OCU-061 Add unit tests for circuit breaker
### OCU-062 Add unit tests for rollback manager
### OCU-063 Add integration tests for main → specialist flows
### OCU-064 Add migration notes

**Depends on**: all previous phases

---

## Suggested implementation batches for Codex

### Batch A
- OCU-001
- OCU-010
- OCU-011
- OCU-012

### Batch B
- OCU-013
- OCU-020
- OCU-021
- OCU-022

### Batch C
- OCU-030
- OCU-031
- OCU-032
- OCU-033
- OCU-034

### Batch D
- OCU-040
- OCU-041
- OCU-042

### Batch E
- OCU-050
- OCU-051
- OCU-052
- OCU-053
- OCU-054

### Batch F
- OCU-060
- OCU-061
- OCU-062
- OCU-063
- OCU-064
