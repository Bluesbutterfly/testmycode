from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
   name = StringField(label='用户名',validators=[DataRequired("用户名不能为空"),Length(min=4,max=20)])
   password = PasswordField(label='密码',validators=[DataRequired("密码不能为空")])
   submit = SubmitField(label='提交')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myscript'

@app.route("/",methods=["GET","POST"])
def index():
  form = LoginForm()
  form.validate()
  data = {}
  if form.validate_on_submit():
     data['name'] = form.name.data
     data['password'] = form.password.data
  return render_template("login.html",form=form,data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()