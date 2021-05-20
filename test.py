import requests
from flask import jsonify

BASE = "http://127.0.0.1:5000/"

_locations = [[228, 0], [912, 0], [0, 80], [114, 80], [570, 160], [798, 160], [342, 240], [684, 240], [570, 400], [912, 400], [114, 480], [228, 480], [342, 560], [684, 560], [0, 640], [798, 640]]
_depot = [[456, 320]] # location 0 - the depot
_demands = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
_vehicle_cap = [15, 15, 15, 15]
_num_vehicles = 4

res = {"vCount" : _num_vehicles , "depot" : _depot , "locations" : _locations , "vCap" : _vehicle_cap}

import json

response = requests.post( BASE + "vrp" , json = res )
print( response.json() ) 