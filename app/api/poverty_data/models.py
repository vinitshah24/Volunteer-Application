from flask import jsonify
from pandas import json_normalize
import pandas as pd
import requests
import json
import os


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
    """Get North Carolina Counties JSON data"""
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


def merge_coorrdinates_data(api_filename, coordinates_filename, output_filename):
    """Merging co-ordinates for NC counties"""
    if api_filename and coordinates_filename and output_filename:
        json_dir = os.path.join(os.path.dirname(__file__), 'data')
        nc_api = os.path.join(json_dir, api_filename)
        nc_coordinates = os.path.join(json_dir, coordinates_filename)
        output = os.path.join(json_dir, output_filename)

        api_f = open(nc_api, 'r', encoding='utf-8')
        api_data = api_f.read()
        nc_json = json.loads(api_data)
        df1 = json_normalize(nc_json['NC'])
        # print(df1.head(3))

        coordinates_f = open(nc_coordinates, 'r', encoding='utf-8')
        coordinates_data = coordinates_f.read()
        coordinates_json = json.loads(coordinates_data)
        df2 = pd.DataFrame.from_dict(coordinates_json, orient='index')
        df2.reset_index(level=0, inplace=True)
        # print(df2.head(3))

        merged_df = pd.merge(
            df1, df2[['index', 'lat', 'lng']], how='left', left_on='code', right_on='index')
        merged_df.drop(columns=['index'], inplace=True)
        # print(merged_df)
        merged_df.to_json(output, orient='records')
    else:
        print('Required Parameters are not satisfied!')
