"""create match model

Revision ID: 59027238546f
Revises: 58812c4686c2
Create Date: 2025-04-05 16:18:18.558609

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "59027238546f"
down_revision: Union[str, None] = "58812c4686c2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "match",
        sa.Column("tournament_id", sa.Integer(), nullable=False),
        sa.Column("first_team_id", sa.Integer(), nullable=True),
        sa.Column("second_team_id", sa.Integer(), nullable=True),
        sa.Column("score", sa.ARRAY(sa.Integer()), nullable=True),
        sa.Column("best_of", sa.SmallInteger(), nullable=False),
        sa.Column("date_start", sa.DateTime(), nullable=True),
        sa.Column("date_end", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.CheckConstraint("first_team_id != second_team_id", name="check_teams_not_equal"),
        sa.ForeignKeyConstraint(["first_team_id"], ["ea_team.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["second_team_id"], ["ea_team.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["tournament_id"], ["tournament.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("match")
