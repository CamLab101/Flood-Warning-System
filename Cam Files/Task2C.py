from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    list_of_tuples=stations_highest_rel_level(stations,10)
    for station in list_of_tuples:
    	print(station[0],station[1])

run()