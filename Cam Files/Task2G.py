'This document is the warning system'
from floodsystem.analysis import 
import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels, polyfit
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
#part1
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
for station_low in stations_low:
	dt = 1
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, p)
    #make lists of date and lavel
        plot_water_level_with_fit(station.name, dates, levels, 4)
#part3
#part4