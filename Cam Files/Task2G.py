'This document is the warning system'
import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
#part1
#return list of stations with different relative water levels
stations= build_station_list()
update_water_levels(stations)
stations_high=[]
stations_mid=[]
stations_low=[]
stations_none=[]
for station in stations:
	if  station.relative_water_level()==None:
			stations_none.append(station)
	else:
		if station.relative_water_level() < 0.8:
			stations_low.append(station)
		elif station. relative_water_level() >1.5:
			stations_high.append(station)
		else:
			stations_mid.append(station)
print(len(stations_low)+len(stations_mid)+len(stations_high)+len(stations_none))
print(len(stations))

#part2
for station_low in stations_low:
	dt = 1
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    rel_level=
    poly, d0 = polyfit(dates, levels, 0)
    poly(date)
    #make lists of date and lavel
        plot_water_level_with_fit(station.name, dates, levels, 4)

#part3

#part4