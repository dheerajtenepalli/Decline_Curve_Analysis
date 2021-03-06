"""
This is the main file for the code.
1. This file uses code from other .py files to fit and forecast data.
3. A documentation pdf along with readme.txt file is submitted for reference.
"""

#Importing necessary Libraries
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

	
	
def fit_and_forecast(well_data):
	"""
	Description: This function takes in well_data.
	Input: df
	Output: Preprocessed data for oil and gas for all wells.
	"""
	
	#Saving the well_name of our well_data into a variable.
	well_name = "Well_170245_gas" 
	print("Processing",well_name)
	
	#Converting pandas series to a numpy array for much faster processing without overhead.	
	well_data = np.array(well_data)

	#Creating a time array for our well_data where t1 and y1 are time and welldata respectively.	
	t1 = np.array(list(range(len(well_data)))) + 1
	y1 = well_data
	
		
	#Remove downtime outliers.	
	y2 = y1[np.nonzero(y1)]
	t2 = np.array(list(range(len(y2)))) + 1
	
	
	#features = signal_features.reduce_signal_to_basic_features(y2)
	
	#Outlier analysis using data distribution --> Removes both global and local outliers.
	y2,outliers = np.array(outlier_analysis.remove_outliers(y2))
	
	#Identify initial time to peak
	max_peak = init_peak.indentify_initial_peak(y2)
	
	if math.isnan(max_peak):
		index_max_peak = 0
	else:
		index_max_peak = list(y2).index(max_peak)
	
	#Seperate decline curves and remove operational outlier peaks.	
	y3 = y2[index_max_peak:]
	peaks = find_all_peaks.find_all_peaks(y3,max_peak,index_max_peak)
	list_of_subdeclines,all_peaks = find_all_peaks.get_seperate_declines(y2,peaks,index_max_peak)
	find_indexes_for_these_values = y2[all_peaks]
	indexes_for_prediction = [list(y1).index(each_value) for each_value in find_indexes_for_these_values]

	#Initialize lists to store models.
	list_of_all_fits_exponential = []
	list_of_all_fits_harmonic = []
	list_of_all_fits_hyperbolic = []
	list_of_all_fits_hyp2exp = []
	
	#Check if subdeclines are less than length 7 as per R code.	
	length_of_first_sub_decline = len(list_of_subdeclines[0])	
	length_of_last_sub_decline = len(list_of_subdeclines[-1])	
	
	if length_of_last_sub_decline <= 7:
		list_of_subdeclines[-2] = np.concatenate((list_of_subdeclines[-2],list_of_subdeclines[-1])) 	
		list_of_subdeclines = list_of_subdeclines[:-1]
		indexes_for_prediction = indexes_for_prediction[:-1]
		
	if length_of_first_sub_decline <= 7:
		list_of_subdeclines[1] = np.concatenate((list_of_subdeclines[0],list_of_subdeclines[1])) 	
		list_of_subdeclines = list_of_subdeclines[1:]
		indexes_for_prediction = indexes_for_prediction[1:]

	#Model traininig to fit the data for several decline curves.
	for index,each_decline in enumerate(list_of_subdeclines):
		if index == 0:
			initial_guess_for_q_i = 200
		elif index == 0 and len(list_of_subdeclines)==1:
			initial_guess_for_q_i = np.mean(each_decline[:3])
		else:
			initial_guess_for_q_i = np.mean(each_decline[:3])
		t = np.array(list(range(len(each_decline)))) + 1
		try:
			popt_1, pcov_1 = curve_fit(dec_func.exponential_decline, t,each_decline,p0=(initial_guess_for_q_i,0.01), bounds = ([0,0.0002738226],[initial_guess_for_q_i*2, 1]),method = "trf")
			list_of_all_fits_exponential.append(popt_1)
		except Exception as e:
			list_of_all_fits_exponential.append(["No_Model"])
			print("Error: "+str(e))
		try:
			popt_2, pcov_2 = curve_fit(dec_func.harmonic_decline, t,each_decline,p0=(initial_guess_for_q_i,0.01), bounds = ([0,0.0002738226],[initial_guess_for_q_i*2, 1]),method = "trf")
			list_of_all_fits_harmonic.append(popt_2)
		except Exception as e:
			list_of_all_fits_harmonic.append(["No_Model"])
			print("Error: "+str(e))
		try:
			popt_3, pcov_3 = curve_fit(dec_func.hyperbolic_decline, t,each_decline,p0=(initial_guess_for_q_i,0.01,0.7), bounds = ([0,0.0002738226,0.6],[initial_guess_for_q_i*2, 1, 4]),method = "trf" )
			list_of_all_fits_hyperbolic.append(popt_3)
		except Exception as e:
			list_of_all_fits_hyperbolic.append(["No_Model"])
			print("Error: "+str(e))
		try:
			popt_4, pcov_4 = curve_fit(dec_func.hyp2exp, t,each_decline,p0=(initial_guess_for_q_i,0.01,0.7,0.1), bounds = ([0,0.0002738226,0.6,0],[initial_guess_for_q_i*2, 1, 4,0.5]),method = "trf")
			list_of_all_fits_hyp2exp.append(popt_4)
		except Exception as e:
			list_of_all_fits_hyp2exp.append(["No_Model"])
			print("Error: "+str(e))
	
	list_of_prediction_declines = np.split(y1,indexes_for_prediction)
	forecast_from = len(list_of_prediction_declines[-1])+ 1
	forecast_until = forecast_from + 1100
	t_forecast = np.array(list(range(forecast_from,forecast_until+1))) 
	
	#Check how the trained model fits the training data
	y_pred_exponential = []
	for index,each_model in enumerate(list_of_all_fits_exponential):
		current_length = len(list_of_prediction_declines[index])
		t = np.array(list(range(current_length))) + 1
		if index != 0 and "No_Model" not in list(each_model):
			y_pred_exponential = y_pred_exponential + list(dec_func.exponential_decline(t,each_model[0],each_model[1]))
		elif index == 0 and len(list_of_subdeclines)==1:
			y_pred_exponential = y_pred_exponential + list(dec_func.exponential_decline(t,each_model[0],each_model[1]))			
		else:
			y_pred_exponential = y_pred_exponential + [float('nan')]*current_length	
			
	y_pred_harmonic = []			
	for index,each_model in enumerate(list_of_all_fits_harmonic):
		current_length = len(list_of_prediction_declines[index])
		t = np.array(list(range(current_length))) + 1
		if index!=0 and "No_Model" not in list(each_model):
			y_pred_harmonic = y_pred_harmonic + list(dec_func.harmonic_decline(t,each_model[0],each_model[1]))
		elif index == 0 and len(list_of_subdeclines)==1:
			y_pred_harmonic = y_pred_harmonic + list(dec_func.harmonic_decline(t,each_model[0],each_model[1]))
		else:
			y_pred_harmonic = y_pred_harmonic + [float('nan')]*current_length	

	y_pred_hyperbolic = []			
	for index,each_model in enumerate(list_of_all_fits_hyperbolic):
		current_length = len(list_of_prediction_declines[index])
		t = np.array(list(range(current_length))) + 1
		if index!=0 and "No_Model" not in list(each_model):
			y_pred_hyperbolic = y_pred_hyperbolic + list(dec_func.hyperbolic_decline(t,each_model[0],each_model[1],each_model[2]))
		elif index == 0 and len(list_of_subdeclines)==1:
			y_pred_hyperbolic = y_pred_hyperbolic + list(dec_func.hyperbolic_decline(t,each_model[0],each_model[1],each_model[2]))
		else:
			y_pred_hyperbolic = y_pred_hyperbolic + [float('nan')]*current_length	
	
	y_pred_hyp2exp = []
	for index,each_model in enumerate(list_of_all_fits_hyp2exp):
		current_length = len(list_of_prediction_declines[index])
		t = np.array(list(range(current_length))) + 1
		if index!=0 and "No_Model" not in list(each_model):
			y_pred_hyp2exp = y_pred_hyp2exp + list(dec_func.hyp2exp(t,each_model[0],each_model[1],each_model[2],each_model[3]))
		elif index == 0 and len(list_of_subdeclines)==1:
			y_pred_hyp2exp = y_pred_hyp2exp + list(dec_func.hyp2exp(t,each_model[0],each_model[1],each_model[2],each_model[3]))
		else:
			y_pred_hyp2exp = y_pred_hyp2exp + [float('nan')]*current_length	
			

	#Forecast for three years in the future based on recent decline.				
	if "No_Model" not in list(list_of_all_fits_exponential[-1]):
		exponential_forecast = dec_func.exponential_decline(t_forecast,list_of_all_fits_exponential[-1][0],list_of_all_fits_exponential[-1][1])
	else:
		exponential_forecast = "No_Forecast"

	
	if "No_Model" not in list(list_of_all_fits_harmonic[-1]):
		harmonic_forecast = dec_func.harmonic_decline(t_forecast,list_of_all_fits_harmonic[-1][0],list_of_all_fits_harmonic[-1][1])
	else:
		harmonic_forecast = "No_Forecast"


	if "No_Model" not in list(list_of_all_fits_hyperbolic[-1]):
		hyperbolic_forecast = dec_func.hyperbolic_decline(t_forecast,list_of_all_fits_hyperbolic[-1][0],list_of_all_fits_hyperbolic[-1][1],list_of_all_fits_hyperbolic[-1][2])
	else:
		hyperbolic_forecast = "No_Forecast"
	

	if "No_Model" not in list(list_of_all_fits_hyp2exp[-1]):
		hyp2exp_forecast = dec_func.hyp2exp(t_forecast,list_of_all_fits_hyp2exp[-1][0],list_of_all_fits_hyp2exp[-1][1],list_of_all_fits_hyp2exp[-1][2],list_of_all_fits_hyp2exp[-1][3])
	else:
		hyp2exp_forecast = "No_Forecast"
			
	list_save = []
	list_save.append(y1)
	list_save.append(y_pred_exponential)
	list_save.append(y_pred_harmonic)
	list_save.append(y_pred_hyperbolic)
	list_save.append(y_pred_hyp2exp)
	list_save.append(exponential_forecast)
	list_save.append(harmonic_forecast)
	list_save.append(hyperbolic_forecast)
	list_save.append(hyp2exp_forecast)
	list_save.append(len(list_of_subdeclines[-1]))
	list_save.append(outliers)
		
	return list_save	
