from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models.perro import Perro

perro_blueprint = Blueprint("perro", __name__)

@perro_blueprint.route("/perros")
@login_required
def ver_perros():
    if current_user.is_admin:
        perros = Perro.query.all()
        return render_template("perros.html", perros=perros)
    else:
        flash(f"Hola, {current_user.username}. No tienes permisos para ver esta página.", "info")
        return redirect(url_for("home.dashboard"))
