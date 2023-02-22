from wtforms import Form,StringField, TextAreaField, PasswordField, SubmitField, validators, ValidationError
from flask_wtf import FlaskForm
from .models import Register

class CustomerRegisterForm(FlaskForm):
    name= StringField('Name: ')
    username = StringField('Username: ',[validators.DataRequired()])
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ',[validators.DataRequired(), validators.EqualTo('confirm',message=' Both password must match ')])
    confirm = PasswordField('Repeat Password: ',[validators.DataRequired()])
    submit =SubmitField('Register')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("This username is already in use")

    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("This email is already in use")



class CustomerLoginForm(FlaskForm):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ',[validators.DataRequired()])


