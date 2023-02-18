"""empty message

Revision ID: 5dd8627a1778
Revises: 8175d3f64e58
Create Date: 2023-02-18 11:53:55.714003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dd8627a1778'
down_revision = '8175d3f64e58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('diametro', sa.String(length=250), nullable=False),
    sa.Column('periodo_orbital', sa.String(length=250), nullable=False),
    sa.Column('poblacion', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planetas')
    # ### end Alembic commands ###
