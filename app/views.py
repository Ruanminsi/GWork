from app import app
from .admin import admin
from .user import user

app.register_blueprint(admin, url_prefix='/admins')
app.register_blueprint(user, url_prefix='/user')

