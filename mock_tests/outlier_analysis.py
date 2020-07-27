"""
This file contains code for outlier analysis. There are two types of outlier analysis. Global and Local.
1. First one is global outlier analysis. Here we consider the entire data distribution.
2. Local outliers are operational outliers indentified in each decline.
"""		

#Importing necessary libraries
import numpy as np
from sklearn.ensemble import IsolationForest
from scipy import stats


def remove_outliers(data):
	"""
	Description: Analyzes and removes outlier based on machine learning algorithms.	
	Input: Gas or oil data for a specific well with outliers
	Output: Data without global or local outliers. 
	"""	
	data = np.array(data).reshape(-1,1)
	algorithm = IsolationForest(contamination = 0.01)
	algorithm.fit(data)
	predictions = algorithm.predict(data)
	outliers = 	data[np.where(predictions == -1)]
	normal_data = data[np.where(predictions != -1)]
	outliers = outliers.reshape(1,len(outliers))[0]
	normal_data = normal_data.reshape(1,len(normal_data))[0]
	return normal_data,outliers

