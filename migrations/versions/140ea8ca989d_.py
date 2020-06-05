"""empty message

Revision ID: 140ea8ca989d
Revises: 614084a2a65c
Create Date: 2020-05-31 22:32:05.073048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '140ea8ca989d'
down_revision = '614084a2a65c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
