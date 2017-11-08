#!/usr/bin/env python3
import csv
import sqlite3
import sys

input_file = sys.argv[1]


#Creates a connection object that represents the database an creates it in RAM.
con = sqlite3.connect('Suppliers.db') 
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
                    (Supplier_Name VARCHAR(20),
                    Invoice_Number VARCHAR(20),
                    Part_Number VARCHAR(20),
                    Cost FLOAT,
                    Purchase_Date DATE);"""
#Carry out the SQL-Command
c.execute(create_table)
#Saving changes
con.commit()



file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data) #question marks serve as placeholders for the values.
con.commit()
print('')

output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
