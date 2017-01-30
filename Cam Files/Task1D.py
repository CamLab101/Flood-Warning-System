from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations=build_station_list()
def run():
    rivers=rivers_with_station(stations)
    return print(rivers[:10])

#return first 10 rivers
rivers=rivers_with_station(stations)
print(rivers[:10])

#stations_in('River Aire')

dict=stations_by_river(stations)
print(dict['River Aire'])
print(dict['River Cam'])
print(dict['Thames'])
