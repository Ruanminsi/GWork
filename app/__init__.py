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
    ''' 跳转注册页面 '''
    return render_template('user/login.html')

@app.route('/searchall')
def userSearch():
    ''' 跳转注册页面 '''
    return render_template('user/searchall.html')
from app import models, views


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
        return jsonify({'result': True, 'url': 'searchall'})
        # Users(username=username, password=encodepassword).save()


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
        encodestr = base64.b64encode(bytesString).decode()  #加密
        decodestr = base64.b64decode(encodestr).decode()    #解密
        Users(name=username, password=encodestr, nickname=nickname).save()
        return jsonify({'result': True, 'url': 'login'})
    else:
        return jsonify({'result': False, 'reason': '该邮箱已注册',
                        'url': None})


@app.route('/searchall', methods=['POST'])
def search():
	if request.method == 'POST':
		key = request.form.get('key', None)
		select = request.form.get('select', None)
	if select == '找分析':
		return jsonify({'result': True, 'url': 'login'})
	else:
		return jsonify({'result': True, 'url': 'register'})


@app.route('/report', methods=['POST'])
def report():
	pass


@app.route('/report', methods=['POST'])
def report():
	pass

