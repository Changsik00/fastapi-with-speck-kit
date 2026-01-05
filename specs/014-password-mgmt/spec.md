# Spec: Password Management

## 1. Background
Users need a way to manage their credentials securely. This includes changing their password while logged in and recovering access if they forget their password.

## 2. Requirements

### A. Change Password (Authenticated)
- **Goal**: Allow a logged-in user to change their password.
- **Endpoint**: `POST /api/v1/auth/password/change`
- **Security**: Requires Bearer Token.
- **Input**:
    - `current_password`: To verify identity.
    - `new_password`: The new credential.
- **Logic**:
    1. Verify `current_password` matches the stored hash. (If not match -> 400).
    2. Preventing reuse of recent passwords is NOT required for MVP.
    3. Update user's `hashed_password` with `new_password`.

### B. Reset Password (Unauthenticated / Recovery)
- **Goal**: Allow users to regain access if they forget their password.
- **Flow**:
    1. **Request Recovery**: `POST /api/v1/auth/password/recover`
        - Input: `email`
        - Action: Check if user exists. If yes, generate a **password reset token** (JWT or random string) and "send" it via email.
        - *Note*: Use "Mock Email Service" for now (print to log) until SMTP is configured.
    2. **Reset Password**: `POST /api/v1/auth/password/reset`
        - Input: `token`, `new_password`
        - Action: Verify token validity and expiration. Update password. Invalidate token (optional, or rely on short expiry).

## 3. Scope
- **In Scope**: `AuthService`, `auth.py` (Controller), `User` model (if token storage needed, though JWT is stateless).
- **Out of Scope**: SMTP Server Setup (Mocking for now).
