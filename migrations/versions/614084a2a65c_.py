"""empty message

Revision ID: 614084a2a65c
Revises: 9e97bb4a840d
Create Date: 2020-05-31 22:07:32.231917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '614084a2a65c'
down_revision = '9e97bb4a840d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###
