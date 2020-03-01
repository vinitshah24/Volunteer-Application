import json
import os

from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
import api.external_api.models as external_api

external_api_blueprint = Blueprint('external_api', __name__)
api = Api(external_api_blueprint)


class APIList(Resource):
    def get(self):
        json_data = external_api.getJsonDataByNC()
        if json_data:
            return make_response(jsonify(json_data, 200)
        else:
            return make_response("Internal Error occured", 404)

api.add_resource(APIList, '/poverty/NC')
