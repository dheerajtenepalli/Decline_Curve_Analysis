import evaluate
import numpy as np
import pickle
import math
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#Mock test values 
y_actual = [100,99,98,87,70]
y_pred_exponential = [99,98,97,85,69]
y_pred_harmonic = [99.1,99,98.5,97,75]
y_pred_hyperbolic = [100,98,95,85,65]
y_pred_hyp2exp = [100,99.1,98,85,64]

def test_get_scores():
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[0] == -2.1588830833596715
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[1] == -5.327123292259293
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[2] == -7.673515968169928
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[3] == -5.378258845738287
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[4] == 3.959456058662778
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[5] == 11.88005658091183
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[6] == 17.74603827068842
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[7] == 12.007895464609316
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[8] == 1.2649110640673518
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[9] == 2.792848008753788
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[10] ==  5.021155245558536 
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[11] ==  2.8287806560424578
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[12] == 0.8
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[13] == 0.8
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[14] == 0.8
	assert evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp)[15] == 0.8

#print(evaluate.get_scores(y_actual,y_pred_exponential,y_pred_harmonic,y_pred_hyperbolic,y_pred_hyp2exp))	