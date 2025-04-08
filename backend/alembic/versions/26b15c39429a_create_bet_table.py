"""create bet table

Revision ID: 26b15c39429a
Revises: 8524140394dc
Create Date: 2025-04-08 10:38:41.754566

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "26b15c39429a"
down_revision: Union[str, None] = "8524140394dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "bet",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Numeric(precision=12, scale=2), nullable=False),
        sa.Column("coefficient", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("possible_gain", sa.Numeric(precision=12, scale=2), nullable=False),
        sa.Column(
            "bet_status",
            sa.Enum("ACTIVE", "WON", "LOST", "SOLD", "CANCELED", name="betstatus"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["event_id"], ["event.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("bet")
