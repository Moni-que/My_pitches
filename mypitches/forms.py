from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired,Length,Email, EqualTo,ValidationError
from mypitches.models import User
from flask_login import current_user

class RegisterForm(FlaskForm):
    username = StringField('Username', validaters = [InputRequired(),Length(min = 5, max = 20)])
    email = StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    password_confirm = PasswordField('confirm password', validators = [InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user :
            raise ValidationError('username unavailable')


    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user :
            raise ValidationError('email unavailable')


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validaters = [InputRequired(),Length(min = 5, max = 20)])
    email = StringField('Email', validators = [InputRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user :
                raise ValidationError('username unavailable')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user :
                raise ValidationError('email unavailable')