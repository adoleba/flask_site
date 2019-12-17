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
    order_whiteheaderwithbutton = db.Column(db.Integer)
    whiteheaderwithbutton_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    whiteheaderwithbutton = db.relationship(UniversalPage, backref='whiteheaderwithbutton')


class ThreeColumnsWithHeaders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    column_no_1_header = db.Column(db.String, nullable=False)
    column_no_1_text = db.Column(db.Text, nullable=False)
    column_no_2_header = db.Column(db.String, nullable=False)
    column_no_2_text = db.Column(db.Text, nullable=False)
    column_no_3_header = db.Column(db.String, nullable=False)
    column_no_3_text = db.Column(db.Text, nullable=False)
    order_threecolumnswithheaders = db.Column(db.Integer)

    threecolumnswithheaders_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    threecolumnswithheaders = db.relation(UniversalPage, backref='threecolumnswithheaders')


class BlockQuoteWithHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header_text = db.Column(db.Text, nullable=False)
    paragraph_text = db.Column(db.Text, nullable=False)
    order_blockquotewithheader = db.Column(db.Integer)

    blockquotewithheader_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    blockquotewithheader = db.relation(UniversalPage, backref='blockquotewithheader')


class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    order_faq = db.Column(db.Integer)

    faq_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    faq = db.relation(UniversalPage, backref='faq')


class GreyHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, nullable=False)
    order_greyheader = db.Column(db.Integer, nullable=False)

    greyheader_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    greyheader = db.relation(UniversalPage, backref='greyheader')


class SmallGreyHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, nullable=False)
    order_smallgreyheader = db.Column(db.Integer)

    smallgreyheader_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    smallgreyheader = db.relation(UniversalPage, backref='smallgreyheader')


class BlockQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String, nullable=False)
    order_blockquote = db.Column(db.Integer)

    blockquote_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    blockquote = db.relation(UniversalPage, backref='blockquote')
