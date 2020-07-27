"""
This file contains code for evaluation based on RMSE,AIC,BIC scores and slope of the decline.
"""
import numpy as np
import pickle
import math
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp):
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
		
		#Calculate slope. Seperate curves with negative slopes from positive ones.
		negslope_exp_percentage = len(y_pred_exponential[np.where(np.diff(y_pred_exponential) < 0)])/len(y_pred_exponential)
		negslope_hyp_percentage = len(y_pred_hyperbolic[np.where(np.diff(y_pred_hyperbolic) < 0)])/len(y_pred_hyperbolic)
		negslope_harm_percentage = len(y_pred_harmonic[np.where(np.diff(y_pred_harmonic) < 0)])/len(y_pred_harmonic)
		negslope_hyp2exp_percentage = len(y_pred_hyp2exp[np.where(np.diff(y_pred_hyp2exp) < 0)])/len(y_pred_hyp2exp)

		return aic_exp,aic_hyp,aic_harm,aic_hyp2exp,bic_exp,bic_hyp,bic_harm,bic_hyp2exp,rmse_for_exp,rmse_for_hyp,rmse_for_harm,rmse_for_hyp2exp,negslope_exp_percentage,negslope_hyp_percentage,negslope_harm_percentage,negslope_hyp2exp_percentage
		
	except Exception as e:
		print(str(e))
		return "No_model_found"
	
			
