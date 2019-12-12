from flask import render_template

from flask_site.common.views import PageView
from flask_site.universal_page.models import UniversalPage


class SamplePage(PageView):

    def dispatch_request(self, *args, **kwargs):

        ctx = self.get_context_data(**kwargs)
        url = ctx['url']
        page = UniversalPage.query.filter_by(url=url).first()

        block_order_list = []
        block_models = ['whiteheaderwithbutton', 'smallgreyheader', 'blockquotewithheader', 'faq', 'greyheader',
                        'threecolumnswithheaders', 'blockquote']

        if page:
            for model in block_models:
                if getattr(page, model):

                    blocks_quantity = len(getattr(page, model))
                    for number in range(blocks_quantity):

                        block_order_name = 'order_' + model
                        order = getattr(getattr(page, model)[number], block_order_name)
                        current_block = getattr(page, model)[number]
                        attributes_list = []
                        model_columns = current_block.__table__.columns._data.keys()
                        for value in model_columns:
                            attributes_list.append(value)

                        attribute_values = []
                        for element in attributes_list:
                            attribute_values.append(getattr(current_block, element))

                        block_order_list.append((str(order), model, attribute_values))
        sorted_list = sorted(block_order_list)

        return render_template('universal_page/universal_page.html', page=page, sorted_list=sorted_list, **ctx)
