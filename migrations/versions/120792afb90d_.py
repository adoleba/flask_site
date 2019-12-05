"""empty message

Revision ID: 120792afb90d
Revises: 
Create Date: 2019-12-05 11:31:30.292938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '120792afb90d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('title_description', sa.Text(), nullable=True),
    sa.Column('red_intro', sa.String(), nullable=True),
    sa.Column('black_intro', sa.String(), nullable=True),
    sa.Column('intro_description', sa.Text(), nullable=True),
    sa.Column('first_offer', sa.String(), nullable=True),
    sa.Column('first_offer_description', sa.Text(), nullable=True),
    sa.Column('second_offer', sa.String(), nullable=True),
    sa.Column('second_offer_description', sa.Text(), nullable=True),
    sa.Column('third_offer', sa.String(), nullable=True),
    sa.Column('third_offer_description', sa.Text(), nullable=True),
    sa.Column('first_step', sa.String(), nullable=True),
    sa.Column('first_step_description', sa.Text(), nullable=True),
    sa.Column('second_step', sa.String(), nullable=True),
    sa.Column('second_step_description', sa.Text(), nullable=True),
    sa.Column('third_step', sa.String(), nullable=True),
    sa.Column('third_step_description', sa.Text(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_about_edited'), 'about', ['edited'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=10000), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('firstname', sa.String(length=50), nullable=True),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('intro', sa.String(length=200), nullable=True),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_name', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_name'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_table('user')
    op.drop_index(op.f('ix_about_edited'), table_name='about')
    op.drop_table('about')
    # ### end Alembic commands ###