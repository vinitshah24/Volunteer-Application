import pandas as pd
import os
import json
from pandas import json_normalize


def merge_coorrdinates_data(api_filename, coordinates_filename, output_filename):
    if api_filename and coordinates_filename and output_filename:
        json_dir = os.path.join(os.path.dirname(__file__), 'data')
        nc_api = os.path.join(json_dir, api_filename)
        nc_coordinates = os.path.join(json_dir, coordinates_filename)
        output = os.path.join(json_dir, output_filename)

        api_f = open(nc_api, 'r', encoding='utf-8')
        api_data = api_f.read()
        nc_json = json.loads(api_data)
        df1 = json_normalize(nc_json['NC'])
        #print(df1.head(3))

        coordinates_f = open(nc_coordinates, 'r', encoding='utf-8')
        coordinates_data = coordinates_f.read()
        coordinates_json = json.loads(coordinates_data)
        df2 = pd.DataFrame.from_dict(coordinates_json, orient='index')
        df2.reset_index(level=0, inplace=True)
        #print(df2.head(3))

        merged_df = pd.merge(
            df1, df2[['index', 'lat', 'lng']], how='left', left_on='code', right_on='index')
        merged_df.drop(columns=['index'], inplace=True)
        #print(merged_df)
        merged_df.to_json(output, orient='records')
    else:
        print('Required Parameters are not satisfied!')

merge_coorrdinates_data('nc_data.json', 'counties.json', 'output.json')
