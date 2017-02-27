import matplotlib
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels

import datetime

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
