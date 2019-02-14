# monthly_sales.py

# 2019-02-15 
# Kuran Pran Malhotra
# OPIM 243-30
# Attribution: fantastic notes located at https://github.com/prof-rossetti/georgetown-opim-243-201901/tree/e2d64e2d74621f3ff070175954878ba3f1562388/notes

# TODO: import some modules and/or packages here

import matplotlib as plot
import csv
import statistics as st
import tkinter
from tkinter import filedialog
import os

# TODO: write some Python code here to produce the desired functionality...

### adapted from: prof-rossetti notes on csv mgmt
### THE BELOW CODE CAME FROM THE HELP OF https://stackoverflow.com/questions/41600684/put-file-path-in-global-variable-from-browse-button-with-tkinter
### AND ALSO FROM https://docs.python.org/3/library/tkinter.html#file-handlers

csv_file_path = ""
filename = ""
line = "=" * 50

def getfile():

# Get the file: 

    tkinter.Tk().withdraw() # Close the root window
    global csv_file_path
    global filename
    csv_file_path = filedialog.askopenfilename()
    filename = os.path.basename(csv_file_path) # <-- TY Stack Exchange!

# Data validation on the file: 

    print(line)
    print(csv_file_path)
    print(line)
    response = input("Is the above filepath for " + filename.upper() + " correct? ('TRUE' or 'FALSE'): ")
    if response != "TRUE":
	    getfile() #<--Honestly shocked that I can recursively call the function, that's pretty cool

# Introduction:
print(line)
print("Welcome to the Executive Dashboard. Please follow the prompts.")

getfile()
print(filename.upper())
f = list(filename.upper())
year = f[6] + f[7] + f[8] + f[9]
year = (int(year))
print(type(year))

print(line)

# with open(csv_file_path, "r") as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row["date"], row["product"], row["unit price"],row["units sold"],row["sales price"])
#     print(type(reader))

# 	for row in reader: 


# print("-----------------------")
# print("MONTH: March 2018")

# print("-----------------------")
# print("CRUNCHING THE DATA...")

# print("-----------------------")
# print("TOTAL MONTHLY SALES: $12,000.71")

# print("-----------------------")
# print("TOP SELLING PRODUCTS:")
# print("  1) Button-Down Shirt: $6,960.35")
# print("  2) Super Soft Hoodie: $1,875.00")
# print("  3) etc.")

# print("-----------------------")
# print("VISUALIZING THE DATA...")