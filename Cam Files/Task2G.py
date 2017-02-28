'This document is the warning system'
import numpy as np
import datetime
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.dates

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
		elif station.relative_water_level() >1.5:
			stations_high.append(station)
		else:
			stations_mid.append(station)
print(len(stations_low), len(stations_mid)+len(stations_high)+len(stations_none))
print(len(stations))

#part2
no_risk=[]
low_risk=[]
moderate_risk=[]
high_risk=[]
severe_risk=[]
#predition for low stations
for station in stations_low:
	if station.relative_water_level() < 0.5:
		no_risk.append(station)
	else:
		dt = 1
		#get history dates and levels
		dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
		#calculating relative history data
		try:
			station.history_levels=np.array(levels)
			relative_levels=station.relative_history_levels()
			#calculating a one power line of fit
			poly, d0=polyfit (dates, relative_levels, 1)
			#predict after one day
			t_now = matplotlib.dates.date2num(datetime.datetime.utcnow())
			predict=poly(t_now+1-d0)
			if predict > 0.8:
				moderate_risk.append(station)
			else:
				low_risk.append(station)
		except:
			no_risk.append(station)
			pass
	print(len(no_risk), len(low_risk), len(moderate_risk), len(high_risk),len(severe_risk), len(no_risk)+len(moderate_risk)+len(low_risk)+len(high_risk)+len(severe_risk), len(stations))

for station in stations_mid:
	dt = 1
	#get history dates and levels
	dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
	#calculating relative history data
	try:
		station.history_levels=np.array(levels)
		relative_levels=station.relative_history_levels()
		#calculating a one power line of fit
		poly, d0=polyfit (dates, relative_levels, 1)
		#predict after one day
		t_now = matplotlib.dates.date2num(datetime.datetime.utcnow())
		predict=poly(t_now+1-d0)
		if predict > 0.8:
			high_risk.append(station)
		elif predict > 0.5:
			moderate_risk.append(station)
		else:
			low_risk.append(station)
	except:
		moderate_risk.append(station)
		pass
	print(len(no_risk), len(low_risk), len(moderate_risk), len(high_risk),len(severe_risk), len(no_risk)+len(moderate_risk)+len(low_risk)+len(high_risk)+len(severe_risk), len(stations))

for station in stations_high:
	dt = 1
	#get history dates and levels
	dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
	#calculating relative history data
	try:
		station.history_levels=np.array(levels)
		relative_levels=station.relative_history_levels()
		#calculating a one power line of fit
		poly, d0=polyfit (dates, relative_levels, 1)
		#predict after one day
		t_now = matplotlib.dates.date2num(datetime.datetime.utcnow())
		predict=poly(t_now+1-d0)
		if predict.deriv() > 1:
			severe_risk.append(station)
		elif predict < 0.7:
			moderate_risk.append(station)
		else:
			high_risk.append(station)
	except:
		high_risk.append(station)
		pass
	print(len(no_risk), len(low_risk), len(moderate_risk), len(high_risk),len(severe_risk), len(no_risk)+len(moderate_risk)+len(low_risk)+len(high_risk)+len(severe_risk), len(stations))


#part3

#part4