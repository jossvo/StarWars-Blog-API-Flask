"""empty message

Revision ID: 83d4c90600e4
Revises: 016e8ca75169
Create Date: 2023-01-20 17:33:43.800463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83d4c90600e4'
down_revision = '016e8ca75169'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('starship', schema=None) as batch_op:
        batch_op.alter_column('crew',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=120),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('starship', schema=None) as batch_op:
        batch_op.alter_column('crew',
               existing_type=sa.String(length=120),
               type_=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
