#for Task 2B
#returns a list of tuples, where each tuple holds 
#(1) a station at which the latest relative water level is over tol and 
#(2) the relative water level at the station
def stations_level_over_threshold(stations, tol):
	list_of_tuples=[]
	for station in stations:
		if  station.relative_water_level()==None:
			pass
		else:
			if station.relative_water_level() > tol:
				list_of_tuples.append((station.name, station.relative_water_level()))
	list_of_tuples.sort(key=lambda tup: tup[1], reverse=True)
	return list_of_tuples

#for Task 2C
#returns a list of the N stations at which the water level, relative to the typical range, is highest.
def stations_highest_rel_level(stations, N):
	stations_highest_rel_level=[]
	for station in stations:
		if station.relative_water_level() != None:
			stations_highest_rel_level.append((station.name, station.relative_water_level()))
	stations_highest_rel_level.sort(key=lambda tup: tup[1], reverse=True)
	return (stations_highest_rel_level[:N])
