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
    login = db.DateTimeField()


# class Position(db.Document):
