# Continuous testing and integration of monthly_sales.py

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

from app.monthly_sales import (
	getfile,
	parse_year,
	parse_month,
	convert_month,
	to_usd
	)

def test_to_usd():
	result = to_usd(5200.2)
	assert result == "$5200.20"