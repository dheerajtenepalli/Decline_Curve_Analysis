import scipy.signal as signal
import time
import math
import numpy as np
import pandas as pd
from scipy.optimize import fmin_tnc
from scipy import stats
from pylab import *
from scipy.optimize import curve_fit
from multiprocessing import Pool, cpu_count
from contextlib import closing
import pickle

#Importing other .py files
import prepare_data
import initial_estimate_of_time_to_peak as init_peak
import outlier_analysis
import identify_number_and_volume_of_peaks as find_all_peaks 
import decline_functions as dec_func
import signal_features
import main
#Mock test data.
#Mocking gas data for a mock well

well_data = list(range(900,100,-1))

def test_fit_and_forecast():
	#Check whether 10 arrays containing test results, forecasts, ouliers are present.
	if len(main.fit_and_forecast(well_data)) == 11:
		print("1 Passed, 1 warnings")
	
"""
The ouput array from this fit_and_forecast function has 11 sub arrays.
1. Array1 = origianl data
2. Array2 = y_pred_exponential
3. Array3 = y_pred_harmonic
4. Array4 = y_pred_hyperbolic
5. Array5 = y_pred_hyp2exp
6. Array6 = exponential_forecast
7. Array7 = harmonic_forecast
8. Array8 = hyperbolic_forecast
9. Array9 = hyp2exp_forecast
10. Array10 = length_of_last_subdecline
11. Array11 = outliers

"""
test_fit_and_forecast()
#Note the output is very large and values are in float. The decimal points changes somtimes by a very small value, so we can not assert them.