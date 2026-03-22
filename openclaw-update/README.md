# OpenClaw Update

This directory contains the engineering rollout plan for the OpenClaw v1.1 architecture update.

## Goal

Implement a production-ready architecture that favors:

- single main orchestrator
- minimal A2A interaction
- typed workflow over freeform multi-agent collaboration
- guarded one-shot specialist subagents
- rollback + circuit breaker protections
- progressive skill loading and telemetry-driven skill evolution

## Delivery strategy

The work is split into sequenced task groups so Codex can implement them incrementally with clear scope boundaries.

## Recommended order

1. Core contracts and config scaffolding
2. Task framing + plan compiler + route selector
3. Spawn governor
4. Specialist contract + spawn wrapper
5. Rollback layer
6. Circuit breaker / runtime budgets
7. Workflow runtime
8. Skill loader + telemetry
9. Integration tests and migration notes

## Files in this directory

- `BACKLOG.md`: master task list and dependency order
- `TASK-01-core-contracts.md`
- `TASK-02-routing-and-governor.md`
- `TASK-03-specialists-runtime.md`
- `TASK-04-rollback-and-circuit-breaker.md`
- `TASK-05-workflows-skills-telemetry.md`
- `TASK-06-tests-and-migration.md`

## Usage with Codex

Recommended prompt pattern:

> Read `openclaw-update/BACKLOG.md` and `openclaw-update/TASK-0X-*.md`. Implement only the selected task. Keep changes scoped. Add tests for new runtime guards and contracts. Do not introduce nested subagent delegation.
