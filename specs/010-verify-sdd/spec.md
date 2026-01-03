# Specification: Verify SDD Workflow & Documentation

## 1. Background
The project has recently adopted a strict Specification Driven Development (SDD) process and updated the `agent.md` with new operational modes ("Strict" vs "FF"). We need to verify that these rules are practical and that our documentation (`spec`, `plan`, `README`) accurately reflects this reality.

## 2. Requirements
- **Verify SDD Artifacts**: Ensure that creating `spec.md` and `plan.md` manually (or via tool if available) provides a useful blueprint for development.
- **Verify Constitution**: Check if `constitution.md` rules (e.g., Git workflow, Clean Architecture) are actually being followed.
- **Update Documentation**: Ensure `README.md` clearly mentions the `agent.md` protocol so new contributors (and agents) know how to work.

## 3. User Stories
- As a **Developer**, I want to see if the "Spec -> Plan" flow helps clarify the task before coding.
- As a **User**, I want the `README.md` to point me to `agent.md` and `constitution.md` so I understand the project rules.

## 4. Constraints
- Must follow the "Strict Mode" manually since `spec-kit` CLI is missing.
