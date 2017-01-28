"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
#haversine function for distance calculation
from haversine import haversine

#For task 1B
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

#For task 1C
def stations_within_radius(stations, centre, r):
	stations_within_radius=[]
	distancelist=stations_by_distance(stations, centre)
	for station in stations:
		if station[2] < r
		stations_within_radius.append (distancelist[0])
	return stations_within_radius

#For task 1D
#returns all rivers (by name) with a monitoring station
def rivers_with_station(stations):
    rivers_with_station=[]
    for station in stations:
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