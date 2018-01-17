"""Add profile picture name column

Revision ID: f6bb1eeb892d
Revises: f887fe8f2ea8
Create Date: 2018-01-17 16:45:39.321381

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f6bb1eeb892d'
down_revision = 'f887fe8f2ea8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profile_picture_name', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('profile_picture_url', sa.String(length=300), nullable=True))
    op.drop_column('user', 'profile_picture')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profile_picture', mysql.VARCHAR(length=300), nullable=True))
    op.drop_column('user', 'profile_picture_url')
    op.drop_column('user', 'profile_picture_name')
    # ### end Alembic commands ###