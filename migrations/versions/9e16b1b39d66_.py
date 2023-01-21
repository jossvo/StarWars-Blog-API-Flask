"""empty message

Revision ID: 9e16b1b39d66
Revises: 6b20fbc17485
Create Date: 2023-01-21 03:17:05.965720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e16b1b39d66'
down_revision = '6b20fbc17485'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('specie', schema=None) as batch_op:
        batch_op.drop_constraint('specie_homeworld_by_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'planet', ['homeworld_by_id'], ['id'], ondelete='cascade')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('specie', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('specie_homeworld_by_id_fkey', 'planet', ['homeworld_by_id'], ['id'])

    # ### end Alembic commands ###
