from flask import Flask, request, session, Response
# import pymysql
import datetime
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.home.module import _generate_token, verify_jwt


app = Flask(__name__)
CORS(app,supports_credentials=True)
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'user'
USERNAME = 'root'
PASSWORD = 'welcome123'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '1315as4dvf45das8eq5as3215z5asq'
db = SQLAlchemy()
db.init_app(app)

response = Response("set cookie")

class User(db.Model):
    __tablename__ = "usermsg"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(80))
    emain = db.Column(db.String(80))
    telphone = db.Column(db.Integer)
    userName = db.Column(db.String(80), unique=True, nullable=False)
    nickName = db.Column(db.String(80))
    identityCard = db.Column(db.Integer)
    password = db.Column(db.String(80), nullable=False)
    publish_time = db.Column(db.DateTime,default=datetime.datetime.now,onupdate=datetime.datetime.now)
    downline_time = db.Column(db.DateTime,default=datetime.datetime.now,onupdate=datetime.datetime.now)
# def create_app(config_name):
#     app = Flask(__name__)
#     # app.config.from_object(config[config_name])
#     # config[config_name].init_app(app)
#     # db.init_app(app)
#     # 注册蓝图
#     from app.home import home as home_blueprint
#     from app.admin import admin as admin_blueprint
#     app.register_blueprint(home_blueprint)
#     app.register_blueprint(admin_blueprint,url_prefix="admin")
#     return app
@app.route("/register",methods=["GET","POST"],strict_slashes=False)
# @cross_origin()
def register():
    """注册接口"""
    if request.method == "POST":
        """
        接收表单数据
        并进行表单验证
        """
        userName = request.json.get('account')
        emain = request.json.get('email')
        nickName = request.json.get('nickName')
        identityCard = 1333333333
        telphone = request.json.get('telphone')
        password = request.json.get('password')
        name = '名称'
        """
        查找全局数据表查看是否有重复用户名
        如果有重复用户名
        返回错误信息告知用户名用户名已被注册
        如果没有用户名重复则注册用户
        """
        user = User.query.all()
        for item in user:
            if item.userName == userName:
                return {'code':200,'data':'注册成功','message':'用户名已被注册，请重新填写用户名！'}
            else:
                new_user = User(userName=userName,password=password,emain=emain,nickName=nickName,telphone=telphone,identityCard=identityCard,name=name)
                db.session.add(new_user)
                db.session.commit()
                return {'code':200,'data':'注册成功','message':'注册成功'}
@app.route("/login",methods=["GET","POST"],strict_slashes=False)
def login():
    """登录接口"""
    if request.method == "POST":
        userName = request.json.get('account')
        password = request.json.get('password')
        user = User.query.all()
        for item in user:
            if item.userName == userName:
                # 如果存在用户名
                if item.password == password:
                    access_token = _generate_token(item.id)
                    usermessage = {
                        'token':access_token
                    }
                    # session.permanent = True
                    session["token"] = access_token
                    # response.set_cookie("token",access_token)
                    # resp.set_cookie('username', 'the username')
                    return {'code':200,'data':usermessage,'message':'登录成功'}
                else:
                    return {'code':205,'data':'登录失败','message':'用户密码不正确'}
            else:
                return {'code':205,'data':'登录失败','message':'用户名不存在'}
        
@app.route("/logout",methods=["GET","POST"],strict_slashes=False)
def logout():
    """注销登录"""
    if request.method == "GET":
        session.clear()
        # response.delete_cookie("token")
        return {'code':200,'data':'注销成功','message':'注销成功'}
@app.route("/userStatus",methods=["GET"],strict_slashes=False)
def userStatus():
    """获取登录状态"""
    if request.method == "GET":
        loginstatus = session.get("token")
        headers = request.headers
        token = ''
        param = {}
        for key,value in headers:
            if key == 'Authorization':
                token = value.split('Bearer ')[1]
        # print('*'*3,headers['Authorization'])
        if token:
            trans = verify_jwt(token,app.config['SECRET_KEY'])
            # print("token是否还有效",verify_jwt(token,app.config['SECRET_KEY']))
            """
            判断存的token是否有效
            cookies是否在有效期
            """
            if trans:
                """
                判断后端服务器是否在登录状态
                如果在登录状态证明在登录
                如果不在登录状态则说明已经退出登录
                """
                if loginstatus:
                    user = User.query.all()
                    for item in user:
                        if item.id == trans['user_id']:
                            param['userName'] = item.userName
                            param['telphone'] = item.telphone
                            param['nickName'] = item.nickName
                    return {'code':200,'data':param,'message':'成功'}
                else:
                    return {'code':205,'data':None,'message':'用户已经退出登录'}
            else:
                return {'code':205,'data':None,'message':'token已经不在有效期内'}
        else:
            return {'code':205,'data':None,'message':'未登录'}
class user:
    def __init__(self) -> None:
      self.time =''
    def run():
        # db.create_all()
        host = "127.0.0.1"
        port = 5000
        # ser = pywsgi.WSGIServer(('0.0.0.0',5000),app)
        # ser.serve_forever()
        app.debug = True
        app.run(host=host,port=port)