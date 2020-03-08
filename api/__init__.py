""" Register Blueprints """

from flask import Flask
from api.database import mysql

from api.users.routes import users_blueprint
from api.events.routes import events_blueprint
from api.rsvp.routes import rsvp_blueprint
from api.external_api.routes import external_api_blueprint


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    mysql.init_app(app)
    # Blueprints
    app.register_blueprint(users_blueprint, url_prefix='/api/v1/')
    app.register_blueprint(events_blueprint, url_prefix='/api/v1/')
    app.register_blueprint(rsvp_blueprint, url_prefix='/api/v1/')
    app.register_blueprint(external_api_blueprint, url_prefix='/api/v1/')
    return app
