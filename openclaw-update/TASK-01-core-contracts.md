# TASK-01 Core Contracts and Config Scaffolding

## Scope
Implement the minimum contracts and configuration scaffolding required to move OpenClaw toward the v1.1 architecture.

## Includes
- configuration folder scaffolding
- agent config stubs
- policy config stubs
- `TaskFrame`
- `CompiledPlan`
- route selection contract

## Do not do yet
- real spawn execution
- rollback implementation
- workflow engine
- telemetry

## Files to add
- `config/openclaw.json5`
- `config/models.json`
- `config/agents/*.json`
- `config/policies/*.json`
- `runtime/orchestrator/task-framer.ts`
- `runtime/orchestrator/plan-compiler.ts`
- `runtime/orchestrator/route-selector.ts`

## Contract targets

### TaskFrame
```ts
export type TaskFrame = {
  goal: string
  domain: "general" | "research" | "coding" | "ops"
  needsWeb: boolean
  needsFsWrite: boolean
  needsExec: boolean
  needsIsolation: boolean
  needsLongRun: boolean
  estimatedComplexity: "low" | "medium" | "high"
  risk: "low" | "medium" | "high"
}
```

### CompiledPlan
```ts
export type ExecutionMode = "direct" | "json_step" | "workflow" | "specialist"

export type CompiledPlan = {
  goal: string
  mode: ExecutionMode
  specialistType?: "research" | "coder" | "ops"
  steps: Array<{
    id: string
    kind: "tool" | "llm_json" | "workflow_step" | "specialist"
    name: string
    input: Record<string, unknown>
    outputSchema?: string
    budget?: {
      maxToolCalls?: number
      maxTokens?: number
      maxSeconds?: number
    }
  }>
  budget: {
    maxTokens: number
    maxSeconds: number
    maxToolCalls: number
  }
}
```

## Acceptance criteria
- contracts compile cleanly
- config files are syntactically valid
- route selector returns one of the 4 execution modes
- no nested specialist logic is introduced
