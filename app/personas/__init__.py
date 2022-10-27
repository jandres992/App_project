import types
from flask import Blueprint
from app.decorators import class_route

person = Blueprint("ws", __name__, url_prefix="/ws", template_folder="")
person.class_route = types.MethodType(class_route, person)


from .views import PersonView
