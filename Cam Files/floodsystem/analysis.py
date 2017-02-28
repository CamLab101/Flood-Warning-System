"This is a document computes the analysis of the water level data"
import datetime
import numpy as np
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