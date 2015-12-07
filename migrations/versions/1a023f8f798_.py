"""empty message

Revision ID: 1a023f8f798
Revises: None
Create Date: 2015-12-07 11:00:45.992669

"""

# revision identifiers, used by Alembic.
revision = '1a023f8f798'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweet', sa.Column('author_id', sa.Integer(), nullable=True))
    op.drop_constraint('tweet_user_fkey', 'tweet', type_='foreignkey')
    op.create_foreign_key(None, 'tweet', 'user', ['author_id'], ['id'])
    op.drop_column('tweet', 'user')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweet', sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'tweet', type_='foreignkey')
    op.create_foreign_key('tweet_user_fkey', 'tweet', 'user', ['user'], ['id'])
    op.drop_column('tweet', 'author_id')
    ### end Alembic commands ###
