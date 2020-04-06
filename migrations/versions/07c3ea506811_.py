"""empty message

Revision ID: 07c3ea506811
Revises: ed990d1d55cf
Create Date: 2020-04-04 11:48:49.474588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07c3ea506811'
down_revision = 'ed990d1d55cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attended', sa.Boolean(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['class.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.drop_table('attendance')
    # ### end Alembic commands ###
