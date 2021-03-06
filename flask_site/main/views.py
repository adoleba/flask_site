from flask import render_template

from flask_site.blog.models import Post
from flask_site.common.views import PageView
from flask_site.main.models import Home


class HomePage(PageView):
    def get(self, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'home': Home.query.filter_by(id=1).first(),
            'posts': Post.query.order_by(Post.timestamp.desc())[:3],
        })
        return render_template('index.html', **ctx)
