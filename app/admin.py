from flask import Blueprint, render_template, redirect, request
from flask_admin.contrib.mongoengine import ModelView

admin = Blueprint('admins', __name__)



class UserView(ModelView):
    form_columns = ['name', 'password']
    column_labels = dict(
        name='用户名',
        password='密码'
    )

    column_filters = ['name']

    column_searchable_list = ('name', 'password')

@admin.route('/login')
def index():
    return render_template('admin/login.html')