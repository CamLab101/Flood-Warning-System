"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key
#maps river names to a list of stations on a given river
def rivers_with_station(stations):
    dict={}
    for station in stations:
        dict[station.river]=station.name
    return dict
#can improve because some river names begins with 'River'