"""
This file contains code to identify intital time to peak.
"""
import math
import numpy as np
import configuration as cg

def indentify_initial_peak(y2):
	"""
	Description: This Function finds the initial peak within the first 180 data points.
	Input: Well's oil or gas values
	Output: Initial peak value.	
	"""

	max_peak = float('nan')
	initial_max_peaks_index = y2.argsort()[-3:][::-1]
	initial_max_peaks = np.where(initial_max_peaks_index >= cg.find_initial_peak_within_these_points, float('nan'), y2[initial_max_peaks_index])
	
	if initial_max_peaks[1] > initial_max_peaks[2]:
		max_peak = initial_max_peaks[1]
		
	if math.isnan(max_peak) and math.isnan(initial_max_peaks[2]):
		max_peak = initial_max_peaks[1]

	if math.isnan(max_peak) and math.isnan(initial_max_peaks[1]):
		max_peak = initial_max_peaks[2]
		
	if math.isnan(max_peak):
		max_peak = initial_max_peaks[0]
			
	return max_peak
