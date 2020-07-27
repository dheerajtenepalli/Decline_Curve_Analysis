
import math
import numpy as np
import scipy.signal as signal
import identify_number_and_volume_of_peaks as all_peaks

"""
For testing purposes we set the minimum peak distance as 3.
Step1: We find the initial peak from initial_estimate_of_time_to_peak.py
Step2: We then seperate the data into two parts, the second part of data will start from 3 data points after the initial peak.
Step3: We find all the indexes of any other peaks in part 2 of data using this .py file
Step4: Seperate declines using found peak indexes.
Step5: Please note that the width of peak is also taken into consideration. This helps to undetstand if the peak is really a peak or it is just an operational outlier.
"""
#Mock unit tests
#Lets suppose initial Peak is present at index 12. And there are two peaks after that, but one of them do not satisfy the minumim distance criterian which is 3.
#Index of the unit_test_1 array starts from 12
unit_test_1 = [600,500,400,300,1590,1580,1570,1560,1550,1540,1400,1200,1100,1050,1000,800,700,600,500,400,1400,1300,1200,4000,3500,3200,3100]

#Multiple peaks that satisfy both the height, distance and width requirement.
unit_test_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,18,17,16,15,14,13,12,11,10,9,8,9,10,11,12,13,14,16,19,25,40,50,60,70,80,90,100,110,120,140,144,130,120,110,107,102,80,70,60,50,34,20,10,8,7,6,3,2,1,2,3,4,6,7,8,7,5,4,3,2,1]

#Initial Peak is NaN. Lets see if we have any peaks in the second part of the array!!!!
unit_test_3 = [9,8,9,10,11,12,13,14,16,19,25,40,50,60,70,80,90,100,110,120,140,144,130,120,110,107,102,80,70,60,50,34,20,10,8,7,6,3,2,1,2,3,4,6,7,8,7,5,4,3,2,1]
 
def test_find_all_peaks():
	assert all_peaks.find_all_peaks(unit_test_1,700,12) == [16]
	assert (all_peaks.find_all_peaks(unit_test_2,10,12) ==[30,61]).all()
	assert (all_peaks.find_all_peaks(unit_test_2,float('nan'),float('nan')) == [18,49]).all()


	
#Mock unit tests
unit_test_4 = np.array([1,2,3,4,5,6,5,4,3,2,1])	
	
def test_get_seperate_declines():	
	assert len(all_peaks.get_seperate_declines(unit_test_4,[5],2)[0])==3
	
#test_get_seperate_declines()
print(all_peaks.get_seperate_declines(unit_test_4,[5],2))	