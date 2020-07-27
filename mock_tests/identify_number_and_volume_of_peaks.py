#Importing necessary libraries
import math
import numpy as np
import scipy.signal as signal

#This function finds all peaks with a minimum distance of  "minimum_peak_distance" which is set in configuration.py file.
#Removes operational outlier peaks during declines using width parameter.
#In this example for testing purposes we will set the minimum distance between peaks as 3
def find_all_peaks(y3,max_peak,index_max_peak):
	y4 = y3[3:]

	if math.isnan(max_peak):
		peaks, _ = signal.find_peaks(y4,distance = 3,width = 7)
		peaks = peaks + 3	
	else:
		peaks, _ = signal.find_peaks(y4, height = 0.5*max_peak, distance = 3,width = 7)
		peaks = peaks + 3 + index_max_peak

	return peaks

def get_seperate_declines(y2,peaks,index_max_peak):
	#print(peaks)
	#print(index_max_peak)
	if index_max_peak != 0:
		all_peaks = np.insert(np.array(peaks),0,int(index_max_peak))
	else:
		all_peaks = peaks
	print(all_peaks)
	list_of_all_declines = np.split(y2,all_peaks)
	#print("All_peaks",all_peaks)
	return list_of_all_declines,all_peaks
	
	
	
	
