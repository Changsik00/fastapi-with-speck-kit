# Tasks: Configuration Management

- [ ] **Dependency**: Install `pydantic-settings` <!-- id: 1 -->
    - [ ] Add to `requirements.txt`
    - [ ] Run `uv pip install -r requirements.txt` (or equivalent)
- [ ] **Environment**: Setup local environment <!-- id: 2 -->
    - [ ] Add `.env` to `.gitignore`
    - [ ] Create `.env` file with `PROJECT_NAME="FastAPI Clean Ops"`, `MODE=dev`
    - [ ] Create `.env.example` for reference
- [ ] **Core**: Implement Settings <!-- id: 3 -->
    - [ ] Create `app/core/config.py`
    - [ ] Define `Settings` class with `env_file=".env"`
    - [ ] Add fields: `PROJECT_NAME`, `API_V1_STR`, `MODE`
- [ ] **Refactor**: Use Settings in Application <!-- id: 4 -->
    - [ ] Modify `app/main.py` to import `settings`
    - [ ] Replace string literals with `settings.PROJECT_NAME`
- [ ] **Verify**: Test changes <!-- id: 5 -->
    - [ ] Run server (`uv run uvicorn ...`) and check `/docs` title
    - [ ] Verify `.env` values override defaults
