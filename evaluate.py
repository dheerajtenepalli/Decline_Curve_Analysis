"""
This file contains code for evaluation based on RMSE,AIC,BIC scores and slope of the decline.
"""
import numpy as np
import pickle
import math
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from scipy import stats


def get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp):
	"""
	Description: This function is the one which calculates AIC, BIC and RMSE scores.
	Input: Actual Oil and Gas values for the last decline and also the predicted values for the last decline.
	Output: AIC,BIC,RMSE,Slope scores for all fitting models such as exp,harmonic,hyperbolic,hyp2exp. A total of 16 parameters.
	"""
	try:
		#Fill Nans
		y_actual = np.nan_to_num(np.array(y_actual))
		y_pred_exponential = np.nan_to_num(np.array(y_pred_exponential))
		y_pred_hyperbolic = np.nan_to_num(np.array(y_pred_hyperbolic))
		y_pred_harmonic = np.nan_to_num(np.array(y_pred_harmonic))
		y_pred_hyp2exp = np.nan_to_num(np.array(y_pred_hyp2exp))
		
		#Remove zeroes from evaluation
		non_zero_index = np.nonzero(y_actual) 
		
		if len(non_zero_index[0]) == 0:
			non_zero_index = list(range(len(y_actual)))
		mse_exp = mean_squared_error(y_actual[non_zero_index],y_pred_exponential[non_zero_index])
		mse_hyp = mean_squared_error(y_actual[non_zero_index],y_pred_hyperbolic[non_zero_index])
		mse_harm = mean_squared_error(y_actual[non_zero_index],y_pred_harmonic[non_zero_index])
		mse_hyp2exp = mean_squared_error(y_actual[non_zero_index],y_pred_hyp2exp[non_zero_index])
		
		#AIC scores, note that k in AIC is equal to 2 and the number of parameters is 1.
		aic_exp = 2 - 2*np.log(mse_exp*len(y_pred_exponential[non_zero_index]))
		aic_hyp = 2 - 2*np.log(mse_hyp*len(y_pred_hyperbolic[non_zero_index]))
		aic_harm = 2 - 2*np.log(mse_harm*len(y_pred_harmonic[non_zero_index]))
		aic_hyp2exp = 2 - 2*np.log(mse_hyp2exp*len(y_pred_hyp2exp[non_zero_index]))

		#BIC scores, k = 1 here
		bic_exp = len(y_pred_exponential[non_zero_index])*np.log(mse_exp) + np.log(len(y_pred_exponential[non_zero_index]))
		bic_hyp = len(y_pred_hyperbolic[non_zero_index])*np.log(mse_hyp) + np.log(len(y_pred_hyperbolic[non_zero_index]))
		bic_harm = len(y_pred_harmonic[non_zero_index])*np.log(mse_harm) + np.log(len(y_pred_harmonic[non_zero_index]))
		bic_hyp2exp = len(y_pred_hyp2exp[non_zero_index])*np.log(mse_hyp2exp) + np.log(len(y_pred_hyp2exp[non_zero_index]))

		#RMSE calculations
		rmse_for_exp = math.sqrt(mse_exp)
		rmse_for_hyp = math.sqrt(mse_hyp)
		rmse_for_harm = math.sqrt(mse_harm)
		rmse_for_hyp2exp = math.sqrt(mse_hyp2exp)
		
		#Calculate slope. Slope percentage tells us the steepness of the curve.
		negslope_exp_percentage = len(y_pred_exponential[np.where(np.diff(y_pred_exponential) < 0)])/len(y_pred_exponential)
		negslope_hyp_percentage = len(y_pred_hyperbolic[np.where(np.diff(y_pred_hyperbolic) < 0)])/len(y_pred_hyperbolic)
		negslope_harm_percentage = len(y_pred_harmonic[np.where(np.diff(y_pred_harmonic) < 0)])/len(y_pred_harmonic)
		negslope_hyp2exp_percentage = len(y_pred_hyp2exp[np.where(np.diff(y_pred_hyp2exp) < 0)])/len(y_pred_hyp2exp)

		return aic_exp,aic_hyp,aic_harm,aic_hyp2exp,bic_exp,bic_hyp,bic_harm,bic_hyp2exp,rmse_for_exp,rmse_for_hyp,rmse_for_harm,rmse_for_hyp2exp,negslope_exp_percentage,negslope_hyp_percentage,negslope_harm_percentage,negslope_hyp2exp_percentage
		
	except Exception as e:
		print(str(e))
		return "No_model_found"
	
"""			
Note_1: Start the evaluation on the test set for all wells.
Note_2: The evaluation is done for only the last decline actual and predicted values.
Expected evaluation results: best model for each_well's oil and gas declines.
"""

#Load the test csv. 
test_csv = pd.read_csv("test_ops_results_blank.csv")
unique_wells_in_test_data = list(test_csv["WELL_NUM"].unique())
all_outputs = []

#Iterate in a for loop 
for index,each_well in enumerate(unique_wells_in_test_data):

	#Evaluate on oil data
	each_well_parameters = each_well + "_oil_parameters.txt"
	
	#Load Saved Parameters
	with open("saved_model_parameters/"+each_well_parameters, "rb") as fp: 
		saved_parameters = pickle.load(fp)
		
	evaluate_from = len(saved_parameters[0])-saved_parameters[-2]
	output = get_scores(saved_parameters[0][evaluate_from:],saved_parameters[1][evaluate_from:],saved_parameters[2][evaluate_from:],saved_parameters[3][evaluate_from:],saved_parameters[4][evaluate_from:])
	if output != "No_model_found":
		output = list(output)
		best_aic = np.argmin(np.array(output[:4]))
		best_bic = np.argmin(np.array(output[4:8]))
		best_rmse = np.argmin(np.array(output[8:12]))
		mode = stats.mode(np.array([best_aic,best_bic,best_rmse]))		
	else:
		output = ["No_model_found"]*16
		mode = [0,1]
	
	#Find the best model for this well's oil decline.
	if mode[1] > 1:
		if mode[0] == 0:
			best_model = "exp"
		if mode[0] == 1:
			best_model = "hyp"
		if mode[0] == 2:
			best_model = "harm"
		if mode[0] == 3:
			best_model = "hyp2exp"
	else:
		best_model = "hyp2exp"

	output.append(each_well + "_oil")
	output.append(best_model)
	output.append(saved_parameters[-1])
	all_outputs.append(output)

	
	#Evaluate on gas data		
	each_well_parameters = each_well + "_gas_parameters.txt"
	
	#Load saved parameters
	with open("saved_model_parameters/"+each_well_parameters, "rb") as fp: 
		saved_parameters = pickle.load(fp)
		
	evaluate_from = len(saved_parameters[0])-saved_parameters[-2]
	output = get_scores(saved_parameters[0][evaluate_from:],saved_parameters[1][evaluate_from:],saved_parameters[2][evaluate_from:],saved_parameters[3][evaluate_from:],saved_parameters[4][evaluate_from:])
	if output != "No_model_found":
		output = list(output)
		best_aic = np.argmin(np.array(output[:4]))
		best_bic = np.argmin(np.array(output[4:8]))
		best_rmse = np.argmin(np.array(output[8:12]))
		mode = stats.mode(np.array([best_aic,best_bic,best_rmse]))		
	else:
		output = ["No_model_found"]*16
		mode = [0,1]

	#Find the best model for this well's gas decline.		
	if mode[1] > 1:
		if mode[0] == 0:
			best_model = "exp"
		if mode[0] == 1:
			best_model = "hyp"
		if mode[0] == 2:
			best_model = "harm"
		if mode[0] == 3:
			best_model = "hyp2exp"
	else:
		best_model = "exp"
		
	
	output.append(each_well + "_gas")
	output.append(best_model)
	output.append(saved_parameters[-1])
	all_outputs.append(output) 

#Write results to a csv
Evaluation_results = pd.DataFrame(all_outputs)	
Evaluation_results.columns = ["aic_exp","aic_hyp","aic_harm","aic_hyp2exp","bic_exp","bic_hyp","bic_harm","bic_hyp2exp","rmse_for_exp","rmse_for_hyp","rmse_for_harm","rmse_for_hyp2exp","negslope_exp_percentage","negslope_hyp_percentage","negslope_harm_percentage","negslope_hyp2exp_percentage","WELL_NUM","best_model","All_outliers"]
Evaluation_results.to_csv("evaluation_results.csv",index=False)
print("Evaluation Finished")