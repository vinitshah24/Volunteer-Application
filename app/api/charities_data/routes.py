import json
import os
import sys

from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
import api.charities_data.models as charities_api

charities_data_blueprint = Blueprint('charities_data', __name__)
api = Api(charities_data_blueprint)


class APIList(Resource):
    def get(self):
        json_dir = os.path.join(os.path.dirname(__file__), 'data')
        file_path = os.path.join(json_dir, 'charities_data.json')
        # Check if file already exists or else call the api
        if not os.path.isfile(file_path):
            charities_api.getJsonDataByNC()
            print("Charities API was called!")
        print(os.path.isfile(file_path))
        if os.path.isfile(file_path):
            file = open(file_path)
            file_content = file.read()
            json_data = json.loads(file_content)
            file.close()
            return make_response(jsonify({'charities': json_data}), 200)
        else:
            return make_response("Internal Error occured!", 404)


api.add_resource(APIList, '/charities/NC')
