from flask import Flask, jsonify, request
import json
from srcs.get_range import get_distance
app = Flask(__name__)

# Validates parametres
def validate_params(q, lat, lon):
	if  q == None or len(q) < 1 or lat == None or lon == None:
		return False
	elif not (-90 <= lat <= 90):
		return False
	elif not (-180 <= lon <= 180):
		return False
	else:
		return True

# Tries to typecast string to float, returns None failure
def transcribe_float(str_nb):
	try:
		nb = float(str_nb)
	except:
		nb = None
	return nb

@app.route("/restaurants/search", methods=['GET'])
def do_search():
	res = list()
	if request.args.get('q'):
		q = request.args.get('q').lower()
	else:
		q = None
	lat = transcribe_float(request.args.get('lat'))
	lon = transcribe_float(request.args.get('lon'))
	if not validate_params(q, lat, lon):
		return "Bad Request!", 400
	with open("resources/restaurants.json") as f:
		data = json.load(f)
		for r in data["restaurants"]:
			if q in r['name'].lower() or q in r['tags'] or q in r['description']:
				r_lat = float(r['location'][1])
				r_lon = float(r['location'][0])
				r['distance'] = get_distance(r_lat, r_lon,lat, lon)
				if r['distance'] < 3000:
					res.append(r)
	#Enveloping the results
	ret = {"__search_details" : {"query" : q, "location" : [lon, lat], "results" : len(res)}}
	ret["restaurants"] = res
	return jsonify(ret), 200


if __name__ == "__main__":
	app.run(debug=True)

# default
# /restaurants/search?q=sushi&lat=60.17045&lon=24.93147
# toolo 2.92km from center
# /restaurants/search?q=sushi&lat=60.191672&lon=24.911110