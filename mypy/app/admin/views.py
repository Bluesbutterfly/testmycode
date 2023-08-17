from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'myscript'
@app.route("/",methods=["GET","POST"])

def login():
    """登录"""
    form = LoginForm()