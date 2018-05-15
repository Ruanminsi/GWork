import re
from flask import Flask, render_template, request, session, jsonify, redirect,url_for
from flask_mongoengine import MongoEngine
from flask_babelex import Babel
import base64
import config

app = Flask(__name__)
app.config.from_object('config')
app.config['MONGODB_SETTINGS'] = {'DB': 'todos'}
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
db = MongoEngine(app)
babel = Babel(app)

@babel.localeselector
def get_locale():
	return session.get('lang', 'zh_Hans_CN')


@app.route('/')
def hello_world():
	return render_template('user/login.html')


@app.route('/register')
def userregister():
	''' 跳转注册页面 '''
	return render_template('user/register.html')


@app.route('/login')
def userLogin():
	''' 跳转登录页面 '''
	return render_template('user/login.html')


@app.route('/findPw')
def findPw():
	''' 跳转设置密码页面 '''
	return render_template('user/findPw.html')



@app.route('/searchall')
def userSearch():
	''' 跳转搜索页面 '''
	return render_template('user/searchall.html')

@app.route('/person')
def person():
	''' 跳转岗位搜索页面 '''
	return render_template('user/personCenter.html')


@app.route('/position')
def position():
	''' 跳转岗位搜索页面 '''
	return render_template('user/position.html')


@app.route('/vsearchall')
def uservSearch():
	''' 跳转搜索页面 '''
	return render_template('visitor/searchall.html')

@app.route('/visitor/report')
def vReport():
	''' 跳转搜索页面 '''
	return render_template('visitor/report.html')

@app.route('/visitor/position')
def vPosition():
	''' 跳转搜索页面 '''
	return render_template('visitor/position.html')

from app import models, views


@app.route('/report')
def userReport():
	''' 跳转报告页面 '''
	return render_template('user/report.html')


@app.route('/send', methods=["POST"])
def send():
	from app.models import Users
	from app.mail import mail
	if request.method == "POST":
		title = request.form.get('title', None)
		select = request.form.get('select', None)
		content = request.form.get('content', None)
	dr = re.compile(r'<[^>]+>', re.S)
	content = dr.sub('', content)
	if select == 0:
		select = "系统通知"
	else:
		select = "活动公告"
	users = Users.objects.all()
	for user in users:
		mail(title, select, content, user.name)
	return redirect(url_for('admin.index'))


@app.route('/login', methods=["POST"])
def login():
	from app.models import Users
	if request.method == "POST":
		username = request.form.get('username', None)
		password = request.form.get('password', None)
	bytesString = password.encode(encoding="utf-8")
	encodestr = base64.b64encode(bytesString).decode()  # 加密
	obj = Users.objects(name=username, password=encodestr).first()
	if obj is None:
		return jsonify({'result': False, 'reason': 'no exist',
		                'url': None})
	else:
		session['userid'] = obj.name
		import datetime
		Users.objects(name=obj.name).update(set__last_login=datetime.datetime.now(), login_status=1)
		return jsonify({'result': True, 'url': 'searchall'})


@app.route('/register', methods=['POST'])
def register():
	''' 注册 '''
	from app.models import Users
	if request.method == 'POST':
		username = request.form.get('username', None)
		password = request.form.get('password', None)
		nickname = request.form.get('nickname', None)

	obj = Users.objects(name=username).first()
	if obj is None:
		bytesString = password.encode(encoding="utf-8")
		encodestr = base64.b64encode(bytesString).decode()  # 加密
		decodestr = base64.b64decode(encodestr).decode()  # 解密
		Users(name=username, password=encodestr, nickname=nickname).save()
		return jsonify({'result': True, 'url': 'login'})
	else:
		return jsonify({'result': False, 'reason': '该邮箱已注册',
		                'url': None})


@app.route('/searchall', methods=['POST'])
def search():
	if request.method == 'POST':
		keyword = request.form.get('key', None)
		selects = request.form.get('select', None)
	if selects == '找分析':
		from app.operate import returnReport
		obj = returnReport(keyword)
		if obj is None:
			return jsonify({'result': False, 'detail': '系统尚未收录该信息，给您造成不便十分抱歉'})
		session["obj"] = obj
		return jsonify({'result': True, 'url': 'report'})
	else:
		from app.operate import getPositions
		session["keyword"] = keyword
		if getPositions(keyword) is None:
			return jsonify({'result': False, 'detail': '系统尚未收录该信息，给您造成不便十分抱歉'})
		return jsonify({'result': True, 'url': 'position'})


@app.route('/reportInfo', methods=['GET'])
def report():
	obj = session["obj"]
	print(obj)
	return jsonify({'result': True, 'detail': obj})


@app.route('/positionList', methods=['GET'])
def positionList():
	from app.operate import getPositions
	obj = {}
	keyword = session["keyword"]
	obj["pList"] = getPositions(keyword)
	return jsonify({'result': True, 'detail': obj})


@app.route('/positionDetail', methods=['POST'])
def positionDetail():
	if request.method == 'POST':
		name = request.form.get('name', None)
		pName = request.form.get('pName', None)
	from app.operate import getDetailrPosition
	obj = getDetailrPosition(name, pName)
	return jsonify({'result': True, 'detail': obj})


@app.route('/getCode', methods=['POST'])
def getCode():
	import random
	if request.method == 'POST':
		name = request.form.get('username', None)
	content = random.randint(100000, 999999)
	session['randomCode'] = content
	from app.operate import findPW
	result = findPW(content, name)
	if result is True:
		return jsonify({'result': True, 'detail': '验证码已发送'})
	else:
		return jsonify({'result': False, 'detail': '用户不存在'})


@app.route('/resetPw', methods=['POST'])
def resetPw():
	if request.method == 'POST':
		name = request.form.get('username', None)
		newPass = request.form.get('newPass', None)
		code = request.form.get('code', None)
	if int(code) != int(session["randomCode"]):
		return jsonify({'result': False, 'detail': "验证码错误"})
	else:
		from app.operate import setPw
		bytesString = newPass.encode(encoding="utf-8")
		encodestr = base64.b64encode(bytesString).decode()  # 加密
		setPw(name, encodestr)
		return jsonify({'result': True, 'url': 'login'})


@app.route('/getPerson', methods=['GET'])
def getPerson():
	name = session["userid"]
	from app.models import Users
	obj = Users.objects(name=name).first()
	return jsonify({'result': True, 'detail': obj})

@app.route('/setPerson', methods=['POST'])
def setPerson():
	''' 设置 '''
	from app.models import Users
	if request.method == 'POST':
		nickname = request.form.get('nickname', None)
		question = request.form.get('question', None)
		answer = request.form.get('answer', None)
	username = session["userid"]
	from app.operate import setPI
	setPI(username, nickname, question, answer)
	return jsonify({'result': True, 'detail': '保存成功'})
