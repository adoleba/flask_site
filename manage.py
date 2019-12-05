
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_site.admin import AdminPostView, AdminUserView
from flask_site.users.models import User
from flask_site.blog.models import Post
from flask_site import create_app, db

app = create_app()

admin = Admin(app, index_view=AdminPostView(Post, db.session, url='/admin'))
admin.add_view(AdminUserView(User, db.session))


if __name__ == '__main__':
    app.run()
