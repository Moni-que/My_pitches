from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired,Length,Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validaters = [InputRequired(),Length(min = 5, max = 20)])
    email = StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    password_confirm = PasswordField('confirm password', validators = [InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')