"""add review

Revision ID: b08bd2d3dc13
Revises: fe06dc22a66d
Create Date: 2024-10-04 13:52:27.848458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b08bd2d3dc13'
down_revision = 'fe06dc22a66d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_reviews_customer_id_customers')),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], name=op.f('fk_reviews_item_id_items')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###