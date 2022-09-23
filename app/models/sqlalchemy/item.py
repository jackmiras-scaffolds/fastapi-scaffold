from sqlalchemy import Column, DateTime, Float, Integer, String, UniqueConstraint

from configs.database import Base


class Item(Base):
    __tablename__ = "items"
    __table_args__ = (
        UniqueConstraint("inventory_id"),
        UniqueConstraint("aggregator_id"),
    )

    id = Column(Integer, primary_key=True)
    ncm = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    subtype = Column(String, nullable=True)
    item_type = Column(String, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    name = Column(String, index=True, nullable=False)
    inventory_id = Column(String, nullable=False, unique=True)
    aggregator_id = Column(String, index=True, nullable=False, unique=True)
