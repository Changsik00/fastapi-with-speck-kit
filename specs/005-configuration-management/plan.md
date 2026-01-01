# Plan: Configuration Management

## 1. Architecture
We will use the **Configuration Object Pattern**. A singleton instance of `pydantic_settings.BaseSettings` will be created in `app/core/config.py` and imported wherever configuration is needed.

### Components
- **`app/core/config.py`**: Defines the schema and loads the config.
- **`.env`**: Local secret storage (git-ignored).
- **`app/main.py`**: Consumer of the config.

## 2. Dependencies
- `pydantic-settings`: Official Pydantic library for settings management.

## 3. Data Schema (`Settings`)

| Field | Type | Default | Description |
|---|---|---|---|
| `PROJECT_NAME` | `str` | `"FastAPI Clean Architecture"` | The name of the API. |
| `API_V1_STR` | `str` | `"/api/v1"` | The prefix for V1 API routes. |
| `MODE` | `Literal['dev', 'prod', 'test']` | `"dev"` | Operational mode. |

## 4. Implementation Steps

### 1. Setup
- Add `pydantic-settings` to `requirements.txt`.
- Add `.env` to `.gitignore` (if not present).
- Create a template `.env.example` for documentation.

### 2. Core Implementation
- Create `app/core/config.py`.
- Implement `Settings` class with `env_file=".env"`.
- Instantiate `settings = Settings()`.

### 3. Refactoring
- **`app/main.py`**: Replace hardcoded title with `settings.PROJECT_NAME`.

## 5. Verification
- **Automated**: Create a test case that overrides environment variables and asserts `settings` values change.
- **Manual**: Run the server and check the OpenAPI docs title.
