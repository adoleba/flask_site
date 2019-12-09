from flask import render_template

from flask_site.common.views import PageView


class SamplePage(PageView):
    def get(self):

        return render_template('universal_page/universal_page.html')
