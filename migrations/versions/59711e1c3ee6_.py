"""empty message

Revision ID: 59711e1c3ee6
Revises: 832021fc72b8
Create Date: 2022-04-11 15:03:04.056705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59711e1c3ee6'
down_revision = '832021fc72b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('brewery_posts', sa.Column('beer', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('brewery_posts', 'beer')
    # ### end Alembic commands ###
