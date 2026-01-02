# Plan: Database Migrations with Alembic

## 1. Architecture
- **Tool**: Alembic (Standard Python migration tool).
- **Integration point**: `app/core/config.py` (for DB URL) and `app/domain/models` (for SQLModel metadata).
- **Directory**: `/alembic` (root level) to store migration scripts.

## 2. Dependencies
- `alembic`: Needs to be added to `requirements.txt`.

## 3. Implementation Steps
1.  **Install**: Add `alembic` to `requirements.txt` and install.
2.  **Initialize**: Run `alembic init -t async alembic` to create async-compatible structure.
3.  **Configure `alembic.ini`**: Remove hardcoded URL, prep for env var usage (or handled in `env.py`).
4.  **Configure `alembic/env.py`**:
    - Import `settings` from `app.core.config`.
    - Import `SQLModel` and domain models (e.g. `Item`).
    - Set `target_metadata = SQLModel.metadata`.
    - Configure `run_migrations_online` to use `async_engine` from our code or create one using `DATABASE_URL`.
5.  **Refactor Main**: Remove `lifespan` context manager from `app/main.py` (stop auto-creating tables).
6.  **First Migration**: Run `alembic revision --autogenerate -m "Initial migration"`.
7.  **Apply**: Run `alembic upgrade head`.

## 4. Verification
- **Test**: Run `pytest` (It uses in-memory SQLite, so it should NOT be affected by Alembic unless we update `conftest.py` to run migrations, but `create_all` is safer/faster for tests. We will keep `create_all` in `conftest.py`).
- **Manual**: Check if `alembic_version` table exists in Supabase. Verify `Item` table persists.
