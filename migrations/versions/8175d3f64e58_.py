"""empty message

Revision ID: 8175d3f64e58
Revises: a0fb404bcbc3
Create Date: 2023-02-18 11:45:11.120410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8175d3f64e58'
down_revision = 'a0fb404bcbc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personajes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('altura', sa.String(length=250), nullable=False),
    sa.Column('genero', sa.String(length=250), nullable=False),
    sa.Column('peso', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('personajes')
    # ### end Alembic commands ###
