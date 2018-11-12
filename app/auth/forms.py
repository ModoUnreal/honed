# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm

# Import Form elements like TextField and BooleanField
from wtforms import TextField, PasswordField, StringField, BooleanField, SubmitField, TextAreaField

# Import Form validators
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from app.auth.models import User

# Define the login form (WTForms)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    password = PasswordField('Password', [
                DataRequired(message='You must provide a password. ;-')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    """Form for registering a new user."""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Used to validate a username, so that the username is unique."""
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username, this one is taken.')

    def validate_email(self, email):
        """Makes sure that the email is a proper email."""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

