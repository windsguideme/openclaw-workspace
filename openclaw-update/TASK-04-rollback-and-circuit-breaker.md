# TASK-04 Rollback and Circuit Breaker

## Scope
Implement the safety runtime for high-risk execution.

## Includes
- snapshot manager
- file backup support
- workspace snapshot support
- restore logic
- ops side-effect action log
- runtime budget contract
- circuit breaker

## Files to add
- `runtime/rollback/snapshot-manager.ts`
- `runtime/rollback/file-backup.ts`
- `runtime/rollback/workspace-snapshot.ts`
- `runtime/rollback/action-log.ts`
- `runtime/rollback/restore.ts`
- `runtime/governance/timeout-manager.ts`
- `runtime/governance/token-meter.ts`
- `runtime/governance/retry-policy.ts`

## Contracts
```ts
export type RollbackMode = "file" | "workspace" | "none"

export type RuntimeBudget = {
  maxSeconds: number
  maxTokens: number
  maxToolCalls: number
  maxRetriesPerStep: number
  maxRepeatedSameFailure: number
}

export type ActionLogEntry = {
  ts: string
  action: string
  target: string
  reversible: boolean
  rollbackHint?: string
  status: "started" | "done" | "failed"
}
```

## Required behavior
- snapshot is mandatory before medium/high-risk coder or ops runs
- rollback mode is selected by governor and honored by runtime
- circuit breaker must trip on timeout, token limit, tool loop, or unchanged repeated failure
- tripped runs must return a structured `SpecialistResult`

## Acceptance criteria
- file-level backup and restore work for changed files
- workspace-level snapshot and restore work for high-risk runs
- circuit breaker can stop execution without corrupting the final result contract
