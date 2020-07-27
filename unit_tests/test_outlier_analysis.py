
import outlier_analysis
import numpy as np

#Mock unit tests 

#Operational outlier
unit_test_array_1 = [1,2,3,567,4,5,6,7,8]
#Negative outlier
unit_test_array_2 = [-200,27,29,28,27,25,22,21,19]
#Down time outlier
unit_test_array_3 = [146.84,108.58,98.03,0,0,158.11,121.72]
#Data distribution outlier
unit_test_array_4 = [108.58,98.03,5,158.11,121.72,100]

def test_remove_outliers():
	assert np.isclose(outlier_analysis.remove_outliers(unit_test_array_1)[0],np.array([1,2,3,4,5,6,7,8])).all()
	assert np.isclose(outlier_analysis.remove_outliers(unit_test_array_1)[1],np.array([567])).all()
	assert np.isclose(outlier_analysis.remove_outliers(unit_test_array_2)[0],np.array([27,29,28,27,25,22,21,19])).all()
	assert np.isclose(outlier_analysis.remove_outliers(unit_test_array_2)[1],np.array([-200])).all()
	assert np.isclose(outlier_analysis.remove_outliers(unit_test_array_4)[0],np.array([108.58,98.03,158.11,121.72,100])).all()
	assert np.isclose(outlier_analysis.remove_outliers(unit_test_array_4)[1],np.array([5])).all()
