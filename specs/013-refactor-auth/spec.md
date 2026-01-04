# Spec: Refactor Auth to Clean Architecture

## 1. Background
The current authentication implementation (`auth`) diverges from the project's established Clean Architecture pattern (`items` module).
- **Inconsistency**: `items` uses a flat structure (`api/v1/items.py`), while `auth` uses a nested structure (`api/v1/endpoints/auth.py`).
- **Fat Controller**: The `auth` controller contains business logic (password verification, token creation) that should reside in the Service layer.

## 2. Requirements

### A. Structural Consistency
- **Constraint**: Move `app/api/v1/endpoints/auth.py` to `app/api/v1/auth.py`.
- **Cleanup**: Remove the `endpoints` directory if empty.

### B. Separation of Concerns (Logic)
- **Constraint**: The Controller (`auth.py`) MUST NOT import `UserRepository` or `Core Config` (settings) directly for logic.
- **Constraint**: The `AuthService` MUST implement high-level business methods:
    - `login(form_data)` -> Returns Token or None.
    - `signup(user_create)` -> Returns User.
- **Goal**: The Controller should be "Thin", only handling HTTP Request/Response translation.

## 3. Scope
- **In Scope**: `app/api/v1/endpoints/auth.py`, `app/services/auth_service.py`, `app/main.py`.
- **Out of Scope**: Changing the database schema or authentication behavior (Tests must pass as is).
