"""create_item_aliases_table

Revision ID: d3da97611e80
Revises: c22d370d16d7
Create Date: 2020-08-02 16:39:18.937253

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d3da97611e80"
down_revision = "87293e18fda9"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "item_aliases",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("item_aggregator_id", sa.String(), nullable=True),
        sa.Column("alias_aggregator_id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True, default=None),
        sa.ForeignKeyConstraint(
            ["item_aggregator_id"], ["items.aggregator_id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("alias_aggregator_id"),
    )


def downgrade():
    op.drop_table("item_aggregator_id_aliases")
