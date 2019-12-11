from flask import render_template

from flask_site.common.views import PageView
from flask_site.universal_page.models import UniversalPage


class SamplePage(PageView):

    def dispatch_request(self, *args, **kwargs):

        ctx = self.get_context_data(**kwargs)
        url = ctx['url']
        page = UniversalPage.query.filter_by(url=url).first()

        blocks_order_dict = {}
        block_models = ['blockquote', 'smallgreyheader', 'blockquotewithheader', 'faq', 'greyheader',
                        'threecolumnswithheaders', 'whiteheaderwithbutton']

        if page:
            for model in block_models:
                if getattr(page, model):
                    block_order_name = 'order_' + model
                    order = getattr(getattr(page, model)[0], block_order_name)
                    blocks_order_dict[model] = order

        blocks_sorted_dict = {block_name: block_order for block_name, block_order in sorted(blocks_order_dict.items(),
                                                                                            key=lambda item: item[1])}

        return render_template('universal_page/universal_page.html', page=page,
                               blocks_sorted_dict=blocks_sorted_dict, **ctx)
