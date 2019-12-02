
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_script import Manager

from flask_site.users.models import User
from flask_site.blog.models import Post
from flask_site import create_app, db
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)


admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()
