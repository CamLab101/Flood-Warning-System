#import station by distance
from floodsystem.geo import stations_within_radius
#inport the station list
from floodsystem.stationdata import build_station_list
#open station list
stations = build_station_list()
#coordinate of Cambridge
centre=(52.2053, 0.1218)
#radius
r=10

def run():
	radiuslist=stations_within_radius(stations, centre, r)
	print (radiuslist)
run()