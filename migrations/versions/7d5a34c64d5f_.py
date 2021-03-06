"""empty message

Revision ID: 7d5a34c64d5f
Revises: b4c148929329
Create Date: 2021-05-01 14:01:58.864812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d5a34c64d5f'
down_revision = 'b4c148929329'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_subscribes_name', table_name='subscribes')
    op.drop_column('subscribes', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscribes', sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.create_index('ix_subscribes_name', 'subscribes', ['name'], unique=False)
    # ### end Alembic commands ###
