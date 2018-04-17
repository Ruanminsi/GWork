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

class PositionView(ModelView):
    form_columns = ['companyFullName', 'companyShortName','companyLabelList',
                    'companySize','financeStage','industryField','industryLables',
                    'positionName','salary','workYear','education','positionLables',
                    'jobNature','firstType','secondType','positionAdvantage','city'
                    ]
    column_labels = dict(
        companyFullName='公司全名',
        companyShortName='公司缩写'
    )
    column_filters = ['city']
    column_searchable_list = ('city', 'salary')

@admin.route('/login')
def index():
    return render_template('admin/login.html')