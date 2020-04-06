"""empty message

Revision ID: cb31b29ef8a9
Revises: dfc5fc665f9a
Create Date: 2020-04-05 13:22:02.823050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb31b29ef8a9'
down_revision = 'dfc5fc665f9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('photo', sa.String(length=250), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint(None, 'attendance', type_='foreignkey')
    op.create_foreign_key(None, 'attendance', 'class', ['class_id'], ['id'])
    op.alter_column('class', 'institution_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('class', 'institution_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint(None, 'attendance', type_='foreignkey')
    op.create_foreign_key(None, 'attendance', 'class', ['class_id'], ['id'], ondelete='CASCADE')
    op.drop_table('event')
    # ### end Alembic commands ###