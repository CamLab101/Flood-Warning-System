from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
	stations = build_station_list()
	update_water_levels(stations)
	list_of_tuples=stations_level_over_threshold(stations,0.8)
	for station in list_of_tuples:
		print(station[0],station[1])
run()