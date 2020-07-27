import numpy as np
import decline_functions as dec_func

#Mock tests
t = np.array([1,2,3])
q_i = 100
d = 0.01
b = 0.6
beta = 0.5

def test_exponential_decline():
	assert np.isclose(dec_func.exponential_decline(t,q_i,d),np.array([99.00498337,98.01986733,97.04455335])).all()
 
def test_hyperbolic_decline():
	assert np.isclose(dec_func.hyperbolic_decline(t,q_i,d,b),np.array([99.00794174,98.03153715,97.0704486])).all()
 
def test_harmonic_decline():
	assert np.isclose(dec_func.harmonic_decline(t,q_i,d),np.array([99.00990099,98.03921569,97.08737864])).all()

def test_hyp2exp_decline():
	assert np.isclose(dec_func.hyp2exp(t,q_i,d,b,beta),np.array([98.41857853,96.87345001,95.36336546])).all()


