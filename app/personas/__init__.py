import types
from flask import Blueprint
from app.decorators import class_route

person = Blueprint("persona", __name__, url_prefix="/persona", template_folder="")
person.class_route = types.MethodType(class_route, person)

from .views import PersonView
