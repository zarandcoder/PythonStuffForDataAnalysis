#!/usr/bin/env python3
import pandas as pd
import sys
input_file = 'excel_files\\sales_2013.xlsx' #sys.argv[1]
output_file = 'excel_files\\2pandas_output.xls'#sys.argv[2]
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
important_dates = ['31/12/2013', '30/11/2013']
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)]
writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name = 'jan_2013_output', index=False)
writer.save()
