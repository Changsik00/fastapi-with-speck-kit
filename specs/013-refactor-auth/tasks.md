# Tasks: Refactor Auth to Clean Architecture

- [x] **Design & Approval** (Done) <!-- id: 1 -->
    - [x] Create Branch `013-refactor-auth` <!-- id: 2 -->
    - [x] Draft `spec.md` <!-- id: 3 -->
    - [x] Draft `plan.md` <!-- id: 4 -->
    - [x] Approve SDD Documents <!-- id: 5 -->

- [ ] **Implementation** (Done) <!-- id: 6 -->
    - [x] **Service Layer**: Update `AuthService` with `login` and `signup` methods <!-- id: 7 -->
    - [x] **Presentation Layer**: Move `endpoints/auth.py` to `api/v1/auth.py` <!-- id: 8 -->
    - [x] **Refactoring**: Rewrite Controller to use Service methods only <!-- id: 9 -->
    - [x] **Cleanup**: Update `main.py` imports and remove old folder <!-- id: 10 -->

- [x] **Verification** (Done) <!-- id: 11 -->
    - [x] Verify Import Structure (Check for `UserRepository` in Controller) <!-- id: 12 -->
    - [x] Run Tests (`uv run pytest tests/contract/test_auth.py`) <!-- id: 13 -->
