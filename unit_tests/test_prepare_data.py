import pandas as pd
import numpy as np
import prepare_data

#This mock train csv contains only the first rows of data. There is only one well in the sample training data.
#So, the length of returned list should contain data for oil and gas.
#That makes the length of the list equal to 2.
first_row = ["WellNum-17655","1/1/2000",0,0,0,0] 
columns = ["WELL_NUM","DAILY_RDG_DATE","GROSS_OIL_BBLS","GROSS_WTR_BBLS","GROSS_GAS_MCF","CASING_PRESS"]

df = pd.DataFrame(columns = columns)
df.loc[0] = first_row

def test_prepare_data():
	assert len(prepare_data.prepare_data(df)) == 2

