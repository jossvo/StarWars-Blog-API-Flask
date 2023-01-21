"""empty message

Revision ID: 6b20fbc17485
Revises: 537b831ed408
Create Date: 2023-01-21 03:16:22.151446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b20fbc17485'
down_revision = '537b831ed408'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.drop_constraint('location_film_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('location_planet_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'planet', ['planet_id'], ['id'], ondelete='cascade')
        batch_op.create_foreign_key(None, 'film', ['film_id'], ['id'], ondelete='cascade')

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint('people_homeworld_by_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'planet', ['homeworld_by_id'], ['id'], ondelete='cascade')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('people_homeworld_by_id_fkey', 'planet', ['homeworld_by_id'], ['id'])

    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('location_planet_id_fkey', 'planet', ['planet_id'], ['id'])
        batch_op.create_foreign_key('location_film_id_fkey', 'film', ['film_id'], ['id'])

    # ### end Alembic commands ###