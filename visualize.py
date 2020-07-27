"""
This file contains code to visualize the results. Please run this only after training.
"""

#Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pickle
import pandas as pd

def visualize():
	"""
	Description: This function is used to visualize both the data fit and also the forecast for all the wells in the test data.
	Input: test_csv and also saved_model_parameters from the training.
	Output: 2D graphs. Please note that you have to close the opened graph to continue plotting the next graph.
	"""	
	test_csv = pd.read_csv("test_ops_results_blank.csv")
	unique_wells_in_test_data = list(test_csv["WELL_NUM"].unique())
	for index,each_well in enumerate(unique_wells_in_test_data):
		each_well_parameters = each_well + "_oil_parameters.txt"
		with open("saved_model_parameters/"+each_well_parameters, "rb") as fp: 
			saved_parameters = pickle.load(fp)
		try:
			plt.plot(saved_parameters[0])	
			plt.plot(np.concatenate((saved_parameters[1],saved_parameters[5])),label = 'exp')	
			plt.plot(np.concatenate((saved_parameters[2],saved_parameters[6])),label = 'harmonic')	
			plt.plot(np.concatenate((saved_parameters[3],saved_parameters[7])),label = 'hyp')	
			plt.plot(np.concatenate((saved_parameters[4],saved_parameters[8])),label = 'hyp2exp')
			plt.xlabel("Time")
			plt.ylabel("Oil Production for "+str(each_well))
			plt.legend(loc='upper right')
			print("Graph is open now. Please close the graph to visualize the next result")
			plt.show()
		except Exception as e:
			print("Error: "+str(e))	
	for index,each_well in enumerate(unique_wells_in_test_data):
		each_well_parameters = each_well + "_gas_parameters.txt"
		with open("saved_model_parameters/"+each_well_parameters, "rb") as fp: 
			saved_parameters = pickle.load(fp)
		try:
			plt.plot(saved_parameters[0])	
			plt.plot(np.concatenate((saved_parameters[1],saved_parameters[5])),label = 'exp')	
			plt.plot(np.concatenate((saved_parameters[2],saved_parameters[6])),label = 'harmonic')	
			plt.plot(np.concatenate((saved_parameters[3],saved_parameters[7])),label = 'hyp')	
			plt.plot(np.concatenate((saved_parameters[4],saved_parameters[8])),label = 'hyp2exp')
			plt.xlabel("Time")
			plt.ylabel("Gas Production for "+str(each_well))
			plt.legend(loc='upper right')
			print("Graph is open now. Please close the graph to visualize the next result")
			plt.show()		
		except Exception as e:
			print("Error: "+str(e))
			
visualize()			