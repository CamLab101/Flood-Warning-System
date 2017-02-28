'This document is the warning system'
from floodsystem.analysis import polyfit
import numpy as np
#part1
#part2
for station_low in stations_low:
	dt = 1
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, p)
    #make lists of date and lavel
        plot_water_level_with_fit(station.name, dates, levels, 4)
#part3
#part4