# Specification: Configuration Management

## 1. Goal
Externalize application configuration to environment variables using `pydantic-settings` to improve security, flexibility, and adherence to 12-factor app principles.

## 2. Background
Currently, configuration values like `PROJECT_NAME`, `API_V1_STR` (if any), and potential DB URLs are hardcoded or scattered. We need a centralized, type-safe way to manage these.

## 3. Requirements

### Functional Requirements
- **Centralized Config**: Create `app/core/config.py` to hold all application settings.
- **Environment Variables**: Values must be readable from system environment variables and a `.env` file.
- **Type Safety**: Use `pydantic.BaseSettings` for validation/type-hinting.
- **Default Values**: Provide sensible defaults for development (e.g., `MODE=dev`).

### Non-Functional Requirements
- **Security**: Secrets (like API keys, DB passwords) must NOT be committed to version control.
- **DX**: `git clone` -> `uv run` should work out-of-the-box (with defaults) or fail gracefully if `.env` is missing critical values.

## 4. User Stories
- **Developer**: I want to change the database URL by editing a `.env` file without touching the code.
- **Developer**: I want my IDE to autocomplete configuration settings (e.g., `settings.PROJECT_NAME`).
- **Ops**: I want to inject secrets via environment variables in production (Docker/K8s).

## 5. Mockups / Interface
```python
# Usage Example
from app.core.config import settings

print(settings.PROJECT_NAME)
```
