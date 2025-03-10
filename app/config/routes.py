from app.controllers.home_controller import home_blueprint
from app.controllers.perro_controller import perro_blueprint

def register_routes(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(perro_blueprint)
    