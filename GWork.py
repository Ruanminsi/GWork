from app import app
import flask_admin as admin
from flask_admin.contrib.mongoengine import ModelView

from app.admin import UserView
from app.models import Users

admin = admin.Admin(app, '后台管理')
# Add views

admin.add_view(UserView(Users, '用户管理'))
app.run()
