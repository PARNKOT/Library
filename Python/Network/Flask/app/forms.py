from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    user = StringField("user", validators=[DataRequired()], default="Логин")
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    commit = SubmitField("Submit")


class ContactForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    #email = StringField("Email: ", validators=[Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")