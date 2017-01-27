"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key
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