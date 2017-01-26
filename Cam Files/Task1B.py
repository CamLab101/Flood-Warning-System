#import station by distance
from floodsystem.geo import stations_by_distance
#inport the station list
from floodsystem.stationdata import build_station_list

from haversine import haversine

stations = build_station_list()
p=(52.2053, 0.1218)

def run():
	def stations_by_distance(stations, p):
		distancelist=[]
		for station in stations:
			distance=haversine(station.coord, p)
			#print(station.name,station.town,distance)
			return [station.name, station.town, distance]
	print (stations_by_distance(stations, p))
run()