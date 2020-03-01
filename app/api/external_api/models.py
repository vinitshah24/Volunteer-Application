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
        return json.loads(response.text)
    else:
        return None


def filterByState(json_object, state):
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
    api_key = 'adeeb2c76d8bb84bbc115f84d23399d4'
    series_id = 'S1701ACS037179'
    api_url = 'https://api.stlouisfed.org/geofred/series/data'
    state = 'NC'
    json_output = fetchDataFromStLouisFed(api_key, api_url, series_id)
    print(json_output)
    nc_data = filterByState(json_output, state)
    print(nc_data)
    dict = {}
    dict['title'] = json_output['meta']['title']
    dict['units'] = json_output['meta']['units']
    dict['frequency'] = json_output['meta']['frequency']
    dict[state] = nc_data
    with open('nc_data_test.json', 'w', encoding='utf-8') as json_file:
        json.dump(dict, json_file, ensure_ascii=False, indent=2)


getJsonDataByNC()
