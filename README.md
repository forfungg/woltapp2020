# WoltApp Summer 2020

This is my solution for [Wolt's Summer 2020 Internship assignment](https://github.com/woltapp/summer2020)

## My solution (search.py)

### Requirements

* python3
* Flask (pip3 install flask)

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

Then either use included [tester.py](https://github.com/forfungg/woltapp2020#tests-testerpy), or create custom request using any internet browser window and the retrieved ip address. From previous example the request could look like this:
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

To calculate the distance I've used the [Spherical Law of Cosines](https://en.wikipedia.org/wiki/Spherical_law_of_cosines), however since I read that with standard average Earth radius the error margin is up 0.3% I decided also to calculate Earth radius on both known latitudes (customer & restaurant) and use their average instead, which should increase the accuracy.\
The search was fairly simple using python's synax "if string in iterable" and build in string function .lower() to guarantee the precision.\
Error management considers following and returns relevant standard API code:
- query string is less than one character or missing as a whole\
- latitude is not in allowed range -90 to +90, not a float number or missing as a whole\
- longitude is not in allowd range -180 to +180, not a float number or missing as a whole\
- the request method is not GET

Return codes\
200 OK	Successful.\
400 Bad Request	Bad input parameter.\
405 Method Not Allowed

## Tests (tester.py)

### Requirements
	
- python3
- requests module (pip3 install requests)
- running [search.py](https://github.com/forfungg/woltapp2020#usage-and-output)

If the "Running on" IP address is different than "127.0.0.1:5000" the variable localhost_ip in tester.py (line 6) must be adjusted to the correct value.

### Usage

Run the tester.py
```
	python3 tester.py
```

Select mode:
- Mode 1: Selects random tag and random location from [test_requests.json](resources/test_requests.json) and runs correct GET requests to the API\
- Mode 2: Choose the search query of your desire, but the location will be randomly selected from [test_requests.json](resources/test_requests.json)\
- Mode 3: Fully customizable request parametres values
- Mode 4: Does bunch of incorrect requests on the API

### Extract Script

If you desire to generate new random locations. Or if you're using different sample file than the given restaurants.json, please copy such file to resources/ and/or adjust the path within extract.py code. Then run following from the root:
```
python3 resources/extract.py
```

The scipt extracts all tags from the resource file and generates 100 random locations within rectangle between Suomenlinna and Meilathi hospital (about 7km apart). Also 