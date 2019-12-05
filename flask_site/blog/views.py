from flask import render_template

from flask_site.blog.models import Post
from flask_site.common.views import PageView


class BlogPage(PageView):
    def get(self, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'posts': Post.query.order_by(Post.timestamp.desc()),
        })
        return render_template('blog/blog_page.html', **ctx)


class PostPage(PageView):
    def get(self, id, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'post': Post.query.get_or_404(id)
        })
        return render_template('blog/post_page.html', **ctx)
