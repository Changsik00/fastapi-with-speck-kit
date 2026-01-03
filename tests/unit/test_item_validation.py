from app.domain.models.item import ItemCreate
import pytest
from pydantic import ValidationError

def test_item_create_valid():
    item = ItemCreate(name="Apple", description="A delicious red apple")
    assert item.name == "Apple"
    assert item.description == "A delicious red apple"

def test_item_create_valid_spaces():
    # Helper to check alphanumeric + spaces allowed
    item = ItemCreate(name="Red Car 123")
    assert item.name == "Red Car 123"

def test_item_create_valid_korean():
    item = ItemCreate(name="맛있는 사과")
    assert item.name == "맛있는 사과"

def test_item_create_trim_whitespace():
    item = ItemCreate(name="  Banana  ")
    assert item.name == "Banana"
    
def test_item_create_invalid_length_short():
    with pytest.raises(ValidationError) as exc:
        ItemCreate(name="A")
    assert "String should have at least 2 characters" in str(exc.value)

def test_item_create_invalid_length_long():
    long_name = "A" * 51
    with pytest.raises(ValidationError) as exc:
        ItemCreate(name=long_name)
    assert "String should have at most 50 characters" in str(exc.value)

def test_item_create_forbidden_word():
    with pytest.raises(ValidationError) as exc:
        ItemCreate(name="admin")
    assert "Name 'admin' is forbidden" in str(exc.value)

def test_item_create_special_chars():
    with pytest.raises(ValidationError) as exc:
        ItemCreate(name="Apple!")
    assert "Name must contain only alphanumeric characters(English/Korean) and spaces" in str(exc.value)

def test_description_empty_string_to_none():
    item = ItemCreate(name="Grape", description="   ")
    assert item.description is None
