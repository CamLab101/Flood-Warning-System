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
#returns all rivers (by name) with a monitoring station
def rivers_with_station(stations):
    rivers_with_station=[]
    for station in stations:
<<<<<<< HEAD
        dict[station.river]=station.name
    return dict
#can improve because some river names begins with 'River'
>>>>>>> master
=======
        rivers_with_station.append(station.river)
    rivers_with_station=set(rivers_with_station)
    unique_rivers=[]
    for river in rivers_with_station:
        unique_rivers.append(river)
    unique_rivers.sort()
    return unique_rivers

#maps river names (the ‘key’) to a list of stations on a given river
def stations_by_river(stations):
    dict={}
    for river in rivers_with_station(stations):
        dict [river]=[]
        for station in stations:
            if station.river==river:
                dict [river].append(station.name)
            else:
                    pass
        dict[river].sort()
    return dict
>>>>>>> master
