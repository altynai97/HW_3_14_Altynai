"""empty message

Revision ID: 7e992fec0fb6
Revises: 
Create Date: 2023-04-05 17:17:39.748285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e992fec0fb6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('period', sa.String(length=40), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=40), nullable=True),
    sa.Column('unit', sa.String(length=40), nullable=True),
    sa.Column('subject', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('transactions')
    # ### end Alembic commands ###
