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
    from app.models import Position
    p = Position(companyFullName="1", companyShortName="11",
                 companyLabelList="a", companySize="2",
                 financeStage="a1", industryField="a2",
                 industryLables="t,t", positionName="23",
                 salary="5-6", workYear="2122",
                 education="3y", positionLables="ssss",
                 jobNature="314", firstType="1444",
                 secondType="gg", positionAdvantage="1d",
                 city="31", district="dasd")
    p.save()
    return render_template('user/login.html')


from app import models, views
