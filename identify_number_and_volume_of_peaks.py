"""
This file contains code to indentify peaks with the following restrictions.
Restriction_1 : The peak height should be atleast 0.5 times the initial peak height.
Restriction_2 : The horizontal distance between the peaks should be atlest "minimum_peak_distance". Currently, it is 180.
Restriction_3: The width of each peak must be atleast 7. This helps us to find legitemate declines.
"""

#Importing necessary libraries
import math
import numpy as np
import scipy.signal as signal
import configuration as cg

def find_all_peaks(y3,max_peak,index_max_peak):
	"""
	Description: This functions finds all peaks in the second part of data.
	Input: Second part of data. That is the data from the intial peak.
	Output: Peak indexes adjusted to orginal data.
	"""
	y4 = y3[cg.minimum_peak_distance:]

	if math.isnan(max_peak):
		peaks, _ = signal.find_peaks(y4,distance = cg.minimum_peak_distance,width = cg.minimum_width_peak)
		peaks = peaks + cg.minimum_peak_distance	
	else:
		peaks, _ = signal.find_peaks(y4, height = cg.height_multiplier*max_peak, distance = cg.minimum_peak_distance,width = cg.minimum_width_peak)
		peaks = peaks + cg.minimum_peak_distance + index_max_peak

	return peaks

def get_seperate_declines(y2,peaks,index_max_peak):
	"""
	Description: This function seperates the input data based on all peak indexes.
	Input: Well data without outliers.
	Output: An array of arrays, each array representing one decline.
	"""
	if index_max_peak != 0:
		all_peaks = np.insert(np.array(peaks),0,index_max_peak)
	else:
		all_peaks = peaks

	list_of_all_declines = np.split(y2,all_peaks)
	return list_of_all_declines,all_peaks
	
	
	
	
