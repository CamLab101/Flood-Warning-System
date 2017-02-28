'This document is the warning system'
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
#return list of stations with relative water level above and below 0.8
stations= build_station_list()
update_water_levels(stations)
stations_name_high=[]
stations_high=[]
stations_low=[]
test=[]
list_of_tuples=stations_level_over_threshold(stations,0.8)
for station in list_of_tuples:
	stations_name_high.append(station[0])
for station in stations:
	if (station.name in stations_name_high)==True:
		stations_high.append(station)
	else:
		pass

for station in stations:
	if (station.name in stations_name_high)==True:
		pass
	else:
		stations_low.append(station)

#part2
#part3
#part4