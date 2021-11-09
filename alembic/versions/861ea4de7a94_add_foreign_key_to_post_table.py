"""add foreign-key to post table

Revision ID: 861ea4de7a94
Revises: df8b4f566be9
Create Date: 2021-11-09 15:57:48.312493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '861ea4de7a94'
down_revision = 'df8b4f566be9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", 
                                            referent_table="users", 
                                            local_cols=['owner_id'], 
                                            remote_cols=['id'], 
                                            ondelete="CASCADE")

def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    
