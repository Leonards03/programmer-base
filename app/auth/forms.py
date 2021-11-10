from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField, EmailField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', id='username', validators=[DataRequired()])
    password = PasswordField('Password', id='password', validators=[DataRequired()])
    remember = BooleanField('Remember me')

class CreateAccountForm(FlaskForm):
    username = StringField('Username', id='username', validators=[DataRequired()])
    email = EmailField('Email', id='email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', id='confirm_password', validators=[DataRequired(), EqualTo('password', message='Confirmation password must match password')])
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    title = StringField('Title', id='title', validators=[DataRequired()])
    content = StringField('Content', id='content', validators=[DataRequired()])

    