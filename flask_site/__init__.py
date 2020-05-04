import os

from flask import Flask
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from flask_site import config
from flask_site.config import DevelopmentConfig

db = SQLAlchemy()
manager = Manager()
mail = Mail()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    config_name = os.getenv('FLASK_ENV')

    app.config.from_object(config.config[config_name])
    app.config.from_pyfile('application.cfg', silent=True)

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    migrate = Migrate(app, db)
    mail.init_app(app)
    manager.add_command('db', MigrateCommand)

    from flask_site.blog.models import Post
    from flask_site.users.models import Author
    from flask_site.about.models import About
    from flask_site.admin import AdminPostView, AdminUserView, AdminPageView, ContactThankYouAdminPageView, \
        UniversalPageAdmin, RolePageView, LogoutAdminMenuLink
    from flask_site.contact.models import Contact, ContactThankYou
    from flask_site.main.models import Home
    from flask_site.universal_page.models import UniversalPage
    from flask_site.users.models import Role

    admin = Admin(app, index_view=AdminPostView(Post, db.session, url='/admin'))

    admin.add_view(AdminUserView(Author, db.session))
    admin.add_view(AdminPageView(About, db.session))
    admin.add_view(AdminPageView(Home, db.session))
    admin.add_view(AdminPageView(Contact, db.session))
    admin.add_view(ContactThankYouAdminPageView(ContactThankYou, db.session))
    admin.add_view(UniversalPageAdmin(UniversalPage, db.session))
    admin.add_view(RolePageView(Role, db.session))
    admin.add_link(LogoutAdminMenuLink(name='Logout', url='/logout'))
    admin.add_link(MenuLink(name="Home Page", url='/'))

    from flask_site.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from flask_site.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')

    from flask_site.universal_page import universal_page as universal_page_blueprint
    app.register_blueprint(universal_page_blueprint, url_prefix='/')

    from flask_site.users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')

    from flask_site.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix='/blog')

    from flask_site.about import about_us as about_blueprint
    app.register_blueprint(about_blueprint, url_prefix='/about')

    from flask_site.contact import contact_us as contact_blueprint
    app.register_blueprint(contact_blueprint, url_prefix='/contact')

    from flask_site.about import views, models
    from flask_site.main import views, models
    from flask_site.contact import views, models
    from flask_site.universal_page import views, models
    from flask_site.common import filters

    from flask_site.common.filters import subtract

    app.jinja_env.filters['subtract'] = subtract

    @login_manager.user_loader
    def load_user(author_id):
        return Author.query.get(int(author_id))

    return app
