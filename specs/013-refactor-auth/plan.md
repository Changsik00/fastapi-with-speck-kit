# Plan: Refactor Auth to Clean Architecture

## Goal
Align the Authentication module (`auth`) with the project's existing Clean Architecture pattern (`items`), focusing on consistency and separation of concerns.

## Diagnosis (Why this happened?)
1.  **Structure Divergence**: The existing `items` implementation resides in `app/api/v1/items.py` (Flat Structure). I introduced `app/api/v1/endpoints/auth.py` (Nested Structure), creating inconsistency.
2.  **Logic Leakage**: The `items` controller delegates purely to `ItemService`. My `auth` controller performs business logic (password verification, user existence checks, token creation) directly, violating the "Thin Controller" principle.

## Proposed Changes

### 1. Application Layer (Service Improvement)
#### [MODIFY] [app/services/auth_service.py](file:///Users/ck/Project/Changsik/fastapi/app/services/auth_service.py)
- **Implement `login(email, password)`**: Handles repo lookup, password verification, and token generation. Returns Token or raises Error.
- **Implement `signup(user_create)`**: Handles repo lookup (check existence), hashing, and creation. Returns User or raises Error.
- **Remove** low-level helper exposure (`verify_password`, `get_password_hash`) if they are only used internally by these high-level methods.

### 2. Presentation Layer (Structure & Controller)
#### [MOVE & MODIFY] `app/api/v1/endpoints/auth.py` -> `app/api/v1/auth.py`
- Align file location with `items.py`.
- **Refactor**: Remove `UserRepository` dependency from Controller. Only inject `AuthService`.
- **Delegate**: Call `await auth_service.login(...)` and `await auth_service.signup(...)`.

#### [DELETE] `app/api/v1/endpoints/`
- Remove the implementation drift.

#### [MODIFY] [app/main.py](file:///Users/ck/Project/Changsik/fastapi/app/main.py)
- Update import path for `auth_router`.

## Verification
- **Automated Tests**: Existing tests (`tests/contract/test_auth.py`) MUST pass without modification (Refactoring should not change behavior).
