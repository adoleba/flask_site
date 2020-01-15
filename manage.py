from flask_admin import Admin
from flask_admin.menu import MenuLink

from flask_site.about.models import About
from flask_site.admin import AdminPostView, AdminUserView, AdminPageView, ContactThankYouAdminPageView,\
    UniversalPageAdmin, RolePageView, LogoutAdminMenuLink
from flask_site.contact.models import Contact, ContactThankYou
from flask_site.main.models import Home
from flask_site.universal_page.models import UniversalPage
from flask_site.users.models import User, Role
from flask_site.blog.models import Post
from flask_site import create_app, db

app = create_app()
admin = Admin(app, index_view=AdminPostView(Post, db.session, url='/admin'))
admin.add_view(AdminUserView(User, db.session))
admin.add_view(AdminPageView(About, db.session))
admin.add_view(AdminPageView(Home, db.session))
admin.add_view(AdminPageView(Contact, db.session))
admin.add_view(ContactThankYouAdminPageView(ContactThankYou, db.session))
admin.add_view(UniversalPageAdmin(UniversalPage, db.session))
admin.add_view(RolePageView(Role, db.session))
admin.add_link(LogoutAdminMenuLink(name='Logout', url='/logout'))
admin.add_link(MenuLink(name="Home Page", url='/'))

if __name__ == '__main__':
    app.run()
