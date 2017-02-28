"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
import numpy as np

class MonitoringStation:
	"""This class represents a river level monitoring station"""

	def __init__(self, station_id, measure_id, label, coord, typical_range,
				 river, town):

		self.station_id = station_id
		self.measure_id = measure_id

		# Handle case of erroneous data where data system returns
		# '[label, label]' rather than 'label'
		self.name = label
		if isinstance(label, list):
			self.name = label[0]

		self.coord = coord
		self.typical_range = typical_range
		self.river = river
		self.town = town

		self.latest_level = None

	def __repr__(self):
		d = "Station name:     {}\n".format(self.name)
		d += "   id:            {}\n".format(self.station_id)
		d += " measure id: {}\n".format(self.measure_id)
		d += "   coordinate:    {}\n".format(self.coord)
		d += "   town:          {}\n".format(self.town)
		d += "   river:         {}\n".format(self.river)
		d += "   typical range: {}".format(self.typical_range)
		return d
	
	
	#for 1F
	#return True if the data is consistent and False if the data is inconsistent or unavailable
	def typical_range_consistent(self):
		if self.typical_range == None:
			return False
		else:
			if self.typical_range[0]>self.typical_range[1]:
				return False
			else:
				return True

	#for 2B
	#returns the latest water level as a fraction of the typical range, 
	#i.e. a ratio of 1.0 corresponds to a level at the typical high 
	#and a ratio of 0.0 corresponds to a level at the typical low
	def relative_water_level(self):
		if type(self.latest_level)==list:
			level=sum(self.latest_level)/len(self.latest_level)
		else:
			level=self.latest_level
		if self.typical_range_consistent()==True and self.latest_level != None:
			ratio=(level-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
		else:
			ratio=None
		return ratio

	#for 2G
	def relative_history_levels(self):
		'compute relative water level for history levels'
		if self.typical_range_consistent()==True and self.latest_level != None and type(self.history_levels)==np.ndarray:
			ratio=(self.history_levels-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
		else:
			ratio=None
		return ratio


#for 1F
#returns a list of stations that have inconsistent data
def inconsistent_typical_range_stations(stations):
	inconsistent_stations=[]
	for station in stations:
		if station.typical_range_consistent() == False:
			inconsistent_stations.append(station.name)
		else:
			pass
	inconsistent_stations.sort()
	return inconsistent_stations