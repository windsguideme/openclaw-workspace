# TASK-03 Specialist Runtime

## Scope
Implement strict runtime boundaries for research/coder/ops specialists.

## Includes
- specialist input contract
- specialist output contract
- spawn wrapper
- announcement/result parsing
- malformed output rejection

## Files to add
- `runtime/specialists/contracts.ts`
- `runtime/specialists/spawn-specialist.ts`
- `runtime/specialists/announce-parser.ts`
- `runtime/specialists/research-runner.ts`
- `runtime/specialists/coder-runner.ts`
- `runtime/specialists/ops-runner.ts`

## Contracts
```ts
export type SpecialistTaskContract = {
  taskId: string
  goal: string
  specialistType: "research" | "coder" | "ops"
  context: {
    summary: string
    attachments?: string[]
    filePaths?: string[]
    urls?: string[]
  }
  constraints: {
    maxSeconds: number
    maxTokens: number
    maxToolCalls: number
    noFurtherDelegation: true
    outputMustBeJson: true
  }
  safety: {
    requireSnapshot: boolean
    rollbackMode: "file" | "workspace" | "none"
    stopOnRepeatedFailure: boolean
  }
  outputSchema: string
}

export type SpecialistResult = {
  status: "done" | "failed" | "tripped"
  summary: string
  findings?: string[]
  artifacts?: string[]
  filesChanged?: string[]
  actionsExecuted?: string[]
  risks: string[]
  rollbackAvailable: boolean
  rollbackMode: "file" | "workspace" | "none"
  tripReason?: "timeout" | "token_limit" | "tool_loop" | "unchanged_failure"
  recommendedNextMode?: "main_direct" | "workflow" | "human_decision"
}
```

## Required behavior
- specialists are one-shot only
- specialists must not plan globally
- specialists must not attempt nested delegation
- all outputs must validate against the result contract

## Acceptance criteria
- malformed specialist output is rejected and surfaced to main
- specialist wrapper supports preflight hooks
- result parsing is deterministic and auditable
