from apiflask import APIFlask

from apiflask_first.database import DB


def create_app() -> APIFlask:
    app = APIFlask(__name__)
    app.config.from_object("config.Config")

    from .server import SERVER_BLUEPRINT
    app.register_blueprint(SERVER_BLUEPRINT)

    DB.init_app(app)
    with app.app_context():
        DB.create_all()

    return app

