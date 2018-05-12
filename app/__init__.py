from flask import Flask, render_template, request, session, jsonify
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


@app.route('/admin/login')
def index():
	return render_template('admin/login.html')


@app.route('/')
def hello_world():
	# names = mongo.db.users.find().limit(5)
	# print(names)
	# from app.models import Users
	# user = Users(name="test-0", password="000")
	# user.save()

	return render_template('user/login.html')


@app.route('/register')
def userregister():
	''' 跳转注册页面 '''
	return render_template('user/register.html')


@app.route('/login')
def userLogin():
	''' 跳转登录页面 '''
	return render_template('user/login.html')


@app.route('/searchall')
def userSearch():
	''' 跳转搜索页面 '''
	return render_template('user/searchall.html')


@app.route('/position')
def position():
	''' 跳转岗位搜索页面 '''
	return render_template('user/position.html')


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
	print(type(content))
	i = str(title) + str(select) + content
	if select == 0:
		select = "系统通知"
	else:
		select = "活动公告"
	users = Users.objects.all()
	for user in users:
		mail(title, select, content, user.name)
	return jsonify({'result': i, 'reason': 'no exist'})


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
		from app.test import returnReport
		obj = returnReport(keyword)
		session["obj"] = obj
		return jsonify({'result': True, 'url': 'report'})
	else:
		from app.test import getPositions
		session["keyword"] = keyword
		return jsonify({'result': True, 'url': 'position'})


@app.route('/reportInfo', methods=['GET'])
def report():
	obj = session["obj"]
	print(obj)
	return jsonify({'result': True, 'detail': obj})


@app.route('/positionList', methods=['GET'])
def positionList():
	from app.test import getPositions
	obj = {}
	keyword = session["keyword"]
	obj["pList"] = getPositions(keyword)
	print(type(obj))
	return jsonify({'result': True, 'detail': obj})
