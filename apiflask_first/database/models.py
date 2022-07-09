from . import DB


class Footboolers(DB.Model):
    id_ = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(20))
    surname = DB.Column(DB.String(20))



