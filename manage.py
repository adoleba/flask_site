from flask_admin import Admin

from flask_site.about.models import About
from flask_site.admin import AdminPostView, AdminUserView, AdminAboutView
from flask_site.users.models import User
from flask_site.blog.models import Post
from flask_site import create_app, db

app = create_app()

admin = Admin(app, index_view=AdminPostView(Post, db.session, url='/admin'))
admin.add_view(AdminUserView(User, db.session))
admin.add_view(AdminAboutView(About, db.session))

if __name__ == '__main__':
    app.run()
