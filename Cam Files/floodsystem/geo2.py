"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
#haversine function for distance calculation
from haversine import haversine

def stations_by_distance(stations, p):
	#compte distance
	distancelist=[]
	for station in stations:
		#use haversine function
		distance=haversine(station.coord, p)
		#create a list of tuples contain data of stations
		distancelist.append ((station.name,station.town,distance))
		#output the sorted
	return sorted_by_key (distancelist,2,0)