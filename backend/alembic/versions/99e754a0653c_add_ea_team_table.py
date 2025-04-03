"""add ea_team table

Revision ID: 99e754a0653c
Revises: ce64368294bb
Create Date: 2025-04-03 20:34:56.798316

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "99e754a0653c"
down_revision: Union[str, None] = "ce64368294bb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "ea_team",
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column("game_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["game_id"],
            ["game.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("ea_team")
