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
    form_columns = ['companyFullName', 'companyShortName', 'companyLabelList',
                    'companySize', 'financeStage', 'industryField', 'industryLables',
                    'positionName', 'salary', 'workYear', 'education', 'positionLables',
                    'jobNature', 'firstType', 'secondType', 'positionAdvantage',
                    'city', 'createdTime'
                    ]
    column_labels = dict(
        companyFullName='公司全名',
        companyShortName='公司缩写',
        companyLabelList='公司标签',
        companySize='公司规模',
        financeStage='融资阶段',
        industryField='企业领域',
        industryLables='企业标签',
        positionName='职位名称',
        salary='薪资',
        workYear='工作经验',
        education='学历',
        positionLables='职位标签',
        jobNature='职位类型',
        firstType='职位大类',
        secondType='职位细类',
        positionAdvantage='职位优势',
        city='城市',
        createdTime='发布时间'
    )
    column_filters = ['city']
    column_searchable_list = ('city', 'salary')


@admin.route('/login')
def index():
    return render_template('admin/login.html')
