import os
from flask import jsonify
import requests
import json


def fetchData(api_url, app_id, app_key, pageSize, rated, state):
    """Fetch API data"""
    metadata = {
        'app_id': app_id,
        'app_key': app_key,
        'pageSize': pageSize,
        'rated': rated,
        'state': state,
        'file_type': 'json'
    }
    response = requests.get(url=api_url, params=metadata)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None


def getJsonDataByNC():
    """Get JSON data from NC [state]"""
    app_key = os.getenv('CHARITY_API_KEY')
    app_id = '76041238'
    api_url = 'https://api.data.charitynavigator.org/v2/Organizations'
    pageSize = '10'
    rated = 'TRUE'
    state = 'NC'
    json_output = fetchData(api_url, app_id, app_key, pageSize, rated, state)
    output = []
    for index in range(len(json_output)):
        json_dict = {}
        json_dict['charityName'] = json_output[index]['charityName']
        json_dict['rating'] = json_output[index]['currentRating']['rating']
        json_dict['category'] = json_output[index]['category']['categoryName']
        json_dict['cause'] = json_output[index]['cause']['causeName']
        output.append(json_dict)
    print(output)
    json_dir = os.path.join(os.path.dirname(__file__), 'data')
    file_path = os.path.join(json_dir, 'charities_data.json')
    with open(file_path, 'w+', encoding='utf-8') as json_file:
        json.dump(output, json_file, ensure_ascii=False, indent=2)
