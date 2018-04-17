import datetime

from app import db
from time import time


class User(object):
    @classmethod
    def create_user(cls, username, password):
        return {
            'username': username,
            'password': password,
            'nickname': None,
            'register_at': time(),
            'question': None,
            'answer': None,
            'record': None,
            'status': 0,
            'last_login_at': None,
        }


class Users(db.Document):
    name = db.StringField(max_length=128, required=True)
    password = db.StringField(max_length=128, required=True)
    nickname = db.StringField(default="", max_length=128)
    question = db.StringField(default="", max_length=128)
    answer = db.StringField(default="", max_length=128)
    role = db.IntField(default=0)
    register = db.DateTimeField(default=datetime.datetime.now)
    last_login = db.DateTimeField()
    login_status = db.IntField(default=0)


class Position(db.Document):
    companyFullName = db.StringField(max_length=256)
    companyShortName = db.StringField(max_length=256)
    companyLabelList = db.StringField(max_length=256)
    companySize = db.StringField(max_length=256)
    financeStage = db.StringField(max_length=256)
    industryField = db.StringField(max_length=256)
    industryLables = db.StringField(max_length=256)
    positionName = db.StringField(max_length=256)
    salary = db.StringField(max_length=256)
    workYear = db.StringField(max_length=256)
    education = db.StringField(max_length=256)
    positionLables = db.StringField(max_length=256)
    jobNature = db.StringField(max_length=256)
    firstType = db.StringField(max_length=256)
    secondType = db.StringField(max_length=256)
    positionAdvantage = db.StringField(max_length=256)
    city = db.StringField(max_length=256)
    createdTime = db.StringField(max_length=256)
