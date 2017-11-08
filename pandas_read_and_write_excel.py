#!/usr/bin/env python3
import pandas as pd
input_file = 'excel_files\\sales_2013.xlsx'
output_file = 'excel_files\\4output.xls'
data_frame = pd.read_excel(input_file, sheetname='january_2013')
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_2013_output', index=False)
writer.save()

