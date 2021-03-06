"""empty message

Revision ID: 759effbf4ce1
Revises: 0ee9c04826b9
Create Date: 2020-04-04 04:23:48.093806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '759effbf4ce1'
down_revision = '0ee9c04826b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('institution', sa.Column('photo', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('institution', 'photo')
    # ### end Alembic commands ###
