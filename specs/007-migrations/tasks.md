# Tasks: Database Migrations with Alembic

## 1. Dependencies & Setup
- [ ] Add `alembic` to `requirements.txt`
- [ ] Install dependencies (`uv pip install -r requirements.txt`)
- [ ] Initialize Alembic with async template (`uv run alembic init -t async alembic`)

## 2. Configuration
- [ ] Configure `alembic/env.py`:
    - [ ] Import `app.core.config.settings` for `DATABASE_URL`
    - [ ] Import `app.domain.models` (Item)
    - [ ] Import `sqlmodel.SQLModel`
    - [ ] Set `target_metadata = SQLModel.metadata`
    - [ ] Update `run_migrations_online` to use `settings.DATABASE_URL` and `async_engine`
- [ ] Configure `alembic.ini`:
    - [ ] Ensure script location is correct (usually default is fine)

## 3. Application Updates
- [ ] Refactor `app/main.py`:
    - [ ] Remove `lifespan` function (or remove just the `create_all` part)
    - [ ] Remove `asynccontextmanager` import if unused

## 4. Execution & Verification
- [ ] Generate initial migration (`uv run alembic revision --autogenerate -m "Initial migration"`)
- [ ] Review generated migration script (verify `Item` table creation)
- [ ] Apply migration (`uv run alembic upgrade head`)
- [ ] Verify database state (Manual check or running app)
