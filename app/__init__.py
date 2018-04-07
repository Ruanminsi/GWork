from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import config

app = Flask(__name__)
app.config.from_object('config')
app.config.update(
	MONGO_HOST='localhost',
	MONGO_PORT=27017,
	MONGO_USERNAME='',
	MONGO_PASSWORD='',
	MONGO_DBNAME='GPWork'
)
mongo = PyMongo(app)


@app.route('/')
def hello_world():
	return render_template('user/login.html')


from app import models, views
