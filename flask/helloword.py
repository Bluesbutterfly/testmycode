from flask import Flask,url_for,request
app = Flask(__name__)
# 设置登录密令
app.config['SECRET_KEY'] = "mytoken"
@app.route("/")
def hello():
    return "hello Word！你好"
# 路由
@app.route("/index")
def index():
    return "this is index"
@app.route("/user/<username>")
def show_user_profile(username):
    return "user:%s" % username
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post:%s" % post_id
@app.route("/url/")
def get_url():
    return url_for("static",filename="css/style.css")
    # return url_for("show_post",post_id = 2)
@app.route("/login",methods=["POST","GET","PUT"])
def login():
  if request.method == "GET":
      return "这是GET请求"
  elif request.method == "POST":
      pass
  else:
      pass
if __name__ == "__main__":
    app.debug = True
    app.run()