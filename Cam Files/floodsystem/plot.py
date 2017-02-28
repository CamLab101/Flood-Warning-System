'This is a document for plotting level wrt time'
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import matplotlib.dates
import datetime
import numpy as np
from floodsystem.stationdata import build_station_list

def plot_water_levels(station, dates, levels):
	t = dates
	level = levels

	# Plot
	plt.plot(t, level)

	# Add axis labels, rotate date labels and add plot title
	plt.xlabel('date')
	plt.ylabel('water level (m)')
	plt.xticks(rotation=45);
	plt.title(station)

	# Display plot
	plt.tight_layout()  # This makes sure plot does not cut off date labels
	plt.show()

def plot_water_level_with_fit(station, dates, levels, p):

	if dates == []:
		print('{} station has no data to plot.'.format(station))
	else:
		t = dates
		level = levels
		f, d0=polyfit(dates, levels, p)

		#range line
		stations=build_station_list()
		for station_ind in stations:
			if station_ind.name == station:
				typical_low=np.linspace(station_ind.typical_range[0],station_ind.typical_range[0],len(t))
				typical_high=np.linspace(station_ind.typical_range[1],station_ind.typical_range[1],len(t))

		# Plots
		plt.plot(t, level)
		plt.plot(t, f(np.array(matplotlib.dates.date2num(t))-d0))
		plt.plot(t, typical_low)
		plt.plot(t, typical_high)

		# Add axis labels, rotate date labels and add plot title
		plt.xlabel('date')
		plt.ylabel('water level (m)')
		plt.xticks(rotation=45);
		plt.title(station)

		# Display plot
		plt.tight_layout()  # This makes sure plot does not cut off date labels
		plt.show()