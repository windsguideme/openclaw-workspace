# TASK-05 Workflows, Skills, and Telemetry

## Scope
Implement the typed workflow layer, progressive skill loading, and telemetry needed for later skill evolution.

## Includes
- workflow step contract
- workflow definition contract
- workflow engine
- first workflow implementation
- skill catalog loader
- guide/resource loader
- execution telemetry
- skill observation recorder
- offline skill patch proposal generator

## Files to add
- `runtime/workflows/engine.ts`
- `runtime/workflows/schemas.ts`
- `runtime/workflows/gather-normalize-evaluate-compose.ts`
- `runtime/workflows/registry.ts`
- `runtime/telemetry/execution-log.ts`
- `runtime/telemetry/route-metrics.ts`
- `runtime/telemetry/failure-patterns.ts`
- `runtime/telemetry/skill-observer.ts`

## Contracts
```ts
export type WorkflowStep = {
  id: string
  kind: "tool" | "llm_json"
  name: string
  run: (ctx: WorkflowContext) => Promise<void>
  retryable?: boolean
}

export type WorkflowDefinition = {
  id: string
  description: string
  appliesWhen: (frame: TaskFrame) => boolean
  budget: RuntimeBudget
  steps: WorkflowStep[]
}

export type SkillObservation = {
  skillId: string
  taskId: string
  route: "direct" | "workflow" | "specialist"
  success: boolean
  addedSteps?: string[]
  skippedSteps?: string[]
  failureStage?: string
  humanCorrection?: string
}
```

## Skill loading requirements
- level 1: catalog metadata
- level 2: operational guide
- level 3: resources loaded on demand

## Required behavior
- workflows run under shared runtime guardrails
- no automatic skill write-back in this phase
- skill patch proposal generation is offline-only

## Acceptance criteria
- first workflow can execute typed stages in order
- skill loader supports progressive loading
- telemetry captures route and failure data for future tuning
