"""empty message

Revision ID: 172bfdcbdaab
Revises: 0a9c615f85bd
Create Date: 2023-01-20 03:28:41.562231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '172bfdcbdaab'
down_revision = '0a9c615f85bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reg_starship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('starship_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['starship_id'], ['starship.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reg_starship')
    # ### end Alembic commands ###
