import datetime

from app import db
from time import time

class Users(db.Document):
    name = db.StringField(max_length=128, required=True)
    password = db.StringField(max_length=128, required=True)
    nickname = db.StringField(default="", max_length=128)
    question = db.StringField(default="", max_length=128)
    answer = db.StringField(default="", max_length=128)
    role = db.IntField(default=0)
    register = db.DateTimeField(default=datetime.datetime.now)
    last_login = db.DateTimeField(default=datetime.datetime.now)
    login_status = db.IntField(default=0)


class Positiones(db.Document):
    companyFullName = db.StringField(max_length=256)
    companyLabelList = db.ListField(db.StringField(max_length=512))
    companySize = db.StringField(max_length=256)
    financeStage = db.StringField(max_length=256)
    industryField = db.StringField(max_length=256)
    positionName = db.StringField(max_length=256)
    salary = db.StringField(max_length=256)
    workYear = db.StringField(max_length=256)
    education = db.StringField(max_length=256)
    firstType = db.StringField(max_length=256)
    secondType = db.StringField(max_length=256)
    positionAdvantage = db.StringField(max_length=256)
    city = db.StringField(max_length=256)


class Reports(db.Document):
    pname = db.StringField(max_length=256)
    pcontent = db.StringField(max_length=256)
    flag = db.IntField(default=0)