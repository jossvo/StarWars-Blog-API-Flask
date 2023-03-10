"""empty message

Revision ID: 0a9c615f85bd
Revises: 6b5128a5a6db
Create Date: 2023-01-20 03:21:54.040096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a9c615f85bd'
down_revision = '6b5128a5a6db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('specie_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'specie', ['specie_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('specie_id')

    # ### end Alembic commands ###
