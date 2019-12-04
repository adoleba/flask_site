from flask import render_template

from . import about


@about.route('')
def about():
    return render_template("about/about.html")
