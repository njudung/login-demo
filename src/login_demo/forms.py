from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    login = SubmitField("Login")


class RegistrationForm(FlaskForm):
    email = StringField("E-mail", validators=[InputRequired(), Email()])
    password = PasswordField(
        "Password", validators=[InputRequired(), EqualTo("password2", message="Passwords must be equal.")]
    )
    password2 = PasswordField("Password confirmation")
    register = SubmitField("Register")
