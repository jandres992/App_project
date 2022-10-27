from flask import Flask
from .config import config
from .personas import person


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['db'])
    app.register_blueprint(person)

    return app
