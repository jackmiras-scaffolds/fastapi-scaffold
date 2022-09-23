from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ItemAlias(BaseModel):
    id: int
    item_aggregator_id: str
    alias_aggregator_id: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        allow_mutation = False
