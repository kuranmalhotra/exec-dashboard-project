# monthly_sales.py

# 2019-02-15 
# Kuran Pran Malhotra
# OPIM 243-30
# Attribution: fantastic notes located at https://github.com/prof-rossetti/georgetown-opim-243-201901/tree/e2d64e2d74621f3ff070175954878ba3f1562388/notes

# TODO: import some modules and/or packages here

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pds
import statistics as st
import tkinter
from tkinter import filedialog
import os
import datetime as dt

# TODO: write some Python code here to produce the desired functionality...

### adapted from: prof-rossetti notes on csv mgmt
### THE BELOW CODE CAME FROM THE HELP OF https://stackoverflow.com/questions/41600684/put-file-path-in-global-variable-from-browse-button-with-tkinter
### AND ALSO FROM https://docs.python.org/3/library/tkinter.html#file-handlers
### Matt Gallea helped me pivot from the csv package to the pandas package; it's much more user friendly. 

csv_file_path = ""
filename = ""
line = "=" * 50

def getfile():
	# Get the filepath and data validation on the file: 

    tkinter.Tk().withdraw() # Close the root window
    global csv_file_path
    global filename
    csv_file_path = filedialog.askopenfilename()
    filename = os.path.basename(csv_file_path) # <-- TY Stack Exchange!



    print(line)
    print(csv_file_path)
    print(line)
    response = input("Is the above filepath for " + filename.upper() + " correct? ('TRUE' or 'FALSE'): ")
    if response != "TRUE":
	    getfile() # <-- Honestly shocked that I can recursively call the function, that's pretty cool

# Introduction:
print(line)
print("")
print("Welcome to the Executive Dashboard. Please follow the prompts.")
print("")
print(line)
getfile()

# Parse year and month from file name:

f = list(filename.upper())
year = f[6] + f[7] + f[8] + f[9]
year = (int(year))
month = f[10] + f[11]
month = (int(month))
month_name = str

def convert_month():
	global month_name
	if month == 1:
		month_name = "January"
	elif month == 2:
		month_name = "February"
	elif month == 3:
		month_name = "March"
	elif month == 4:
		month_name = "April"
	elif month == 5:
		month_name = "May"
	elif month == 6:
		month_name = "June"
	elif month == 7:
		month_name = "July"
	elif month == 8:
		month_name = "August"
	elif month == 9:
		month_name = "September"
	elif month == 10:
		month_name = "October"
	elif month == 11:
		month_name = "November"
	elif month == 12:
		month_name = "December"

convert_month()

# Read the file into the script:

data = pds.read_csv(csv_file_path)

products = []
numProducts = 0

# Create a list of products:

for instance in data["product"]:
	if instance not in products: 
		products.append(instance)
		numProducts = numProducts + 1

# Gather a list of sales totals:

rowPrice = data.groupby(data["product"]).sum()
rowPrice = rowPrice.sort_values(by=["sales price"], ascending=False)
totalPrice = rowPrice["sales price"].sum()
totalPrice_usd = "{0:,.2f}".format(totalPrice) #<—— Taken from Groceries Exercise


print(line)

print("Month: " + str(month_name) + " " + str(year))
print(line)

print("Crunching the data...")
print(line)
print("")
print("Total Monthly Sales: $" + str(totalPrice_usd))
print("")
print(line)
print("Top Sellers: ")

# Print the list of top sellers by concatenating the product name and price: 

number = 0 
while number < numProducts:
	price = rowPrice.iloc[number][2]
	print(str(number + 1) + ") " + str(rowPrice.index[number]) + " $" + str("{0:,.2f}".format(price)))
	number = number + 1

print(line)
print("Visualizing the data...")
print(line)

# Initialize the data for the chart:

products_tuple = tuple(products)

number = 0
dataPrice =[] 
while number < numProducts:
	dataPrice.append(rowPrice.iloc[number][2])
	number = number + 1

y_pos = np.arange(len(products_tuple))

# Create the chart:

fig, ax = plt.subplots(1,1, figsize=(120,120))

plt.barh(y_pos, dataPrice , align='center', alpha=0.9)
plt.yticks(y_pos, products_tuple, rotation=30)
plt.ylabel('Products')
plt.xlabel('Sales')
plt.title(str('Top Selling Products: ' + month_name + " " + str(year)), fontsize=30)

ax.plot


# Formatting for the numbers:

for x, k in enumerate(dataPrice):
	plt.text(k , x , "   ${0:,.2f}".format(k))

formatter = ticker.FormatStrFormatter('$%1.2f')
ax.xaxis.set_major_formatter(formatter)

# Remove the frame please it was interfering with the labels and I got annoyed with it, oops:
### Special thanks to my amigos at stack overflow for that one: https://stackoverflow.com/questions/14908576/how-to-remove-frame-from-matplotlib-pyplot-figure-vs-matplotlib-figure-frame

for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Set the label colors to green:

for tick in ax.xaxis.get_major_ticks():
    tick.label.set_color('green')

# Show the final plot:

plt.show()





