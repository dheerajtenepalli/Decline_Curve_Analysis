"""
This file contains code to all decline functions.
"""

#Importing necessary libraries
import numpy as np


def exponential_decline(t,q_i,d):
	"""
	Description: The exponential decline function returns values for the given parameters.
	Input: t, q_i, d
	Output: Array of values
	"""
	return q_i*np.exp(-1*d*t)

	
def hyperbolic_decline(t,q_i,d,b):
	"""
	Description: The hyperbolic decline function returns values for the given parameters.
	Input: t, q_i, d, b
	Output: Array of values
	"""

	return q_i*((1+b*d*t)**(-1/b))

		
def harmonic_decline(t,q_i,d):
	"""
	Description: The harmonic decline function returns values for the given parameters.
	Input: t, q_i, d
	Output: Array of values
	"""

	return q_i*((1+d*t)**(-1))

		
def hyp2exp(t,q_i,d,b,beta):
	"""
	Description: The hyperbolic to exponential decline function returns values for the given parameters.
	Input: t, q_i, d, b, beta
	Output: Array of values
	"""
	return q_i * ( ( ((1-beta)**b)*np.exp(-d*t) ) / ( 1- (beta*np.exp(-d*t)) )**b )
	
