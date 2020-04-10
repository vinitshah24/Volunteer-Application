import os
from flask import jsonify
import requests
import json


def fetchDataFromStLouisFed(api_key, api_url, series_id):
    """Fetch API data"""
    metadata = {
        'api_key': api_key,
        'series_id': series_id,
        'file_type': 'json'
    }
    response = requests.get(url=api_url, params=metadata)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


def filterByState(json_object, state):
    """Filter JSON by State"""
    if json_object and state:
        data_list = json_object['meta']['data']['2018']
        json_data = []
        for index in range(len(data_list)):
            if state in data_list[index]['region']:
                json_data.append(data_list[index])
        return json_data
    else:
        return None


def getJsonDataByNC():
    """Get JSON data from NC State"""
    api_key = os.getenv('GEOFRED_API_KEY')
    series_id = 'S1701ACS037179'
    api_url = 'https://api.stlouisfed.org/geofred/series/data'
    state = 'NC'
    json_output = fetchDataFromStLouisFed(api_key, api_url, series_id)
    nc_data = filterByState(json_output, state)
    nc_dict = {}
    nc_dict['title'] = json_output['meta']['title']
    nc_dict['units'] = json_output['meta']['units']
    nc_dict['frequency'] = json_output['meta']['frequency']
    nc_dict[state] = nc_data
    json_dir = os.path.join(os.path.dirname(__file__), 'data')
    file_path = os.path.join(json_dir, 'nc_data.json')
    with open(file_path, 'w+', encoding='utf-8') as json_file:
        json.dump(nc_dict, json_file, ensure_ascii=False, indent=2)
