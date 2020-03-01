import sys
import requests
import json
import os


def fetchDataFromStLouisFed(api_key, api_url, series_id):
    metadata = {
        'api_key': api_key,
        'series_id': series_id,
        'file_type': 'json'
    }
    response = requests.get(url=api_url, params=metadata)
    if response.status_code == 200:
        json_object = json.loads(response.text)
        data_list = json_object['meta']['data']['2018']
        json_data = []
        for index in range(len(data_list)):
            if 'NC' in data_list[index]['region']:
                json_data.append(data_list[index])
        return json_data
    else:
        return None
