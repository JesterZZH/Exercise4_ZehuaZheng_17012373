from flask_wtf import FlaskForm

from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError

from app.models import User


class SignupForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    email = StringField('Email Address:',
                        validators=[DataRequired(), Email(message='Valid email address required')])
    password = PasswordField('Password:',
                             validators=[DataRequired(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Repeat Password:')
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(
                'An account is already registered for that email address. Please use a different email address.')
