# TASK-06 Tests and Migration

## Scope
Add the safety net and rollout notes needed to move from the current architecture to v1.1.

## Includes
- unit tests for governor
- unit tests for circuit breaker
- unit tests for rollback
- integration tests for main -> specialist flows
- malformed result fallback test
- migration notes

## Files to add
- `tests/spawn-governor.spec.ts`
- `tests/circuit-breaker.spec.ts`
- `tests/rollback.spec.ts`
- `tests/workflow-engine.spec.ts`
- `tests/contracts.spec.ts`
- `openclaw-update/MIGRATION.md`

## Required coverage
- low-complexity task does not spawn
- at-most-one-specialist-per-turn guard works
- malformed specialist JSON is rejected
- snapshot restore executes on failed high-risk task
- timeout/token/tool-loop trips are surfaced correctly
- workflow execution respects runtime budget

## Migration note topics
- how current planner maps to task framer + plan compiler
- how legacy multi-agent flows are reduced to single-layer specialist execution
- how to phase in per-agent sandbox policies
- rollout flags and fallback strategy

## Acceptance criteria
- tests cover the main routing and safety invariants
- migration guide explains how to phase in the architecture without breaking current behavior
