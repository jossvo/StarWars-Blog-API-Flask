"""empty message

Revision ID: 88dae1588b3f
Revises: 8838ad350b87
Create Date: 2023-01-20 15:57:03.890409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88dae1588b3f'
down_revision = '8838ad350b87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.alter_column('opening_crawl',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.String(length=600),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.alter_column('opening_crawl',
               existing_type=sa.String(length=600),
               type_=sa.VARCHAR(length=300),
               existing_nullable=False)

    # ### end Alembic commands ###