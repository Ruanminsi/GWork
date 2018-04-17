from app import app
import flask_admin as admin
from flask_admin.contrib.mongoengine import ModelView

from app.admin import UserView, PositionView
from app.models import Users, Position

admin = admin.Admin(app, '后台管理')
# Add views

admin.add_view(UserView(Users, '用户管理'))
admin.add_view(PositionView(Position, '职位信息管理'))
app.run()
