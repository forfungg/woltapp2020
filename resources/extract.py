import json
from random import random

result = dict()
tags = list()
with open("resources/restaurants.json") as f:
	data = json.load(f)
	for r in data['restaurants']:
		for t in r['tags']:
			if t not in tags:
				tags.append(t)


result['tags'] = tags


#generate random locations from a rectangle between
## Suomenlinna 24.980731, 60.144508
## Meilahden tornisairaala 24.900245, 60.191783
## Around 7km diagonally
s_lon = 24.980731
s_lat = 60.144508
e_lon = 24.900245
e_lat = 60.191783
lon_delta = s_lon - e_lon
lat_delta = s_lat - e_lat

locations = list()
for n in range(100):
	rlon = (lon_delta * random()) + e_lon
	rlat = (lat_delta * random()) + e_lat
	locations.append([rlon, rlat])

result['locations'] = locations
with open('resources/test_requests.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)