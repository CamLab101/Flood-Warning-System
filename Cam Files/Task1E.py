from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

stations=build_station_list()
#print (stations_by_river(stations))
#for river in stations_by_river(stations):
#    print(len(stations_by_river(stations)[river]))
print(rivers_by_station_number(stations,9)