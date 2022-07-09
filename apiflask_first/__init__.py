from apiflask import APIFlask

from apiflask_first.database import DB
from datetime import timedelta

def create_app() -> APIFlask:
    app = APIFlask(__name__)
    app.config.from_object("config.Config")
    app.permanent_session_lifetime = timedelta(minutes=30)

    from .server import SERVER_BLUEPRINT
    app.register_blueprint(SERVER_BLUEPRINT)

    DB.init_app(app)
    with app.app_context():
        DB.create_all()

    return app

