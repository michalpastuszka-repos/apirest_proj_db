from apiflask import APIBlueprint
from dotenv import load_dotenv
load_dotenv()
SERVER_BLUEPRINT = APIBlueprint("server_blueprint", __name__)

from . import routes