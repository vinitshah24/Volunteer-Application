import json
import os
import sys

from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
import api.poverty_data.models as poverty_data

poverty_data_blueprint = Blueprint('poverty_data', __name__)
api = Api(poverty_data_blueprint)


class APIList(Resource):
    def get(self):
        json_dir = os.path.join(os.path.dirname(__file__), 'data')
        file_path = os.path.join(json_dir, 'nc_data.json')
        # Check if file already exists or else call the api
        if not os.path.isfile(file_path):
            poverty_data.getJsonDataByNC()
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
