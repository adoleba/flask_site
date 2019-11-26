from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    from flask_site.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from flask_site.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')

    from flask_site.users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')

    from flask_site.users.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
