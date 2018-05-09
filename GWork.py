from flask_admin import AdminIndexView, expose

from app import app
import flask_admin as admin
from flask_admin.contrib.mongoengine import ModelView

from app.admin import UserView, PositionView, ReportView
from app.models import Users, Positiones, Reports


class IndexView(AdminIndexView):
	@expose('/')
	def index(self):
		return self.render('user/login.html')


admin = admin.Admin(app, '后台管理', index_view=AdminIndexView(
	name='首页',
	template='admin/index.html',
	url='/admin'
))
# Add views

admin.add_view(UserView(Users, '用户管理'))
admin.add_view(PositionView(Positiones, '职位信息管理'))
admin.add_view(ReportView(Reports, '模板信息管理'))
app.run()
