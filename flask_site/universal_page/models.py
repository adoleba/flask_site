from flask_site import db


class UniversalPage(db.Model):
    name = db.Column(db.String(64), nullable=False)
    url = db.Column(db.Unicode(20), unique=True, nullable=False)
    id = db.Column(db.Integer, primary_key=True)


class WhiteHeaderWithButton(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header_text = db.Column(db.String, nullable=False)
    button_text = db.Column(db.String, nullable=False)
    button_url = db.Column(db.String, nullable=False)
    order_WhiteHeaderWithButton = db.Column(db.Integer)
    universal_page_whiteheaderwithbutton_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    universal_page_whiteheaderwithbutton = db.relationship(UniversalPage, backref='whiteheaderwithbutton')


class ThreeColumnsWithHeaders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    column_no_1_header = db.Column(db.String, nullable=False)
    column_no_1_text = db.Column(db.Text, nullable=False)
    column_no_2_header = db.Column(db.String, nullable=False)
    column_no_2_text = db.Column(db.Text, nullable=False)
    column_no_3_header = db.Column(db.String, nullable=False)
    column_no_3_text = db.Column(db.Text, nullable=False)
    order_ThreeColumnsWithHeaders = db.Column(db.Integer)

    threecolumnswithheaders_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    threecolumnswithheaders = db.relation(UniversalPage, backref='threecolumnswithheaders')


class BlockQuoteWithHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header_text = db.Column(db.Text, nullable=False)
    paragraph_text = db.Column(db.Text, nullable=False)
    order_BlockQuoteWithHeader = db.Column(db.Integer)

    blockquotewithheader_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    blockquotewithheader = db.relation(UniversalPage, backref='blockquotewithheader')


class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    order_Faq = db.Column(db.Integer)

    faq_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    faq = db.relation(UniversalPage, backref='faq')


class GreyHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, nullable=False)
    order_GreyHeader = db.Column(db.Integer, nullable=False)

    greyheader_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    greyheader = db.relation(UniversalPage, backref='greyheader')


class SmallGreyHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, nullable=False)
    order_SmallGreyHeader = db.Column(db.Integer)

    smallgreyheader_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    smallgreyheader = db.relation(UniversalPage, backref='smallgreyheader')


class BlockQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, nullable=False)
    order_BlockQuote = db.Column(db.Integer)

    blockquote_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    blockquote = db.relation(UniversalPage, backref='blockquote')
