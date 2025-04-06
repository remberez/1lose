"""create map table

Revision ID: 23f92e758cf1
Revises: 370c954b5cd3
Create Date: 2025-04-06 22:08:32.707801

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "23f92e758cf1"
down_revision: Union[str, None] = "370c954b5cd3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "map",
        sa.Column("match_id", sa.Integer(), nullable=False),
        sa.Column("score", sa.ARRAY(sa.Integer()), nullable=False),
        sa.Column("winner_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["match_id"], ["match.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["winner_id"], ["ea_team.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("map")
