"""create event, outcame tables

Revision ID: 8524140394dc
Revises: 23f92e758cf1
Create Date: 2025-04-07 15:58:40.293082

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8524140394dc"
down_revision: Union[str, None] = "23f92e758cf1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "outcome",
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column("coefficient", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "event",
        sa.Column("match_id", sa.Integer(), nullable=False),
        sa.Column("map_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column("first_outcome_id", sa.Integer(), nullable=True),
        sa.Column("second_outcome_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("updated_by", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["first_outcome_id"],
            ["outcome.id"],
        ),
        sa.ForeignKeyConstraint(["map_id"], ["map.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["match_id"], ["match.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["second_outcome_id"],
            ["outcome.id"],
        ),
        sa.ForeignKeyConstraint(
            ["updated_by"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("event")
    op.drop_table("outcome")
