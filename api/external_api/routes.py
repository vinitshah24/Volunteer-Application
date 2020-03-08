import json
import os
import sys

from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
import api.external_api.models as external_api

external_api_blueprint = Blueprint('external_api', __name__)
api = Api(external_api_blueprint)


class APIList(Resource):
    def get(self):
        json_dir = os.path.join(os.path.dirname(__file__), 'data')
        file_path = os.path.join(json_dir, 'nc_data.json')
        # Check if file already exists or else call the api
        if not os.path.isfile(file_path):
            external_api.getJsonDataByNC()
            print("External API was called!")
        if os.path.isfile(file_path):
            file = open(file_path)
            file_content = file.read()
            json_data = json.loads(file_content)
            file.close()
            return make_response(jsonify(json_data), 200)
        else:
            return make_response("Internal Error occured!", 404)


api.add_resource(APIList, '/poverty/NC')
