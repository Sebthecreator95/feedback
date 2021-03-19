from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message='Username is required'), Length(min=6,max=20,message='Username must be between 6 - 20 characters')])
    password = PasswordField('Password', validators=[InputRequired(message='Password is Required')])
    email = StringField('Email', validators=[InputRequired(message='E-mail is Required'), Email(message='Please enter an Email')])
    first_name = StringField('First Name', validators=[InputRequired(message='Name  is Required'), Length(max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(message='Last Name Required'), Length(max=30)])


class LogInForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message='Enter Your Username')])
    password = PasswordField('Password', validators=[InputRequired(message='Enter Your Password')])


class FeedbackForm(FlaskForm):
    
    title = StringField("Title", validators=[InputRequired(message='Enter a title')])
    content = StringField("Title", validators=[InputRequired(message='Enter some content')])