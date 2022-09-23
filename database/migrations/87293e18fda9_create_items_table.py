"""create_items_table

Revision ID: 87293e18fda9
Revises:
Create Date: 2020-07-28 15:57:01.374873

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "87293e18fda9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("inventory_id", sa.String(), nullable=False),
        sa.Column("aggregator_id", sa.String(), nullable=False),
        sa.Column("item_type", sa.String(), nullable=True),
        sa.Column("subtype", sa.String(), nullable=True),
        sa.Column("ncm", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("aggregator_id"),
        sa.UniqueConstraint("inventory_id"),
    )


def downgrade():
    op.drop_table("items")
