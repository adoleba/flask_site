from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)


@app.route('/')
def main():
    return "hello world"


if __name__ == '__main__':
    app.run()
