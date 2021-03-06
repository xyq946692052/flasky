"""initial migration

Revision ID: 0742166942a1
Revises: 
Create Date: 2016-12-08 16:01:45.142813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0742166942a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    # ### end Alembic commands ###
