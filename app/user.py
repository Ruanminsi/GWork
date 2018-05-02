from flask import Blueprint, render_template, redirect, request

user = Blueprint('user', __name__)


@user.route('/')
def hello_world():
	return render_template('user/login.html')
