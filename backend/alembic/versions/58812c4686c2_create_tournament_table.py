"""create tournament table

Revision ID: 58812c4686c2
Revises: 99e754a0653c
Create Date: 2025-04-04 14:52:13.773349

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "58812c4686c2"
down_revision: Union[str, None] = "99e754a0653c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tournament",
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("game_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["game_id"],
            ["game.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tournament")
    # ### end Alembic commands ###
