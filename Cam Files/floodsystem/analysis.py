"This is a document computes the analysis of the water level data"
import numpy as np
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.dates

# Create set of 10 data points
def polyfit(dates, levels, p):
	d0 = matplotlib.dates.date2num(dates[0])
	x = matplotlib.dates.date2num(dates)-d0
	y = levels

	# Find coefficients of best-fit polynomial
	p_coeff = np.polyfit(x, y, p)

	# Convert coefficient into a polynomial that can be evaluated,
	# e.g. poly(0.3)
	poly = np.poly1d(p_coeff)
	return poly, d0

def risk():
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
			if station.relative_water_level() < 1:
				stations_low.append(station)
			elif station.relative_water_level() >2:
				stations_high.append(station)
			else:
				stations_mid.append(station)
	#print(len(stations_low), len(stations_mid)+len(stations_high)+len(stations_none))
	#print(len(stations))

	#part2
	no_risk=[]
	low_risk=[]
	moderate_risk=[]
	high_risk=[]
	severe_risk=[]
	#predition for low stations
	#if level less than 0.5 then no risk, predition < 0.8 low risk, > 0.8 then moderate risk
	for station in stations_low:
		if station.relative_water_level() < 0.7:
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
				if predict > 1:
					moderate_risk.append(station)
				else:
					low_risk.append(station)
			except:
				no_risk.append(station)
				pass
		#print(len(no_risk), len(low_risk), len(moderate_risk), len(high_risk),len(severe_risk), len(no_risk)+len(moderate_risk)+len(low_risk)+len(high_risk)+len(severe_risk), len(stations))

	#predition for medium stations
	#if predition < 0.5 low risk, < 0.8 moderate risk, < 1.5 high risk, > 1.5 severe risk
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
			if predict > 2.5:
				severe_risk.append(station)
			if predict > 1.5:
				high_risk.append(station)
			elif predict > 0:
				moderate_risk.append(station)
			else:
				low_risk.append(station)
		except:
			no_risk.append(station)
			pass
		#print(len(no_risk), len(low_risk), len(moderate_risk), len(high_risk),len(severe_risk), len(no_risk)+len(moderate_risk)+len(low_risk)+len(high_risk)+len(severe_risk), len(stations))

	#predition for high stations
	#if predition increasing, severe risk, < 0.4 moderate risk, decreasing but > 0.4 high risk
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
			if np.gradient(poly)[0] > 1:
				severe_risk.append(station)
			elif predict < 0.5:
				moderate_risk.append(station)
			else:
				high_risk.append(station)
		except:
			no_risk.append(station)
			pass
	return low_risk, moderate_risk, high_risk, severe_risk 
