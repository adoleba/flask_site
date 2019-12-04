from flask import url_for, redirect, request
from flask_admin.contrib.sqla import ModelView
import flask_login as login
from flask_login import current_user
from wtforms import TextAreaField
from wtforms.widgets import TextArea

from flask_site.blog.models import Post


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class AdminPostView(ModelView):

    form_excluded_columns = ('user_name', 'user')
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
        return super().get_query().filter(Post.user_name == current_user.username)

    def is_accessible(self):
        return login.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.args.get))


class AdminUserView(ModelView):

    column_searchable_list = ('username',)
    column_default_sort = ('username', True)
    page_size = 20
    column_exclude_list = ['password', ]
    form_excluded_columns = ('posts',)
