#!/usr/bin/env python3
import pandas as pd
input_file = 'excel_files\\sales_2013.xlsx'
output_file = 'excel_files\\1pandas_output.xls'
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float)>2000.0]
writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
