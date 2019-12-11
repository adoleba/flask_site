"""empty message

Revision ID: 2d5a2b624878
Revises: 93c50b06a0f1
Create Date: 2019-12-09 12:24:12.042969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d5a2b624878'
down_revision = '93c50b06a0f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_contact_thank_you_edited', table_name='contact_thank_you')
    op.drop_table('contact_thank_you')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_thank_you',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('intro', sa.VARCHAR(), nullable=True),
    sa.Column('body', sa.TEXT(), nullable=True),
    sa.Column('edited', sa.DATETIME(), nullable=True),
    sa.Column('title', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_contact_thank_you_edited', 'contact_thank_you', ['edited'], unique=False)
    # ### end Alembic commands ###