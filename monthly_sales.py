# monthly_sales.py

# 2019-02-15 
# Kuran Pran Malhotra
# OPIM 243-30
# Attribution: fantastic notes located at https://github.com/prof-rossetti/georgetown-opim-243-201901/tree/e2d64e2d74621f3ff070175954878ba3f1562388/notes

# TODO: import some modules and/or packages here

import matplotlib as plot
import csv
import statistics as st
# import easygui as eg
import tkinter
from tkinter import filedialog

# TODO: write some Python code here to produce the desired functionality...

# adapted from: csv-mgmt/write_teams.py

# csv_file_path = eg.fileopenbox(default="*", filetypes="*")

def getfile():

    tkinter.Tk().withdraw() # Close the root window
    file_path = filedialog.askopenfilename()
    



print("================")
# # csv_file_path = str
csv_file = getfile()
print(type(csv_file))

# with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
#     writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
#     writer.writeheader() # uses fieldnames set above
#     writer.writerow({"city": "New York", "name": "Yankees"})
#     writer.writerow({"city": "New York", "name": "Mets"})
#     writer.writerow({"city": "Boston", "name": "Red Sox"})
#     writer.writerow({"city": "New Haven", "name": "Ravens"})



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