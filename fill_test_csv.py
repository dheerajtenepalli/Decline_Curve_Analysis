"""
This file contains code to fill test csv using the evaluation results.
"""

import pickle
import pandas as pd

#Load test and evaluation resuts csv files
test_csv = pd.read_csv("test_ops_results_blank.csv")
eval_results = pd.read_csv("evaluation_results.csv")

#Initialize forecast variables
GROSS_OIL_BBLS = []
GROSS_GAS_MCF = []
GROSS_OIL_BBLS_exp = [] 	
GROSS_OIL_BBLS_harm = [] 	
GROSS_OIL_BBLS_hyp = [] 	
GROSS_OIL_BBLS_hyp2exp = [] 	
GROSS_GAS_MCF_exp = []
GROSS_GAS_MCF_harm = []
GROSS_GAS_MCF_hyp = []
GROSS_GAS_MCF_hyp2exp = []

#Count the number of values to forecast for each well in the test set.
count_dictionary_well = dict()
for each_well in test_csv["WELL_NUM"]:
	if each_well not in count_dictionary_well.keys():
		count_dictionary_well[each_well] = [1,False,False,[],[],[],[],[],[],[],[],[],[]]
	else:
		count_dictionary_well[each_well][0] += 1

		
#Fill oil declines for all wells in test set		
for each_well in test_csv["WELL_NUM"]:
	if not count_dictionary_well[each_well][1]:
		each_well_parameters = each_well + "_oil_parameters.txt"
		each_well_full_name = each_well + "_oil"
		
		with open("saved_model_parameters/"+each_well_parameters, "rb") as fp: 
			saved_parameters = pickle.load(fp)
			
		count_dictionary_well[each_well][3] = saved_parameters[5][:count_dictionary_well[each_well][0]]	
		count_dictionary_well[each_well][4] = saved_parameters[6][:count_dictionary_well[each_well][0]]	
		count_dictionary_well[each_well][5] = saved_parameters[7][:count_dictionary_well[each_well][0]]	
		count_dictionary_well[each_well][6] = saved_parameters[8][:count_dictionary_well[each_well][0]]
		count_dictionary_well[each_well][1] = True

		best_model = eval_results[eval_results["WELL_NUM"]==each_well_full_name].values[0][-2]
		if best_model == "exp":
			count_dictionary_well[each_well][11] = saved_parameters[5][:count_dictionary_well[each_well][0]]
		elif best_model == "harm":
			count_dictionary_well[each_well][11] = saved_parameters[6][:count_dictionary_well[each_well][0]]
		elif best_model == "hyp":
			count_dictionary_well[each_well][11] = saved_parameters[7][:count_dictionary_well[each_well][0]]
		elif best_model == "hyp2exp":
			count_dictionary_well[each_well][11] = saved_parameters[8][:count_dictionary_well[each_well][0]]

		GROSS_OIL_BBLS.extend(count_dictionary_well[each_well][11])
		GROSS_OIL_BBLS_exp.extend(count_dictionary_well[each_well][3]) 	
		GROSS_OIL_BBLS_harm.extend(count_dictionary_well[each_well][4]) 	
		GROSS_OIL_BBLS_hyp.extend(count_dictionary_well[each_well][5]) 	
		GROSS_OIL_BBLS_hyp2exp.extend(count_dictionary_well[each_well][6])
			
					
#Fill gas declines for all wells in test set		
for each_well in test_csv["WELL_NUM"]:
	if not count_dictionary_well[each_well][2]:
		each_well_parameters = each_well + "_gas_parameters.txt"
		each_well_full_name = each_well + "_gas"

		with open("saved_model_parameters/"+each_well_parameters, "rb") as fp: 
			saved_parameters = pickle.load(fp)
			
		count_dictionary_well[each_well][7] = saved_parameters[5][:count_dictionary_well[each_well][0]]	
		count_dictionary_well[each_well][8] = saved_parameters[6][:count_dictionary_well[each_well][0]]	
		count_dictionary_well[each_well][9] = saved_parameters[7][:count_dictionary_well[each_well][0]]	
		count_dictionary_well[each_well][10] = saved_parameters[8][:count_dictionary_well[each_well][0]]
		count_dictionary_well[each_well][2] = True
		
		best_model = eval_results[eval_results["WELL_NUM"]==each_well_full_name].values[0][-2]
		if best_model == "exp":
			count_dictionary_well[each_well][12] = saved_parameters[5][:count_dictionary_well[each_well][0]]
		elif best_model == "harm":
			count_dictionary_well[each_well][12] = saved_parameters[6][:count_dictionary_well[each_well][0]]
		elif best_model == "hyp":
			count_dictionary_well[each_well][12] = saved_parameters[7][:count_dictionary_well[each_well][0]]
		elif best_model == "hyp2exp":
			count_dictionary_well[each_well][12] = saved_parameters[8][:count_dictionary_well[each_well][0]]
		

		GROSS_GAS_MCF.extend(count_dictionary_well[each_well][12])
		GROSS_GAS_MCF_exp.extend(count_dictionary_well[each_well][7]) 	
		GROSS_GAS_MCF_harm.extend(count_dictionary_well[each_well][8]) 	
		GROSS_GAS_MCF_hyp.extend(count_dictionary_well[each_well][9]) 	
		GROSS_GAS_MCF_hyp2exp.extend(count_dictionary_well[each_well][10]) 
		
#Convert the results to a dataframe.		
test_csv["GROSS_OIL_BBLS"] = GROSS_OIL_BBLS
test_csv["GROSS_GAS_MCF"] = GROSS_GAS_MCF
test_csv["GROSS_OIL_BBLS_hyp2exp"] = GROSS_OIL_BBLS_hyp2exp
test_csv["GROSS_GAS_MCF_exp"] = GROSS_GAS_MCF_exp

test_csv["GROSS_OIL_BBLS_exp"] = GROSS_OIL_BBLS_exp
test_csv["GROSS_OIL_BBLS_harm"] = GROSS_OIL_BBLS_harm
test_csv["GROSS_OIL_BBLS_hyp"] = GROSS_OIL_BBLS_hyp

test_csv["GROSS_GAS_MCF_harm"] = GROSS_GAS_MCF_harm
test_csv["GROSS_GAS_MCF_hyp"] = GROSS_GAS_MCF_hyp
test_csv["GROSS_GAS_MCF_hyp2exp"] = GROSS_GAS_MCF_hyp2exp

test_csv.to_csv("test_ops_results_blank.csv",index = False)
print("Forecasts are filled and stored in test_ops_results_blank.csv")
		




 		
	
		
		
