#forms.py should include a form for new posts requiring name and text.

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from ..models import User


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    comment = TextAreaField('Enter Text', validators=[Required()])
    submit = SubmitField('Submit')


class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Length(1,50)])
	password = PasswordField('Password', validators=[Required()])
	submit = SubmitField('Log In')

class RegisterForm(Form):
	username = StringField("User Name", validators=[Required(), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
																'Usernames must have only letters, '
																'numbers, dots or underscores')])

	email = StringField('Email', validators=[Required(), Email()])
	password = PasswordField('Password', validators=[Required(), EqualTo('verify', message='Passwords must match.')])
	verify = PasswordField('Retype Password', validators=[Required()])
	submit = SubmitField('Register')

#	def validate_email(self, field):
#		if User.query.filter_by(email=field.data).first():
#			raise ValidationError("Email already registered.")

#	def validate_username(self, field):
#		if User.query.filter.by(username=field.data).first():
#			raise ValidationError("Username already in use")