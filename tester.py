import requests
import json

# please inser localhost ip and port as a string
localhost_ip = "127.0.0.1:5000"


def print_results(restaurants):
	h = restaurants['__search_details']
	all_r = restaurants['restaurants']
	print("\nRequest details")
	for key in h:
		print(f"{key}: {h[key]}")
	print("\nResults")
	i = 1
	for r in all_r:
		dist = "{0:.0f} metres".format(r['distance'])
		print(f"{i}) {r['name']}\n\t{r['description']}\n\t{r['tags']}\n\t{dist}\n")
		i += 1

query = input("Search query:\n")
lon = float(input("Longitude:\n"))
lat = float(input("Latitude: \n"))
ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")

print_results(ret.json())