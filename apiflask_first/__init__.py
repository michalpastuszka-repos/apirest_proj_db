from apiflask import APIFlask

from apiflask_first.database import DB
from dotenv import load_dotenv

def create_app() -> APIFlask:
    app = APIFlask(__name__)
    app.config.from_object("config.Config")

    from .server import SERVER_BLUEPRINT
    app.register_blueprint(SERVER_BLUEPRINT)
    load_dotenv()
    DB.init_app(app)
    with app.app_context():
        DB.create_all()

    return app

