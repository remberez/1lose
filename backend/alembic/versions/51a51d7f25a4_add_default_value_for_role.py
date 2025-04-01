"""add default value for role

Revision ID: 51a51d7f25a4
Revises: 9387aff5557d
Create Date: 2025-04-01 19:35:53.210743

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision: str = "51a51d7f25a4"
down_revision: Union[str, None] = "9387aff5557d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "user",
        "role_code",
        server_default="user",
    )


def downgrade() -> None:
    op.alter_column(
        "user",
        "role_code",
        server_default=text("NULL"),
    )
