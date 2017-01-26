"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
#haversine function for distance calculation
from haversine import haversine
#inport the station list
from .stationdata import build_station_list

def stations_by_distance(stations, p=(52.2053, 0.1218)):
    stations=build_station_list()
    geo=[]
    for station in stations:
        distance=haversine(station.coord, p)
        geo.append((station.name, station.town, station.distance))
    return sorted_by_key(geo, 3, 0)