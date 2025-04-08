"""create game_id field

Revision ID: a15b720467be
Revises: 1d8146ca53f1
Create Date: 2025-04-08 19:05:09.914140

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a15b720467be"
down_revision: Union[str, None] = "1d8146ca53f1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("match", sa.Column("game_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "fk_match_game_id",
        "match",
        "game",
        ["game_id"],
        ["id"],
        ondelete="CASCADE"
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_match_game_id", "match", type_="foreignkey")
    op.drop_column("match", "game_id")
