#import station by distance
from floodsystem.geo import stations_by_distance
#inport the station list
from floodsystem.stationdata import build_station_list

from haversine import haversine

stations = build_station_list()
p=(52.2053, 0.1218) #Cambridge

def run():
	distancelist=stations_by_distance(stations, p)
	print (distancelist[:10])
	print (distancelist[-10:])
run()