#import station by distance
from floodsystem.geo import stations_by_distance
#inport the station list
from floodsystem.stationdata import build_station_list
#open station list
stations = build_station_list()
#coordinate of Cambridge
p=(52.2053, 0.1218)

def run():
	distancelist=stations_by_distance(stations, p)
	print (distancelist[:10])
	print (distancelist[-10:])
run()