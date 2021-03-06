"""empty message

Revision ID: 28b1c13def31
Revises: acba63349b9f
Create Date: 2022-05-25 15:10:28.518315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28b1c13def31'
down_revision = 'acba63349b9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    op.execute('UPDATE todos SET completed=False WHERE completed IS NULL;')
    op.alter_column('todos','completed',nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
