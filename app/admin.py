from flask import Blueprint, render_template, redirect, request
from flask_admin.contrib.mongoengine import ModelView

admin = Blueprint('admins', __name__)


class UserView(ModelView):
    form_columns = ['name', 'password',
                    'nickname', 'question',
                    'answer']
    column_labels = dict(
        name='用户名',
        password='密码',
        nickname='昵称',
        question='密保问题',
        answer='密保答案',
        role='角色',
        login_status='登录状态',
        last_login='登录时间'
    )
    column_filters = ['name']
    column_searchable_list = ('name', 'password')
    column_exclude_list = (
        'register',
    )


class PositionView(ModelView):
    form_columns = ['companyFullName',
                    'companySize', 'financeStage',  'industryField',
                    'positionName', 'salary', 'workYear', 'education',
                    'firstType', 'secondType', 'positionAdvantage',
                    'city'
                    ]
    column_labels = dict(
        companyFullName='公司全名',
        # companyShortName='公司缩写',
        companyLabelList='公司标签',
        companySize='公司规模',
        financeStage='融资阶段',
        industryField='企业领域',
        # industryLables='企业标签',
        positionName='职位名称',
        salary='薪资',
        workYear='工作经验',
        education='学历',
        # positionLables='职位标签',
        # jobNature='职位类型',
        firstType='职位大类',
        secondType='职位细类',
        positionAdvantage='职位优势',
        city='城市'
    )
    column_filters = ['city']
    column_searchable_list = ('city', 'salary')
    column_exclude_list = (
        'companyLabelList'
    )


class ReportView(ModelView):
    form_columns = ['pname', 'pcontent', 'flag']
    column_labels = dict(
        pname='公共信息名称',
        pcontent='公共信息内容',
        flag='是否隐藏'
    )
    column_filters = ['pname', 'pcontent', 'flag']


@admin.route('/login')
@admin.route('/login/')
def index():
    return render_template('admin/login.html')


