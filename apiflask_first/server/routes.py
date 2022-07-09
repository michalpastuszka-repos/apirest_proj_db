from apiflask_first.database.models import DB, Footboolers
from apiflask_first.database.serializers import FootboolerInSchema, FootboolerOutSchema
from . import SERVER_BLUEPRINT
from apiflask import HTTPTokenAuth
# wapiflasku nie uzywamy formularzy !!!
# Update, Delete

# @SERVER_BLUEPRINT.patch
#/show_all_footbooller/ Najpierw RZECZOWNIK potem CZASOWNIK

admin_token = HTTPTokenAuth("1234")
user_token = HTTPTokenAuth()

@SERVER_BLUEPRINT.get("/")#STRONA startowa
def home():
    return {"msg": "Welcome to my app!"}

@SERVER_BLUEPRINT.auth_required(auth=user_token)
@SERVER_BLUEPRINT.get("/footboller/<int:id_>")
@SERVER_BLUEPRINT.output(FootboolerOutSchema)
def get_footboller(id_: int):
    return Footboolers.query.filter_by(id_=id_).first()

@SERVER_BLUEPRINT.auth_required(auth=user_token)
@SERVER_BLUEPRINT.post("/footboller/add")
@SERVER_BLUEPRINT.input(FootboolerInSchema)
def add_new_footboller(data):
    DB.session.add(Footboolers(**data))
    DB.session.commit()
    return {"msg": "Created new footballer"}

@SERVER_BLUEPRINT.get("/show_all_footbooller/")
@SERVER_BLUEPRINT.output(FootboolerOutSchema(many=True))
def show_all_footbollers():
    return Footboolers.query.all()

#zrobic update czyli patch
#wymysl sposob jak zlimitowac ilosc pol do update - tylko - update(name) (parametr only albo exclude)
@SERVER_BLUEPRINT.patch("/footbooller/update/<int:id_>")
@SERVER_BLUEPRINT.input(FootboolerInSchema(only=["name"]))
@SERVER_BLUEPRINT.output(FootboolerOutSchema)
def update_footboller(id_: int, data):
    found_footboller = Footboolers.query.get(id_)
    found_footboller.name = data["name"]
    DB.session.commit()

    return {"msg": "Updated footballer"}

# zrobic delete
@SERVER_BLUEPRINT.delete("/footbooller/delete/<int:id_>")
@SERVER_BLUEPRINT.auth_required(auth=admin_token)
@SERVER_BLUEPRINT.output(FootboolerOutSchema())
#@SERVER_BLUEPRINT.auth_required(role="admin")
def delete_footboller(id_: int):
    footboller_to_delete = Footboolers.query.filter_by(id_=id_).first()
    if footboller_to_delete:
        DB.session.delete(footboller_to_delete)
        DB.session.commit()
    else:
        print("None")
