# "**" in the math equation in this code means power in python.
# So, in python x to the power y is x**y.
# t is the time period. Time is converted from dates and represented in numbers such as 1,2,3,4,5.

#Importing necessary libraries
import numpy as np


def exponential_decline(t,q_i,d):
    return q_i*np.exp(-1*d*t)

	
def hyperbolic_decline(t,q_i,d,b):
	return q_i*((1+b*d*t)**(-1/b))

		
def harmonic_decline(t,q_i,d):
	return q_i*((1+d*t)**(-1))

		
def hyp2exp(t,q_i,d,b,beta):
	return q_i * ( ( ((1-beta)**b)*np.exp(-d*t) ) / ( 1- (beta*np.exp(-d*t)) )**b )
	
