from os import getenv

from apiflask_first.database.models import DB, Footboolers
from apiflask_first.database.serializers import FootboolerInSchema, FootboolerOutSchema
from . import SERVER_BLUEPRINT
from apiflask import HTTPTokenAuth
from dotenv import load_dotenv

# wapiflasku nie uzywamy formularzy !!!
# Update, Delete

# @SERVER_BLUEPRINT.patch
# /show_all_footbooller/ Najpierw RZECZOWNIK potem CZASOWNIK

load_dotenv()
admin_token = HTTPTokenAuth(getenv("ADMIN_TOKEN", "zapasowy"))
user_token = HTTPTokenAuth()


# @SERVER_BLUEPRINT.get("/")  # STRONA startowa
# def home():
#     return {"msg": "Welcome to my app!!!!"}
#
#
# @SERVER_BLUEPRINT.auth_required(auth=user_token)  # zapytac Kacpra jak ukryc admin tokena
# @SERVER_BLUEPRINT.get("/footboller/<int:id_>")
# @SERVER_BLUEPRINT.output(FootboolerOutSchema)
# def get_footboller(id_: int):
#     return Footboolers.query.filter_by(id_=id_).first()
#
#
# @SERVER_BLUEPRINT.auth_required(auth=user_token)
# @SERVER_BLUEPRINT.post("/footboller/add")
# @SERVER_BLUEPRINT.input(FootboolerInSchema)
# def add_new_footboller(data):
#     DB.session.add(Footboolers(**data))
#     DB.session.commit()
#     return {"msg": "Created new footballer"}
#
#
# @SERVER_BLUEPRINT.get("/show_all_footbooller/")
# @SERVER_BLUEPRINT.output(FootboolerOutSchema(many=True))
# def show_all_footbollers():
#     return Footboolers.query.all()
#
#
# # zrobic update czyli patch
# # wymysl sposob jak zlimitowac ilosc pol do update - tylko - update(name) (parametr only albo exclude)
# @SERVER_BLUEPRINT.patch("/footbooller/update/<int:id_>")
# @SERVER_BLUEPRINT.input(FootboolerInSchema(only=["name"]))
# @SERVER_BLUEPRINT.output(FootboolerOutSchema)
# def update_footboller(id_: int, data):
#     found_footboller = Footboolers.query.get(id_)
#     found_footboller.name = data["name"]
#     DB.session.commit()
#
#     return {"msg": "Updated footballer"}
#
#
# # zrobic delete
# @SERVER_BLUEPRINT.delete("/footbooller/delete/<int:id_>")
# @SERVER_BLUEPRINT.auth_required(auth=admin_token)
# @SERVER_BLUEPRINT.output(FootboolerOutSchema())
# # @SERVER_BLUEPRINT.auth_required(role="admin")
# def delete_footboller(id_: int):
#     footboller_to_delete = Footboolers.query.filter_by(id_=id_).first()
#     if footboller_to_delete:
#         DB.session.delete(footboller_to_delete)
#         DB.session.commit()
#     else:
#         print("None")


@SERVER_BLUEPRINT.route("/footbooller/<int:id_>")
class Footboller:

    # decorators = [SERVER_BLUEPRINT.auth_required(token)]
    @SERVER_BLUEPRINT.get("/")  # STRONA startowa
    def home(self):
        return {"msg":"Welcome to my app!!!"}

    @SERVER_BLUEPRINT.output(FootboolerOutSchema)
    def get(self, id_:int):
        return Footboolers.query.filter_by(id_=id_).first()

    @SERVER_BLUEPRINT.input(FootboolerInSchema)
    def post(self, data):
        DB.session.add(Footboolers(**data))
        DB.session.commit()
        return {"msg": "Created new footballer"}

    @SERVER_BLUEPRINT.output(FootboolerOutSchema(many=True))
    def show_all_footboolers(self):
        return Footboolers.query.all()

    @SERVER_BLUEPRINT.input(FootboolerInSchema(only=["name"]))
    @SERVER_BLUEPRINT.output(FootboolerOutSchema)
    def patch(self, id_, data):
        found_footboller = Footboolers.query.get(id_)
        found_footboller.name = data["name"]
        DB.session.commit()

    @SERVER_BLUEPRINT.output(FootboolerOutSchema())
    def delete(self, id_):
        footboller_to_delete = Footboolers.query.filter_by(id_=id_).first()
        if footboller_to_delete:
            DB.session.delete(footboller_to_delete)
            DB.session.commit()
        else:
             print("None")