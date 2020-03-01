import json
import os

from flask import request, jsonify, Blueprint, make_response
from flask_restful import Api, Resource
import api.external_api.models as external_api

external_api_blueprint = Blueprint('external_api', __name__)
api = Api(external_api_blueprint)


class APIList(Resource):
    def get(self):
        api_key = os.getenv('GEOFRED_API_KEY')
        series_id = 'S1701ACS037179'
        api_url = 'https://api.stlouisfed.org/geofred/series/data'
        json_output = external_api.fetchDataFromStLouisFed(
            api_key, api_url, series_id)
        if json_output:
            return make_response(jsonify({'poverty data': json_output}), 200)
        else:
            return make_response("Internal Error occured", 404)


api.add_resource(APIList, '/poverty')
