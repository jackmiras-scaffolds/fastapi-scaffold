"""create_users_table

Revision ID: 4247a644dc14
Revises: d3da97611e80
Create Date: 2023-06-28 17:23:08.909027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4247a644dc14'
down_revision = 'd3da97611e80'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
