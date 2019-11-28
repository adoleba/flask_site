from flask import render_template
from . import blog


@blog.route('')
def blog_page():
    return render_template("blog/blog_page.html")
