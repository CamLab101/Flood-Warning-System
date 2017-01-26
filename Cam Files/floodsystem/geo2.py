"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
#haversine function for distance calculation
from haversine import haversine

def stations_by_distance(stations, p):
    geo=[]
    for station in stations:
        distance=haversine(station.coord, p)
        geo.append((station.name, station.town, station.distance))
    return sorted_by_key(geo, 3, 0)