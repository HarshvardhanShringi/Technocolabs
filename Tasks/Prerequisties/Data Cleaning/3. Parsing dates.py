# importing libraries

from earntools.core import binder
binder.bind(globals())
from learntools.data_cleaning.ex3 import *
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# initializing dataframe
earthquakes = pd.read_csv("../input/earthquake-database/database.csv")

# 1. Checking datetype of column
earthquakes['Date'].head()

# 2. Convert our date columns to datetime
earthquakes[3378:3383]
date_lengths = earthquakes.Date.str.len()
date_lengths.value_counts()
earthquakes.loc[3378, "Date"] = "02/23/1975"
earthquakes.loc[7512, "Date"] = "04/28/1985"
earthquakes.loc[20650, "Date"] = "03/13/2011"
earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], format="%m/%d/%Y")

# 3. Selecting the day of month
day_of_month_earthquakes = earthquakes['date_parsed'].dt.day

# 4. Plot the day of month to check the day parsing
day_of_month_earthquakes = day_of_month_earthquakes.dropna()
