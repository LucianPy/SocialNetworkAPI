"""add content column to posts table

Revision ID: 91cb2249acb0
Revises: fb4cf085c05f
Create Date: 2021-11-09 15:47:18.139555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91cb2249acb0'
down_revision = 'fb4cf085c05f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_column('posts', 'content')
    pass
