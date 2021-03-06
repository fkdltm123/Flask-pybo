"""empty message

Revision ID: 086cc68a136c
Revises: f5e96dc5a57c
Create Date: 2022-01-10 17:50:52.669588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '086cc68a136c'
down_revision = 'f5e96dc5a57c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
