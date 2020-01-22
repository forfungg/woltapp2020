from flask import Flask, jsonify, request
import json
from srcs.get_range import get_distance
app = Flask(__name__)

@app.route("/restaurants/search", methods=['GET'])
def get_tag():
	res = list()
	q = request.args.get('q').lower() #add min len 1
	lat = float(request.args.get('lat'))
	lon = float(request.args.get('lon'))
	with open("resources/restaurants.json") as f:
		data = json.load(f)
		for r in data["restaurants"]:
			if q in r['name'].lower() or q in r['tags'] or q in r['description']:
				r_lat = float(r['location'][1])
				r_lon = float(r['location'][0])
				r['distance'] = get_distance(r_lat, r_lon,lat, lon)
				if r['distance'] < 3000:
					res.append(r)
	ret = {"__search_details" : {"query" : q, "location" : [lon, lat], "results" : len(res)}}
	ret["restaurants"] = res
	return jsonify(ret)


if __name__ == "__main__":
	app.run(debug=True)

# default
# /restaurants/search?q=sushi&lat=60.17045&lon=24.93147
# toolo 2.92km from center
# /restaurants/search?q=sushi&lat=60.191672&lon=24.911110