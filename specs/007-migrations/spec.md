# Specification: Database Migrations with Alembic

## 1. Goal
Implement a robust database migration system using **Alembic** to manage schema changes over time.

## 2. Background
Currently, `app/main.py` uses `SQLModel.metadata.create_all` on startup. We need proper version control for the DB schema.

## 3. Requirements
1.  **Initialize Alembic**: Setup `alembic/` directory and `alembic.ini`.
2.  **Async Support**: Configure `env.py` for `asyncpg`.
3.  **Auto-generation**: Enable `SQLModel` metadata integration.
4.  **Cleanup**: Remove `create_all` from `main.py`.

## 4. User Stories
- Developer runs `alembic revision --autogenerate` to create migrations.
- Developer runs `alembic upgrade head` to apply changes.
