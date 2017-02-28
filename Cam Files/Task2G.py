'This document is the warning system'
import numpy as np
import datetime
from floodsystem.analysis import polyfit, risk
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.dates

def run():
	#part1
	low_risk, moderate_risk, high_risk, severe_risk = risk()

	#part3
	#sort list of towns with warning
	towns_severe=[]
	towns_high=[]
	towns_moderate=[]
	towns_low=[]
	towns_counted=[]
	print('****** SEVERE Risk ******')
	for station in severe_risk:
		if (station.town in towns_counted)==False:
			towns_severe.append (station.town)
			towns_counted.append (station.town)
			print(station.town)
	print(len(severe_risk), 'towns under severe risk')
	print('****** HIGH Risk ******')
	for station in high_risk:
		if (station.town in towns_counted)==False:
			towns_high.append (station.town)
			towns_counted.append (station.town)
			print(station.town)
	print(len(high_risk), 'towns under high risk')
	print('****** MODERATE Risk ******')
	for station in moderate_risk:
		if (station.town in towns_counted)==False:
			towns_moderate.append (station.town)
			towns_counted.append (station.town)
			print(station.town)
	print(len(moderate_risk), 'towns under moderate risk')
	print('****** LOW Risk ******')
	for station in low_risk:
		if (station.town in towns_counted)==False:
			towns_low.append (station.town)
			towns_counted.append (station.town)
			print(station.town)
	print(len(low_risk), 'towns under low risk')

if __name__ == "__main__":
    print("*** The Avdanced Flood Warning System ***")


run ()

#part4