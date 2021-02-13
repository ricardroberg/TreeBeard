import os, csv, xlrd
import json

def readFile(filename):
	filenamesplited = filenamme.split('.')[-1] # To get file extension

# Try open file for CSV and XLRD as Bytecode

# Read the first line/HEADER (assuming 1 header only)

# Read All Collums and separete each one into a dict with value and number
# of occurances {'word1':2, 'word2':7, so on and so forth}
# Maybe i could use Ordered Dict, but no concern at the moment

# The collum with more repeated ocurrence will be the first branch of tree
# The number of relationships of adjacence columns will dictate the order of 
# next branchs
# Ex: First column got only one occurence that repeat 14 times
# of 2 ocurrences, 1 repeat itself 2 times and the other 12 times

# Count number of itens in each dictionary, cont his occurrences and compare a dictionary with eachother
# Create a list with the order in which each dictionary should appear

#List it



# TO BE USED LATTER (OR NOT)
# SNIPPET FROM STACKOVERFLOW
# https://stackoverflow.com/questions/3239207/how-can-i-open-an-excel-file-in-python

# from xlrd import open_workbook

# book = open_workbook('simple.xls',on_demand=True)
# for name in book.sheet_names():
#     if name.endswith('2'):
#         sheet = book.sheet_by_name(name)

#         # Attempt to find a matching row (search the first column for 'john')
#         rowIndex = -1
#         for cell in sheet.col(0): # 
#             if 'john' in cell.value:
#                 break

#         # If we found the row, print it
#         if row != -1:
#             cells = sheet.row(row)
#             for cell in cells:
#                 print cell.value

#         book.unload_sheet(name) 