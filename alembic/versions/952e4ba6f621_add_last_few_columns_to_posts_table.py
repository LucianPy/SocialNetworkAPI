"""add last few columns to posts table

Revision ID: 952e4ba6f621
Revises: 861ea4de7a94
Create Date: 2021-11-09 16:08:36.866357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '952e4ba6f621'
down_revision = '861ea4de7a94'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass