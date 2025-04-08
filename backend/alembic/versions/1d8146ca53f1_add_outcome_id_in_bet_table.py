"""add outcome_id in bet table

Revision ID: 1d8146ca53f1
Revises: 26b15c39429a
Create Date: 2025-04-08 13:21:44.267583

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1d8146ca53f1"
down_revision: Union[str, None] = "26b15c39429a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("bet", sa.Column("outcome_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "fk_bet_outcome_id",
        "bet",
        "outcome",
        ["outcome_id"],
        ["id"],
        ondelete="CASCADE"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_bet_outcome_id", "bet", type_="foreignkey")
    op.drop_column("bet", "outcome_id")
