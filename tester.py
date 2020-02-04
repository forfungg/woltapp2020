import requests
import json
from random import randint

# please inser localhost ip and port as a string
localhost_ip = "127.0.0.1:5000"


def print_results(restaurants):
	if not restaurants:
		print("Empty response")
		return
	h = restaurants['__search_details']
	all_r = restaurants['restaurants']
	print("\nRequest Details:")
	for key in h:
		print(f"{key}: {h[key]}")
	print("\nResults")
	i = 1
	for r in all_r:
		dist = "{0:.0f} metres".format(r['distance'])
		print(f"{i}) {r['name']}\n\t{r['description']}\n\t{r['tags']}\n\t{dist}\n")
		i += 1

def load_data():
	with open("test_requests.json") as f:
		data = json.load(f)
	return data["tags"], data["locations"]

def get_random_location():
	t, l = load_data()
	rng = randint(0, len(l) - 1)
	return l[rng]

def get_random_tag():
	t, l = load_data()
	rng = randint(0, len(t) - 1)
	return t[rng]

print("SELECT TESTER MODE\n 1 - Selects random tag as a query and location from test_request.json\n 2 - Custom query, random location\n 3 - Fully custom request\n 4 - Incorrect requests\n")
while True:
	mode = input()
	if mode in ["1", "2", "3", "4"]:
		break
	else:
		print("Incorrect input, try again. 1, 2, 3 or 4?")

if mode == "3":
	query = input("Search query:\n")
	lon = float(input("Longitude:\n"))
	lat = float(input("Latitude: \n"))
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print_results(ret.json())
elif mode == "2":
	query = input("Search query:\n")
	loc = get_random_location()
	lon = loc[0]
	lat = loc[1]
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print_results(ret.json())
elif mode == "1":
	query = get_random_tag()
	loc = get_random_location()
	lon = loc[0]
	lat = loc[1]
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print(f"Return code: {ret}")
	print_results(ret.json())
elif mode == "4":
	print("Testing q=\"\"")
	query = ""
	loc = get_random_location()
	lon = loc[0]
	lat = loc[1]
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print(ret)
	query = "r"
	print("Testing missing q parameter")
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?lat={lat}&lon={lon}")
	print(ret)
	print("Testing missing lat parameter")
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lon={lon}")
	print(ret)
	print("Testing missing lon parameter")
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}")
	print(ret)
	print("Testing POST request")
	ret = requests.post(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print(ret)
	print("Testing DEL request")
	ret = requests.delete(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print(ret)
	print("Testing invalid latitudes")
	lat = 91
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print(f"lat={lat}: {ret}")
	lat = -91
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print(f"lat={lat}: {ret}")
	loc = get_random_location()
	lon = loc[0]
	lat = loc[1]
	print("Testing invalid latitudes")
	lon = 190
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print(f"lon={lon}: {ret}")
	lon = -190
	ret = requests.get(f"http://{localhost_ip}/restaurants/search?q={query}&lat={lat}&lon={lon}")
	print(f"lon={lon}: {ret}")
	loc = get_random_location()
	lon = loc[0]
	lat = loc[1]