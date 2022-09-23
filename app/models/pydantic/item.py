from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    ncm: str
    name: str
    price: float
    subtype: str
    item_type: str
    inventory_id: str
    aggregator_id: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        allow_mutation = False
