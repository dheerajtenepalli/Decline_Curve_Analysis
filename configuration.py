#Set bounds for exponential decline.
d_exp_min = float(0.0002738226) 
d_exp_max = float(1)
#Set bounds for harmonic decline.
d_harm_min = float(0.0002738226) 
d_harm_max = float(1)
#Set bounds for hyperbolic decline.
d_hyp_min = float(0.0002738226)
d_hyp_max = float(1)
b_hyp_min = float(0.6)
b_hyp_max = float(4)
#Set bounds for hyperbolic to exponential decline.
d_hyp2exp_min = float(0.0002738226)
d_hyp2exp_max = float(1)
b_hyp2exp_min = float(0.6)
b_hyp2exp_max = float(4)
beta_hyp2exp_min = float(0) 
beta_hyp2exp_max =  float(0.5)

#Set bounds for EUR. The idea is to stop forecasting when 2bbls/day of rate is achieved consistently. Feel free to change this.
#Normally this values should be close to zero.
oil_stop_forecast_when = 2
gas_stop_forecast_when = 4

#Set other parameters.
minimum_peak_distance = int(180)
find_initial_peak_within_these_points = int(180)
minimum_points_in_each_decline = 7
height_multiplier = 0.5
minimum_width_peak = 7

#Set this to False if fit and forecast required for all wells in the training data.
only_fit_and_forecast_for_wells_in_test_set = True

#Set Multiprocessing flag to False or True, Setting this to true makes the code run faster.
multiprocessing_flag = True

