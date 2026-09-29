from pydantic import BaseModel, Field
from datetime import date


class LostItemCreate(BaseModel):
    item_name: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=5)
    category: str = Field(min_length=2, max_length=50)
    location: str = Field(min_length=2, max_length=150)
    date_lost: date


class LostItemUpdate(BaseModel):
    item_name: str | None = Field(
        default=None, min_length=2, max_length=100
    )
    description: str | None = Field(default=None, min_length=5)
    category: str | None = Field(
        default=None, min_length=2, max_length=50
    )
    location: str | None = Field(
        default=None, min_length=2, max_length=150
    )
    date_lost: date | None = None


class LostItemResponse(LostItemCreate):
    id: int

    model_config = {"from_attributes": True}