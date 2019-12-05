import os

from flask_script import Manager

from flask_site import config

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
manager = Manager()


def create_app():
    app = Flask(__name__)

    if app.env == 'production':
        app.config.from_object(config.ProductionConfig)
    elif app.env == 'testing':
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    manager.add_command('db', MigrateCommand)

    from flask_site.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from flask_site.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')

    from flask_site.users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')

    from flask_site.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix='/blog')

    from flask_site.about import about as about_blueprint
    app.register_blueprint(about_blueprint, url_prefix='/about')

    from flask_site.users.models import User
    from flask_site.blog.models import Post

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
