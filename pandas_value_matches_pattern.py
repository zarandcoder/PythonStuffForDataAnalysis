#!/usr/bin/env python3
import pandas as pd
import sys
input_file = 'excel_files\\sales_2013.xlsx'
output_file = 'excel_files\\3pandas_output.xls'
data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith("V")]
writer = pd.ExcelWriter(output_file)
data_frame_value_matches_pattern.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()
