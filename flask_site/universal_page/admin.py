from flask_admin.model import InlineFormAdmin

from flask_site.universal_page.models import WhiteHeaderWithButton, ThreeColumnsWithHeaders, \
    BlockQuoteWithHeader, Faq, GreyHeader, SmallGreyHeader, BlockQuote


class WhiteHeaderWithButtonForm(InlineFormAdmin):

    form_label = 'White Header With Button'

    def __init__(self):
        super().__init__(WhiteHeaderWithButton)


class ThreeColumnsWithHeadersForm(InlineFormAdmin):

    form_label = 'Three Columns With Headers'

    def __init__(self):
        super().__init__(ThreeColumnsWithHeaders)


class BlockQuoteWithHeaderForm(InlineFormAdmin):

    form_label = 'Block Quote With Header'

    def __init__(self):
        super().__init__(BlockQuoteWithHeader)


class FaqForm(InlineFormAdmin):

    form_label = 'Faq'

    def __init__(self):
        super().__init__(Faq)


class GreyHeaderForm(InlineFormAdmin):

    form_label = 'Grey Header'

    def __init__(self):
        super().__init__(GreyHeader)


class SmallGreyHeaderForm(InlineFormAdmin):

    form_label = 'Small Grey Header'

    def __init__(self):
        super().__init__(SmallGreyHeader)


class BlockQuoteForm(InlineFormAdmin):
    form_label = 'Block Quote'

    def __init__(self):
        super().__init__(BlockQuote)
