import pandas as pd
import numpy as np

#Prepare data for preprocessing.
def prepare_data(df):
	"""
	Description: This function prepares data for preprocessing.
	Input: df, df is a data frame containing train_ops_results.csv
	Output: Dictionary with well_num as keys and well data dataframes as values.
	"""
	try:
		if "WELL_NUM" in df.columns: 
			all_wells = list(df["WELL_NUM"].unique())
			list_all_wells = []
			gas_dictionary = df.groupby("WELL_NUM")["GROSS_GAS_MCF"].apply(list).to_dict()
			oil_dictionary = df.groupby("WELL_NUM")["GROSS_OIL_BBLS"].apply(list).to_dict()
			#Converting to dataframes with columns as wells.
			gas_data_frame = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in gas_dictionary.items() ]))
			oil_data_frame = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in oil_dictionary.items() ])) 
			#Adding an indentifier such as "gas" or "oil" to the name of columns
			column_name_gas = list(gas_data_frame.columns)
			column_name_gas = [s + "_gas" for s in column_name_gas]
			gas_data_frame.columns = column_name_gas
			column_name_oil = list(oil_data_frame.columns)
			column_name_oil = [s + "_oil" for s in column_name_oil]
			oil_data_frame.columns = column_name_oil
			#Converting dataframe to a list of pandas series objects.
			for index,each_pandas_series in enumerate(gas_data_frame):
				list_all_wells.append(gas_data_frame[each_pandas_series])
			for index,each_pandas_series in enumerate(oil_data_frame):
				list_all_wells.append(oil_data_frame[each_pandas_series])			
		return 	list_all_wells
	except Exception as e:
		print("Error:"+str(e))
