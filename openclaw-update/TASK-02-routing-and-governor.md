# TASK-02 Routing and Spawn Governor

## Scope
Implement the routing path that decides whether a request stays in main, uses a JSON step, enters workflow mode, or spawns a single specialist.

## Includes
- spawn decision contract
- spawn governor implementation
- routing constraints
- turn-level spawn count guard

## Files to add
- `runtime/governance/spawn-governor.ts`
- `runtime/governance/risk-evaluator.ts`
- `runtime/orchestrator/budget-manager.ts`

## Core contract
```ts
export type SpawnDecision = {
  allowed: boolean
  reason:
    | "needs_isolation"
    | "needs_long_running"
    | "needs_specialized_tools"
    | "too_simple"
    | "budget_exceeded"
    | "json_step_sufficient"
    | "a2a_not_worth_it"
    | "spawn_limit_reached"
  targetAgent?: "research" | "coder" | "ops"
  model?: string
  timeoutSec?: number
  requireSnapshot?: boolean
  rollbackMode?: "file" | "workspace" | "none"
}
```

## Required behavior
- default spawn count per turn: 0
- allow at most 1 specialist spawn per turn by default
- refuse spawn for low-complexity tasks with no isolation/tool need
- prefer `json_step` over specialist whenever sufficient
- require snapshot for medium/high-risk coder or ops runs

## Acceptance criteria
- spawn governor returns deterministic decisions from task inputs
- no code path allows specialist -> specialist delegation
- budget and complexity signals affect routing
