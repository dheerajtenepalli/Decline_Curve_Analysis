import numpy as np
import signal_features
unit_test = [1,2,3,4,5,6,11,23,245,12,64,123,12]

def test_reduce_signal_to_basic_features():
	assert signal_features.reduce_signal_to_basic_features(unit_test)[0] == 39.30769230769231 
	assert signal_features.reduce_signal_to_basic_features(unit_test)[1] == 1 
	assert signal_features.reduce_signal_to_basic_features(unit_test)[2] == 245 
	assert signal_features.reduce_signal_to_basic_features(unit_test)[3] == 68.04566861859378 
	assert signal_features.reduce_signal_to_basic_features(unit_test)[4] == -233.0 
	assert signal_features.reduce_signal_to_basic_features(unit_test)[5] ==  222.0 
