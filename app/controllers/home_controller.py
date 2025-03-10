from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models.users import User
from app.models.perro import Perro
from app.config.auth import login_manager

home_blueprint = Blueprint("home", __name__)


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(str(user_id))


@home_blueprint.route("/")
def home():
    return render_template("index.html")


@home_blueprint.route("/login")
def login():
    return render_template("login.html")


@home_blueprint.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@home_blueprint.route("/dashboard-admin")
def dashboard_admin():
    perros = Perro.query.all()
    return render_template("dashboard_admin.html", perros=perros)


@home_blueprint.route("/auth")
def auth():
    username = request.args.get("username")
    password = request.args.get("password")
    user = User.query.filter_by(username=username, password=password).first()

    if user:
        login_user(user)
        if user.is_admin:
            flash(f"Bienvenido {user.username}")
            return redirect(url_for("home.dashboard_admin"))
        flash(f"Bienvenido {user.username}")
        return redirect(url_for("home.dashboard"))

    flash("Las credenciales no estan registradas en el sistema", "error")
    return redirect(url_for("home.login"))


@home_blueprint.route("/auth/profile")
@login_required
def auth_profile():
    if current_user.is_admin:
        return f"datos: {current_user.id} - {current_user.username} - {current_user.email} - {current_user.password}"
    return f"datos: {current_user.id} - {current_user.username} - {current_user.email}"


@home_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home.login"))
