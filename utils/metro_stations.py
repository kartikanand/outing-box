"""
    Responsible for creating list of metro stations from metro.json;
    Also exposes a metro station json object into global view
"""

import json
import os

metro_stations_list = []
metro_stations_dict = {}

file_path = os.path.join(os.path.dirname(__file__), 'metro.json') 

with open(file_path) as f:
    metro_stations_json = json.load(f)

    for station_dict in metro_stations_json:
        station_name = station_dict['name']
        
        metro_stations_list.append((station_name, station_name))
        metro_stations_dict[station_name] = station_dict['details']
