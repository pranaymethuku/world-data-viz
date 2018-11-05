import json
import pandas as pd

countries_csv = pd.read_csv('./csv-data/countries_of_the_world.csv')
countries_csv = countries_csv.Country
countries_csv_list = [country.strip() for country in countries_csv.unique()]

countries_json = json.load(open('./geo-json-data/world-countries.json', 'r+'))
countries_json_list = []
for feature in countries_json['features']:
  countries_json_list.append(str(feature['properties']['name']))

extra_json = list(set(countries_json_list) - set(countries_csv_list))
extra_csv = list((set(countries_csv_list) - set(countries_json_list)))
print(sorted(extra_json))
print(sorted(extra_csv))
