# Tasks: Item Model Validation

- [ ] **1. Implement Validators** <!-- id: 1 -->
    - Update `app/domain/models/item.py`.
    - Add `min_length`, `max_length` to `name`.
    - Add `field_validator` for forbidden words and regex (`^[a-zA-Z0-9 ]+$`).

- [ ] **2. Create Unit Tests** <!-- id: 2 -->
    - Create `tests/unit/test_item_validation.py`.
    - Test valid cases.
    - Test invalid cases (length, forbidden words, special chars).

- [ ] **3. Verify** <!-- id: 3 -->
    - Run `pytest tests/unit/test_item_validation.py`.
