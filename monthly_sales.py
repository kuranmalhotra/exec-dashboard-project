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

# TODO: write some Python code here to produce the desired functionality...

### adapted from: prof-rossetti notes on csv mgmt
### THE BELOW CODE CAME FROM THE HELP OF https://stackoverflow.com/questions/41600684/put-file-path-in-global-variable-from-browse-button-with-tkinter
### AND ALSO FROM https://docs.python.org/3/library/tkinter.html#file-handlers

csv_file_path = ""

def getfile():

# Get the file: 

    tkinter.Tk().withdraw() # Close the root window
    global csv_file_path
    csv_file_path = filedialog.askopenfilename()

# Data validation on the file: 

    print(csv_file_path)
    response = input("Is the above filepath correct? (TRUE/FALSE): ")
    if response != "TRUE":
	    getfile() #<--Honestly shocked that I can recursively call the function, that's pretty cool

# 

getfile()

# print("-----------------------")


with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    for row in reader:
        print(row["date"], row["product"], row["unit price"],row["units sold"],row["sales price"])



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