from flask_site import db


class UniversalPage(db.Model):
    name = db.Column(db.String(64))
    url = db.Column(db.Unicode(20), unique=True)
    id = db.Column(db.Integer, primary_key=True)


class WhiteHeaderWithButton(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header_text = db.Column(db.String)
    button_text = db.Column(db.String)
    button_url = db.Column(db.String)
    universal_page_whiteheaderwithbutton_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    universal_page_whiteheaderwithbutton = db.relationship(UniversalPage, backref='whiteheaderwithbutton')


class ThreeColumnsWithHeaders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    column_no_1_header = db.Column(db.String)
    column_no_1_text = db.Column(db.Text)
    column_no_2_header = db.Column(db.String)
    column_no_2_text = db.Column(db.Text)
    column_no_3_header = db.Column(db.String)
    column_no_3_text = db.Column(db.Text)

    threecolumnswithheaders_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    threecolumnswithheaders = db.relation(UniversalPage, backref='threecolumnswithheaders')


class BlockQuoteWithHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header_text = db.Column(db.Text)
    paragraph_text = db.Column(db.Text)

    blockquotewithheader_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    blockquotewithheader = db.relation(UniversalPage, backref='blockquotewithheader')


class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.Text)

    faq_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    faq = db.relation(UniversalPage, backref='faq')


class GreyHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String)

    greyheader_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    greyheader = db.relation(UniversalPage, backref='greyheader')


class SmallGreyHeader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String)

    smallgreyheader_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    smallgreyheader = db.relation(UniversalPage, backref='smallgreyheader')


class BlockQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String)

    blockquote_id = db.Column(db.Integer, db.ForeignKey(UniversalPage.id))
    blockquote = db.relation(UniversalPage, backref='blockquote')
