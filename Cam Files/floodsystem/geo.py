"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
#haversine function for distance calculation
from haversine import haversine

def stations_by_distance(stations, p):
	distancelist=[]
	for station in stations:
		distance=haversine(station.coord, p)
		distancelist.append ((station.name,station.town,distance))
	return sorted_by_key (distancelist,2,0)