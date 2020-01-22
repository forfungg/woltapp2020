import math

# Earth radius on given Latitude
# re - Equatorial radius of Earth
# rp - Polar radius of Earth
def get_radius(lat):
	re = 6378137.0
	rp = 6356752.3
	lat_rad = math.radians(lat)
	a = ((re**2) * math.cos(lat_rad))**2
	b = ((rp**2) * math.sin(lat_rad))**2
	c = (re * math.cos(lat_rad))**2
	d = (rp * math.sin(lat_rad))**2
	rc = (a + b) / (c + d)
	rc = rc ** 0.5
	return rc

# Distance
# Spherical Law of Cosines
# Using average Earth radius between the two points
def get_distance(lat, lon, my_lat, my_lon):
	lat_rad = math.radians(lat)
	lon_rad = math.radians(lon)
	my_lat_rad = math.radians(my_lat)
	my_lon_rad = math.radians(my_lon)
	avg_r = (get_radius(lat) + get_radius(my_lat)) / 2
	d = math.acos(math.sin(lat_rad) * math.sin(my_lat_rad) + math.cos(lat_rad) * math.cos(my_lat_rad) * math.cos(abs(lon_rad - my_lon_rad))) * avg_r
	return d

if __name__ == "__main__":
	lat_a = 60.17328170963167
	lon_a = 24.938911199569702
	lat_b = 60.17045
	lon_b = 24.93147
	print(get_distance(lat_a, lon_a, lat_b, lon_b))