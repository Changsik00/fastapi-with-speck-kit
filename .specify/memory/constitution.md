# Constitution

The Constitution is a set of invariant rules and guidelines that the agent must follow at all times. It takes precedence over all other instructions.

## 1. Git Workflow
- **Branch Strategy**: modifications/experiments MUST be done on a separate branch.
- **Base Branch**: New feature branches (Spec) MUST be created from `main`.
- **Procedure**: `git checkout main` -> `git pull` -> `git checkout -b {number}-{short-description}`.
- **Commit Messages**: Semantic Commit Messages (e.g., `feat:`, `fix:`, `docs:`).

## 2. SDD (Spec-Driven Development) Workflow
The Agent MUST follow the 6-step cycle for every feature. Do NOT skip steps.

### Step 1: Specify (`speckit.specify`)
- **Goal**: Define WHAT to build.
- **Output**: `specs/{branch}/spec.md`
- **Content**: Summary, Requirements, User Stories.

### Step 2: Clarify (`speckit.clarify`)
- **Goal**: Clear up ambiguities.
- **Output**: `specs/{branch}/clarify.md` (or `research.md`)
- **Content**: Q&A, Edge cases, Constraints.

### Step 3: Plan (`speckit.plan`)
- **Goal**: Design HOW to build.
- **Output**: `specs/{branch}/plan.md`
- **Content**: Architecture, DB Schema, API Endpoints.

### Step 4: Tasks (`speckit.tasks`)
- **Goal**: Break down into actionable steps.
- **Output**: `specs/{branch}/tasks.md`
- **Content**: Detailed implementation checklist (TDD).

### Step 5: Analyze (`speckit.analyze`)
- **Goal**: Impact analysis.
- **Output**: `specs/{branch}/analysis.md`
- **Content**: Files to modify, Side effects, Migration needs.

### Step 6: Implement (`speckit.implement`)
- **Goal**: Write code & Test.
- **Action**: Execute `tasks.md`. Verify with tests.

## 3. Clean Architecture
- **Dependency Rule**: Source code dependencies can only point inwards.
- **Layers**:
  - `Entities` (Enterprise Business Rules)
  - `Use Cases` (Application Business Rules)
  - `Interface Adapters` (Controllers, Gateways, Presenters)
  - `Frameworks & Drivers` (Web, DB, Devices)

## 4. Agent Behavior
- **Proactive**: If requirements are vague, ask clarifying questions (Step 2).
- **Safe**: Always run tests before finishing a task.
- **Context**: Always check `.specify/memory` for project context.