import flask_login as login

from flask import url_for, redirect, request
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_user import current_user
from wtforms import TextAreaField
from wtforms.widgets import TextArea

from flask_site.blog.models import Post
from flask_site.universal_page.admin import BlockQuoteWithHeaderForm, ThreeColumnsWithHeadersForm, \
    WhiteHeaderWithButtonForm, FaqForm, SmallGreyHeaderForm, GreyHeaderForm, BlockQuoteForm
from flask_site.users.models import User


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class SuperUserView(ModelView):

    def is_accessible(self):
        if 'superuser' in login.current_user.role:
            return True


class AdminPostView(ModelView):

    form_excluded_columns = ('user_name', 'user', 'timestamp')
    column_exclude_list = ('body', )
    column_searchable_list = ('title',)
    column_default_sort = ('timestamp', True)
    page_size = 20

    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    form_overrides = {
        'body': CKTextAreaField
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'
        self.endpoint = 'admin'

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.user_name = current_user.username

    def get_query(self):
        if 'superuser' in login.current_user.role:
            return super().get_query()
        return super().get_query().filter(Post.user_name == current_user.username)

    def is_accessible(self):
        return login.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.args.get))


class AdminUserView(ModelView):
    column_searchable_list = ('username',)
    column_default_sort = ('username', True)
    page_size = 20
    column_exclude_list = ['password', 'about_me', 'password_code']
    form_excluded_columns = ('role', 'password', 'created', 'posts', 'password_code')
    form_overrides = {'about_me': TextAreaField}

    @property
    def can_create(self):
        if 'superuser' in login.current_user.role:
            return True

    @property
    def can_delete(self):
        if 'superuser' in login.current_user.role:
            return True

    def get_query(self):
        if 'superuser' in login.current_user.role:
            return super().get_query()
        return super().get_query().filter(User.username == current_user.username)


class AdminPageView(SuperUserView):
    can_delete = False
    can_create = False
    column_list = ('title', 'edited')
    form_excluded_columns = 'edited'


class ContactThankYouAdminPageView(SuperUserView):
    can_delete = False
    can_create = False
    column_list = ('intro', 'edited')
    form_excluded_columns = 'edited'


class RolePageView(SuperUserView):
    column_list = ('name', 'description')


class UniversalPageAdmin(SuperUserView):

    inline_models = (BlockQuoteWithHeaderForm(), ThreeColumnsWithHeadersForm(),
                     WhiteHeaderWithButtonForm(), FaqForm(), SmallGreyHeaderForm(), GreyHeaderForm(), BlockQuoteForm(),)


class LogoutAdminMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated
