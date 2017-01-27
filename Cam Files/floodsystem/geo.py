"""This module contains a collection of functions related to
geographical data.

"""

<<<<<<< HEAD
from .utils import sorted_by_key
#haversine function for distance calculation
from haversine import haversine

def stations_by_distance(stations, p):
	distancelist=[]
	for station in stations:
		distance=haversine(station.coord, p)
		distancelist.append ((station.name,station.town,distance))
	return sorted_by_key (distancelist,2,0)
=======
from floodsystem.utils import sorted_by_key
#maps river names to a list of stations on a given river
def rivers_with_station(stations):
    dict={}
    for station in stations:
        dict[station.river]=station.name
    return dict
#can improve because some river names begins with 'River'
>>>>>>> master
