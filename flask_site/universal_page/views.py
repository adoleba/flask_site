from flask import render_template

from flask_site.common.views import PageView
from flask_site.universal_page.models import UniversalPage


class SamplePage(PageView):

    def dispatch_request(self, *args, **kwargs):

        ctx = self.get_context_data(**kwargs)
        url = ctx['url']
        page = UniversalPage.query.filter_by(url=url).first()

        blocks_order_dict = {}

        if page:
            if page.blockquote:
                order_BlockQuote = page.blockquote[0].order_BlockQuote
                blocks_order_dict['blockquote'] = order_BlockQuote

            if page.smallgreyheader:
                order_SmallGreyHeader = page.smallgreyheader[0].order_SmallGreyHeader
                blocks_order_dict['smallgreyheader'] = order_SmallGreyHeader

            if page.blockquotewithheader:
                order_BlockQuoteWithHeader = page.blockquotewithheader[0].order_BlockQuoteWithHeader
                blocks_order_dict['blockquotewithheader'] = order_BlockQuoteWithHeader

            if page.faq:
                order_Faq = page.faq[0].order_Faq
                blocks_order_dict['faq'] = order_Faq

            if page.greyheader:
                order_GreyHeader = page.greyheader[0].order_GreyHeader
                blocks_order_dict['greyheader'] = order_GreyHeader

            if page.threecolumnswithheaders:
                order_ThreeColumnsWithHeaders = page.threecolumnswithheaders[0].order_ThreeColumnsWithHeaders
                blocks_order_dict['threecolumnswithheaders'] = order_ThreeColumnsWithHeaders

            if page.whiteheaderwithbutton:
                order_WhiteHeaderWithButton = page.whiteheaderwithbutton[0].order_WhiteHeaderWithButton
                blocks_order_dict['whiteheaderwithbutton'] = order_WhiteHeaderWithButton

        blocks_sorted_dict = {block_name: block_order for block_name, block_order in sorted(blocks_order_dict.items(), key=lambda item: item[1])}

        return render_template('universal_page/universal_page.html', page=page,
                               blocks_sorted_dict=blocks_sorted_dict,  **ctx)
