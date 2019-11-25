from flask import render_template

from . import main


@main.route('/')
def main():
    return render_template('index.html')
