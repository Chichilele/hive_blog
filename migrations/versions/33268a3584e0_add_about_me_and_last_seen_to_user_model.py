"""add about_me and last_seen to user model

Revision ID: 33268a3584e0
Revises: 529d8d050b5a
Create Date: 2021-07-27 16:22:20.206788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33268a3584e0'
down_revision = '529d8d050b5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
