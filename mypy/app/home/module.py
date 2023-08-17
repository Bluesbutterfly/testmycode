from flask import Flask
import jwt
from datetime import datetime, timedelta
app = Flask(__name__)

# _app_ctx_stack.top
# _request_ctx_stack.top
# _app_ctx_stack()
# <LocalProxy unbound>
from flask import current_app
current_app

def generate_jwt(payload,expiry,secret=None):
    """
    生成jwt
    :param payload dict 载荷
    :param expiry datatime 有效期
    :param secret 盐
    :param 返回token
    """
    if "expiry" not in payload:
        payload["expiry"] = expiry
    if secret:
        secret = current_app.config["SECRET_KEY"]
    # 生成token jwt.encode
    token = jwt.encode(payload,secret,algorithm="HS256")
    return token
def verify_jwt(token,secret=None):
    """
    检验token
    :param token token值
    :param secret 盐
    :param payload 载荷
    """
    if not secret:
        secret = current_app.config["SECRET_KEY"]
    try:
        # 检验token
        payload = jwt.decode(token,secret,algorithms="HS256")
    except Exception as e:
        print("错误信息>>",e)
        # 检验失败返回None
        payload = None
    return payload
def _generate_token(user_id):
    """
    生成token
    :param user_id: 用户id
    :param 返回token
    """
    secret = current_app.config["SECRET_KEY"]
    # 定义过期时间 
    expiry = datetime.utcnow() + timedelta(hours=3)
    # 生成token 
    token = generate_jwt({"user_id":user_id},str(expiry),secret)
    return token