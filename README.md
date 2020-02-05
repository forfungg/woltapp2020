# WoltApp Summer 2020

This is my solution for [Wolt's Summer 2020 Internship assignment](https://github.com/woltapp/summer2020)

## My solution (search.py)

### Requirements
	- python3
	- Flask (pip3 install flask)

### Usage and output

To start the API, run:
```
python3 search.py
```

From the status message retrieve the "Running on" address (similiar to below):
```
		python3 search.py
		* Serving Flask app "search" (lazy loading)
		* Environment: production
		WARNING: This is a development server. Do not use it in a production deployment.
		Use a production WSGI server instead.
		* Debug mode: on
		* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
		* Restarting with stat
		* Debugger is active!
		* Debugger PIN: 167-670-610
```

Then either use included tester.py, or create custom request using any internet browser window and the retrieved ip address. From previous example the request could look like this:
```
http://127.0.0.1:5000/restaurants/search?q=risotto&lat=60.15260861959699&lon=24.935724109610046
```

As response you should see json formated output including all restaurants from restaurants.json that fulfill given requirements:
- the querry (q) was found in either name, description or tags of the restaurant
- the restaurant is located less than 3000 metres from given position

The output is enveloped in order to show search parametres as it is easier to pass additional information this way, if the enveloping is not desired, it can be simply removed from the code. Also the output information includes added field 'distance' wich contains float value of the distance from given position to the restaurant in metres. This change can be as well simply removed if desired so.

Example output for above stated request:
```
{
  "__search_details": {
    "location": [
      24.935724109610046, 
      60.15260861959699
    ], 
    "query": "risotto", 
    "results": 1
  }, 
  "restaurants": [
    {
      "blurhash": "j2DUFG8jbu8AXuLIT5Tt0B01R2;;", 
      "city": "Helsinki", 
      "currency": "EUR", 
      "delivery_price": 390, 
      "description": "Japanilaista ramenia parhaimmillaan", 
      "distance": 1952.8023025841067, 
      "image": "https://prod-wolt-venue-images-cdn.wolt.com/5d108aa82e757db3f4946ca9/d88ebd36611a5e56bfc6a60264fe3f81", 
      "location": [
        24.941786527633663, 
        60.169934599421396
      ], 
      "name": "Momotoko Citycenter", 
      "online": false, 
      "tags": [
        "ramen", 
        "risotto"
      ]
    }
  ]
}
```

### Description and Approach

I've decided to use Flask framework in python3 to create the solution. Flask allows to set up simple api very quickly while still being fairly lighweight.

Crucial points of the assignment were, correct distance calculation based on latitudes and longitudes, simple search in multiple fields and error management.

Return codes
200 OK	Successful.
400 Bad Request	Bad input parameter. Error message should indicate which one and why.
404 Not Found	Resource not found.
405 (Method Not Allowed)

## WoltApp Summer 2020
Backend option
- REST API
	- searching restaurants
		/* method=GET else: return errno 405 */
	- 3 parameters on request
		- q: querry string (to be searched in name, tags, description; min length 1)
			/* missing requirement for len > 0 */
		- lat: request latitude location
		- lon: request longtitude location
			/* missing protection from invalid parameters for lon and lat */
		/* missing protection from missing parameters or invalid ones */
		/* errno 400 + msg */
	- Return
		- JSON object
			Enveloped
				```
					location: longitude and latitude of the search request
					querry: search query of the request
					results: total amout of found restaurants
					/*tbd*/
					return code: api return code
					return msg: api return message (Success or Error msg)
				```
		- match q string and within 3km range
			/* proposal for sorting and returning only open restaurants  with extra params */
	- Bonus Blurhash
	- Tips
		- clean code
		- good tests
		- README.md with clear instructions how to get the project up and running

## Tests (tester.py)
Requirements
	
	For tests (tester.py)
	-pip3 install requests

Run
	python3 tester.py <local_host:port>

Select mode
	- predefined searches
		- shows results for bunch of test requests (from test_requests.json)
	- predefined locations
		- shows results for custom query with bunch of test locations (from test_requests.json)
	- custom

Advanced
	adjust test_requests.json to your preferences
# To-Do
	requests json?