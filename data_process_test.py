import json

def get_tag():
	with open("resources/restaurants.json") as f:
		data = json.load(f)
		for r in data["restaurants"]:
			print(r['name'])

get_tag()