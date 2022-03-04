from flask import render_template, current_app, redirect, url_for, flash, abort
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from login_demo import app, db
from login_demo.models import User
from .forms import LoginForm, RegistrationForm


logger = app.logger


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admin")
@login_required
def admin():
    users = User.query.all()
    return render_template("admin.html", users=users)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        logger.debug(user)

        if user is not None:
            # Kontrollera lösenord
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                logger.debug("Inloggad!")
                flash(f"Välkommen {user.email}!", "notice")
                return redirect(url_for("admin"))
            else:
                flash(f"Du kunde visst inte lösenordet!", "error")

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Du är nu utloggad.", "notice")
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        logger.info(f"Created user with email: {user.email}")

        return redirect(url_for("index"))

    return render_template("register.html", form=form)
