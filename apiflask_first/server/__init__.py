from apiflask import APIBlueprint


SERVER_BLUEPRINT = APIBlueprint("server_blueprint", __name__)

from . import routes