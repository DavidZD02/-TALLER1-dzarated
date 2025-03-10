from flask import Flask
from app.config.db import db
from app.config.auth import login_manager
from app.config.routes import register_routes


def create_app(config):
    app = Flask(__name__, template_folder="views")

    app.config.from_object(config)
    db.init_app(app)
    login_manager.init_app(app)
    register_routes(app)

    with app.app_context():
        db.create_all()

    return app
