import initial_estimate_of_time_to_peak as test_peak
import numpy as np
import math

#Mock Unit tests

#Note that 280 is the initial start of decline. So, that should be identified as intitial peak
unit_test_1 = np.array([0,0.5,6,7,10,100,200,300,280,270,250,230,220,210,200,180])
#Note here the decrease starts right away. This is a corner case.
unit_test_2 = np.array([180,170,160,150,140,130,120,100])
#Note that there is no peak until the very end, but there is a small decline in between. This is also an interesting case.
unit_test_3 = np.array([1,2,3,4,5,6,7,18,19,30,40,50,60,70,45,85,120,110,100,90,80,70,60,45,30])
#Mostly zeros!!
unit_test_4 = np.array([0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0])
#Initial peak not found in the first 180 points, retunrs intial peak as nan
unit_test_5 = np.array([0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,11,23,45,160,80,70,0,0,0,0,0,0,0,1000,900,800,700])


def test_indentify_initial_peak():
	assert test_peak.indentify_initial_peak(unit_test_1) == 280
	assert test_peak.indentify_initial_peak(unit_test_2) == 170
	assert test_peak.indentify_initial_peak(unit_test_3) == 110
	assert test_peak.indentify_initial_peak(unit_test_4) == 80
	assert math.isnan(test_peak.indentify_initial_peak(unit_test_5))
	
	
print(test_peak.indentify_initial_peak(unit_test_5))	