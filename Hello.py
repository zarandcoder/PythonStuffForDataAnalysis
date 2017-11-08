#!/usr/bin/bash/env python3
from xlrd import open_workbook
import sys
input_file = sys.argv[1]
workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)
