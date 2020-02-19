"""empty message

Revision ID: c0a943f09e36
Revises: d5730252ea3a
Create Date: 2020-02-19 16:56:29.909982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0a943f09e36'
down_revision = 'd5730252ea3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('pubdate', sa.String(length=10), nullable=True))
    op.create_index(op.f('ix_blog_post_pubdate'), 'blog_post', ['pubdate'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blog_post_pubdate'), table_name='blog_post')
    op.drop_column('blog_post', 'pubdate')
    # ### end Alembic commands ###
