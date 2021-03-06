"""empty message

Revision ID: c572dd53ed7c
Revises: 07c3ea506811
Create Date: 2020-04-04 12:23:33.364294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c572dd53ed7c'
down_revision = '07c3ea506811'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('class', 'institution_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'grade', type_='foreignkey')
    op.create_foreign_key(None, 'grade', 'class', ['class_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'grade', type_='foreignkey')
    op.create_foreign_key(None, 'grade', 'class', ['class_id'], ['id'])
    op.alter_column('class', 'institution_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
