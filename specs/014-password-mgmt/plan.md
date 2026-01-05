# Plan: Password Management

## Goal
Implement secure password management features: allowing authenticated users to change their password and unauthenticated users to recover access via a "Found Password" flow (Email Reset).

## Proposed Changes

### 1. Application Layer (Service)
#### [MODIFY] [app/services/auth_service.py](file:///Users/ck/Project/Changsik/fastapi/app/services/auth_service.py)
- **New Method: `change_password(email, current_password, new_password)`**
    - Verify `current_password`.
    - Hash `new_password`.
    - Update User via Repository.
- **New Method: `reset_password(token, new_password)`**
    - Verify reset token (JWT).
    - Hash `new_password`.
    - Update User.
- **New Method: `create_password_reset_token(email)`**
    - Verify email exists.
    - Generate a short-lived JWT (e.g., 15 mins) specifically for reset.
    - **Mock Email Sending**: For now, just return the token or print it to console (SMTP is out of scope for this MVP).

### 2. Presentation Layer (API)
#### [MODIFY] [app/api/v1/auth.py](file:///Users/ck/Project/Changsik/fastapi/app/api/v1/auth.py)
- **POST `/password/change`**
    - Guard: `Depends(get_current_user)`
    - Body: `PasswordChangeRequest` (current_pw, new_pw)
- **POST `/password/recover`**
    - Guard: None (Public)
    - Body: `PasswordRecoverRequest` (email)
    - Response: Message ("If email exists, instruction sent.")
- **POST `/password/reset`**
    - Guard: None (Public)
    - Body: `PasswordResetRequest` (token, new_pw)

### 3. Domain Layer
#### [MODIFY] [app/domain/models/user.py](file:///Users/ck/Project/Changsik/fastapi/app/domain/models/user.py)
- Add DTOs:
    - `PasswordChangeRequest`
    - `PasswordRecoverRequest`
    - `PasswordResetRequest`

## Verification Plan
### Automated Tests
- `tests/contract/test_password_mgmt.py`
    - `test_change_password_success`: User can change password and log in with new one.
    - `test_change_password_wrong_current`: Fail 400.
    - `test_recover_password`: Request token (mocked).
    - `test_reset_password_success`: Use token to set new password.
    - `test_reset_password_invalid_token`: Fail 400.

## Decisions & Issues Log
| ID | Decision | Rationale | Status |
|----|----------|-----------|--------|
| **D-01** | **Dev-Only Token Exposure** | Frontend/Mobile 개발 편의를 위해 `/recover` API 응답에 `reset_token`을 임시 포함. (MVP 이후 제거 필) | **Applied** (Warning Commit) |
