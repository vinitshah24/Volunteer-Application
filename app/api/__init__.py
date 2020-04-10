""" Register Blueprints """

from flask import Flask
from api.database import mysql

from api.users.routes import users_blueprint
from api.events.routes import events_blueprint
from api.poverty_data.routes import poverty_data_blueprint
from api.charities_data.routes import charities_data_blueprint


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    mysql.init_app(app)
    # Blueprints
    app.register_blueprint(users_blueprint, url_prefix='/api/v1/')
    app.register_blueprint(events_blueprint, url_prefix='/api/v1/')
    app.register_blueprint(poverty_data_blueprint, url_prefix='/api/v1/')
    app.register_blueprint(charities_data_blueprint, url_prefix='/api/v1/')

    return app
