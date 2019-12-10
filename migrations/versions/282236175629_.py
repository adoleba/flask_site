"""empty message

Revision ID: 282236175629
Revises: 4c9c15c00377
Create Date: 2019-12-10 16:09:04.033757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '282236175629'
down_revision = '4c9c15c00377'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('block_quote_with_header')
    op.drop_table('three_columns_with_headers')
    op.drop_table('universal_page')
    op.drop_table('grey_header')
    op.drop_table('faq')
    op.drop_table('block_quote')
    op.drop_table('white_header_with_button')
    op.drop_table('small_grey_header')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('small_grey_header',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('header', sa.VARCHAR(), nullable=True),
    sa.Column('smallgreyheader_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['smallgreyheader_id'], ['universal_page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('white_header_with_button',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('header_text', sa.VARCHAR(), nullable=True),
    sa.Column('button_text', sa.VARCHAR(), nullable=True),
    sa.Column('button_url', sa.VARCHAR(), nullable=True),
    sa.Column('universal_page_whiteheaderwithbutton_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['universal_page_whiteheaderwithbutton_id'], ['universal_page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('block_quote',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('header', sa.VARCHAR(), nullable=True),
    sa.Column('blockquote_id', sa.INTEGER(), nullable=True),
    sa.Column('order', sa.INTEGER(), nullable=True),
    sa.Column('order_BlockQuote', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['blockquote_id'], ['universal_page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('faq',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question', sa.VARCHAR(), nullable=True),
    sa.Column('answer', sa.TEXT(), nullable=True),
    sa.Column('faq_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['faq_id'], ['universal_page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grey_header',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('header', sa.VARCHAR(), nullable=True),
    sa.Column('greyheader_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['greyheader_id'], ['universal_page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('universal_page',
    sa.Column('name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('url', sa.VARCHAR(length=20), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('three_columns_with_headers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('column_no_1_header', sa.VARCHAR(), nullable=True),
    sa.Column('column_no_1_text', sa.TEXT(), nullable=True),
    sa.Column('column_no_2_header', sa.VARCHAR(), nullable=True),
    sa.Column('column_no_2_text', sa.TEXT(), nullable=True),
    sa.Column('column_no_3_header', sa.VARCHAR(), nullable=True),
    sa.Column('column_no_3_text', sa.TEXT(), nullable=True),
    sa.Column('threecolumnswithheaders_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['threecolumnswithheaders_id'], ['universal_page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('block_quote_with_header',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('header_text', sa.TEXT(), nullable=True),
    sa.Column('paragraph_text', sa.TEXT(), nullable=True),
    sa.Column('blockquotewithheader_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['blockquotewithheader_id'], ['universal_page.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
