"""
This file contains code to reduce signal to basic features: global approach such as min,max,mean,snr,d1max,d1min.
"""
import numpy as np

def reduce_signal_to_basic_features(signal):
	fmean = np.mean(signal)
	fmin = np.min(signal)
	fmax = np.max(signal)
	fstd = np.std(signal)
	dx = 1
	dydx = np.diff(signal)/dx
	fd1min = np.min(dydx)
	fd1max = np.max(dydx)
	return fmean,fmin,fmax,fstd,fd1min,fd1max
	

