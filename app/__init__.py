from flask import Flask
from .personas import person


def create_app():
    app = Flask(__name__)
    app.register_blueprint(person)

    return app
