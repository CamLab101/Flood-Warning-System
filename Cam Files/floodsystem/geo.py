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
    list_of_stations=rivers_with_station(stations)
    for river in list_of_stations:
        dict [river]=[]
        for station in stations:
            if station.river==river:
                dict [river].append(station.name)
            else:
                    pass
        dict[river].sort()
    return dict

#for task 1E

#determines the N rivers with the greatest number of monitoring stations
def rivers_by_station_number(stations,N):
    dict=stations_by_river(stations)
    #list of tuples
    num_of_stations=[]
    for river in dict:
        num_of_stations.append((river,len(dict[river])))
    #sort
    num_of_stations.sort(key=lambda tup: tup[1], reverse=True)
    #return first N
    nlist=[]
    n=0
    x=0
    #error
    while n<=N:
        x+=1
        nlist.append(num_of_stations[x])
        if num_of_stations[x+1][1]>num_of_stations[x][1]:
            n+=1
        else:
            pass
    return nlist

