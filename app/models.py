from app import mongo
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
