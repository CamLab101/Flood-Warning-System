"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
#haversine function for distance calculation
from haversine import haversine

def stations_by_distance(stations, p):
	#compte distance
	stations_by_distance=[]
	for station in stations:
		#use haversine function
		distance=haversine(station.coord, p)
		#create a list of tuples contain data of stations
		stations_by_distance.append ((station.name,station.town,distance))
		#output the sorted
	return sorted_by_key (stations_by_distance,2,0)

def stations_within_radius(stations, centre, r):
	stations_within_radius=[]
	distancelist=stations_by_distance(stations, centre)
	for station in stations:
		if station[2] < r
		stations_within_radius.append ()