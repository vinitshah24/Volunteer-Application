"""Script for transforming JSON data"""

import json
import os
import pandas as pd
from pandas import json_normalize

json_dir = os.path.join(os.path.dirname(__file__), 'data')
file_path = os.path.join(json_dir, 'nc_data.json')
file = open(file_path)
file_content = file.read()
file.close()
json_data = json.loads(file_content)

"""
region,percent = [],[]
for data in json_data['NC']:
    region.append(data['region'])
    percent.append(data['value'])
df = pd.DataFrame([region, percent]).T
"""

df = json_normalize(json_data['NC'])

# Hard Conversions
df["code"] = pd.to_numeric(df["code"])
df["value"] = pd.to_numeric(df["value"])

# df['code'] = df['code'].astype('int')
# df['value'] = df['value'].astype('float')
# print(df.dtypes)

# Sort by poverty percentages
sort_by_percent = df.sort_values(by='value', ascending=True)
print(sort_by_percent)

# Top 10 poorest counties in NC
poorest_counties = df.nlargest(10, 'value')
print(poorest_counties)

# Top 10 richest counties in NC
richest_counties = df.nsmallest(10, 'value')
print(richest_counties)

# Export transformations to JSON file
output_path = os.path.join(json_dir, 'output_data.json')
poorest_counties.to_json(output_path, orient='records')
