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

@app.route('/registerx')
def userregisterx():
    ''' 跳转注册页面 '''
    return render_template('admin/register.html')

from app import models, views


@app.route('/login', methods=["POST"])
def login():
    from app.models import Users
    if request.method == "POST":
        username = request.form.get('username', None)
        password = request.form.get('password', None)

    obj = Users.objects(name=username, password=password).first()
    if obj is None:
        return jsonify({'result': False, 'reason': 'no exist',
                 'url': None})
    else:
        session['userid'] = obj.name
        return jsonify({'result': True, 'url': 'user/index'})
        # Users(username=username, password=encodepassword).save()

# @app.route('/register', methods=['POST'])
# def register():
#     ''' 注册 '''
#     if request.method == 'POST':
#         p_username = request.form.get('username', None)
#         p_password = request.form.get('password', None)
#
#
#     if result is True:
#         from app.core.calculate.logtimeset import uregister
#         uregister(p_username, p_password)
#         return jsonify({'result': True, 'url': 'login'})
#     else:
#         return jsonify({'result': False, 'reason': '名称被占领了',
#                         'url': None})
