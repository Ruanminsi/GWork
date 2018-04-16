from flask import Flask, render_template, request
# from flask_pymongo import PyMongo
import config

app = Flask(__name__)
app.config.from_object('config')
app.config.update(
	MONGO_HOST='localhost',
	MONGO_PORT=27017,
	MONGO_USERNAME='',
	MONGO_PASSWORD='',
	MONGO_DBNAME='todos'
)
# mongo = PyMongo(app)


@app.route('/')
def hello_world():
	# names = mongo.db.users.find().limit(5)
	# print(names)
	return render_template('user/login.html')


from app import models, views
