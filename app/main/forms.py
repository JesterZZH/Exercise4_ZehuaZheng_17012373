from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email


class SignupForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    email_address = StringField('Email Address:', validators=[DataRequired(), Email(message='Valid email address required')])
    password = PasswordField('Password:',validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Repeat Password:')
    submit = SubmitField('Sign Up')