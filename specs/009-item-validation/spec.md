# Specification: Item Model Validation

## 1. Goal
Implement strict data validation for the `Item` domain using Pydantic V2 validators. This ensures that garbage data cannot enter the system via the API.

## 2. Background
Currently, the `Item` model relies on basic type hints. We need to enforce business rules like minimum length, forbidden words, and whitespace trimming.

## 3. Requirements

### 3.1. Field Validation
1.  **Name (`name`)**:
    - **Min Length**: 2 characters.
    - **Max Length**: 50 characters.
    - **Content**: Cannot be pure whitespace.
    - **Forbidden Words**: "admin", "root" (case-insensitive).
    - **Allowed Characters**: Alphanumeric (English/Korean) and spaces only (`^[a-zA-Z0-9가-힣 ]+$`). Special characters are forbidden.
    - **Trimming**: Automatically trim leading/trailing whitespace.

2.  **Description (`description`)**:
    - **Max Length**: 500 characters.
    - **Content**: Optional, but if provided, cannot be pure whitespace.

### 3.2. Models Affected
- `ItemCreate` (Input for POST)
- `ItemUpdate` (Input for PUT)
- `Item` (SQLModel table - should reflect max lengths in DB schema potentially, though Spec focus is on Pydantic)

## 4. User Stories
- As an API User, I expect a 422 Error if I receive an item with an empty name or a name that is too long.
- As a Product Owner, I want to prevent items named "admin" to avoid confusion.

## 5. Implementation Strategy
- Use `pydantic.field_validator` for custom logic (forbidden words).
- Use `Field(..., min_length=2, max_length=50)` for standard constraints.
