from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import backref, relationship

from configs.database import Base


class ItemAlias(Base):
    __tablename__ = "item_aliases"
    __table_args__ = (UniqueConstraint("alias_aggregator_id"),)

    id = Column(Integer, primary_key=True)
    alias_aggregator_id = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    item_aggregator_id = Column(
        String, ForeignKey("items.aggregator_id", ondelete="CASCADE")
    )

    item = relationship(
        "Item", backref=backref("aliases", lazy="dynamic", passive_deletes=True)
    )
