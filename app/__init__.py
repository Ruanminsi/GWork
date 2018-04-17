from flask import Flask, render_template, request
from flask_mongoengine import MongoEngine
import config

app = Flask(__name__)
app.config.from_object('config')
# app.config.update(
# 	MONGO_HOST='localhost',
# 	MONGO_PORT=27017,
# 	MONGO_USERNAME='',
# 	MONGO_PASSWORD='',
# 	MONGO_DBNAME='todos'
# )
app.config['MONGODB_SETTINGS'] = {'DB': 'todos'}
db = MongoEngine(app)


@app.route('/')
def hello_world():
	# names = mongo.db.users.find().limit(5)
	# print(names)
	from app.models import Users
	user = Users(name="test-0", password="000")
	user.save()

	return render_template('user/login.html')


from app import models, views
