# WoltApp Summer 2020

## Requirenments && Installation

python3

pip install flask

run
	python3 search.py
	get_request to "running on" IP

	'''
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

		Example of request in internet browser:
		http://127.0.0.1:5000/restaurants/search?q=sushi&lat=60.17045&lon=24.93147
	'''

## Descriptions

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
				'''
					location: longitude and latitude of the search request
					querry: search query of the request
					results: total amout of found restaurants
					/*tbd*/
					return code: api return code
					return msg: api return message (Success or Error msg)
				'''
		- match q string and within 3km range
			/* proposal for sorting and returning only open restaurants  with extra params */
	- Bonus Blurhash
	- Tips
		- clean code
		- good tests
		- README.md with clear instructions how to get the project up and running

# Tester
Requirements
	pip3 install requests
	

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