"""add registered column on user table

Revision ID: ce90a2c8c6c1
Revises: 9ae2be9ea047
Create Date: 2018-01-11 20:49:40.847922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce90a2c8c6c1'
down_revision = '9ae2be9ea047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('registered_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'registered_on')
    # ### end Alembic commands ###