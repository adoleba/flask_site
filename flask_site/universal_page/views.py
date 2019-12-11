from flask import render_template

from flask_site.common.views import PageView
from flask_site.universal_page.models import UniversalPage


class SamplePage(PageView):

    def dispatch_request(self, *args, **kwargs):

        ctx = self.get_context_data(**kwargs)
        url = ctx['url']
        page = UniversalPage.query.filter_by(url=url).first()

        order_dict = {}

        if page:
            if page.blockquote:
                order_BlockQuote = page.blockquote[0].order_BlockQuote
                if order_BlockQuote:
                    order_dict['blockquote'] = order_BlockQuote

            if page.smallgreyheader:
                order_SmallGreyHeader = page.smallgreyheader[0].order_SmallGreyHeader
                if order_SmallGreyHeader:
                    order_dict['smallgreyheader'] = order_SmallGreyHeader

            if page.blockquotewithheader:
                order_BlockQuoteWithHeader = page.blockquotewithheader[0].order_BlockQuoteWithHeader
                if order_BlockQuoteWithHeader:
                    order_dict['blockquotewithheader'] = order_BlockQuoteWithHeader

            if page.faq:
                order_Faq = page.faq[0].order_Faq
                if order_Faq:
                    order_dict['faq'] = order_Faq

            if page.greyheader:
                order_GreyHeader = page.greyheader[0].order_GreyHeader
                if order_GreyHeader:
                    order_dict['greyheader'] = order_GreyHeader

            if page.threecolumnswithheaders:
                order_ThreeColumnsWithHeaders = page.threecolumnswithheaders[0].order_ThreeColumnsWithHeaders
                if order_ThreeColumnsWithHeaders:
                    order_dict['threecolumnswithheaders'] = order_ThreeColumnsWithHeaders

            if page.whiteheaderwithbutton:
                order_WhiteHeaderWithButton = page.whiteheaderwithbutton[0].order_WhiteHeaderWithButton
                if order_WhiteHeaderWithButton:
                    order_dict['whiteheaderwithbutton'] = order_WhiteHeaderWithButton

        sorted_dict = {k: v for k, v in sorted(order_dict.items(), key=lambda item: item[1])}

        return render_template('universal_page/universal_page.html', page=page, sorted_dict=sorted_dict,  **ctx)








