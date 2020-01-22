from flask import render_template


def page_not_found(error):
    return render_template('errors/404.html'), 404
