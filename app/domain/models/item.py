import re
from typing import Optional
from pydantic import field_validator
from sqlmodel import Field, SQLModel

class ItemBase(SQLModel):
    name: str = Field(min_length=2, max_length=50)
    description: Optional[str] = Field(default=None, max_length=500)

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Name cannot be empty or whitespace only")
        
        forbidden_words = ["admin", "root"]
        if v.lower() in forbidden_words:
            raise ValueError(f"Name '{v}' is forbidden")
            
        # Alphanumeric (English/Korean) and spaces only
        # Range 가-힣 covers standard Korean syllables.
        if not re.match(r"^[a-zA-Z0-9가-힣 ]+$", v):
            raise ValueError("Name must contain only alphanumeric characters(English/Korean) and spaces")
            
        return v

    @field_validator("description")
    @classmethod
    def validate_description(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        if not v:
            return None # Convert empty string desc to None
        return v

class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ItemCreate(ItemBase):
    pass
