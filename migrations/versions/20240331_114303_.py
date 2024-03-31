"""empty message

Revision ID: 1495a7877607
Revises: 9c8bbf691798
Create Date: 2024-03-31 11:43:03.760653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1495a7877607'
down_revision = '9c8bbf691798'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=130), nullable=True),
    sa.Column('file_one', sa.String(), nullable=True),
    sa.Column('file_two', sa.String(), nullable=True),
    sa.Column('file_three', sa.String(), nullable=True),
    sa.Column('file_four', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
