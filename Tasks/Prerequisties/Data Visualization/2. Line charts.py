# Importing libraries
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import os
if not os.path.exists("../input/museum_visitors.csv"):
    os.symlink("../input/data-for-datavis/museum_visitors.csv", "../input/museum_visitors.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex2 import *

#2. initializing dataframe
museum_filepath = "../input/museum_visitors.csv"
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)

# 3. Reviewing data
museum_data.tail()
ca_museum_jul18 = 2620
avila_oct18 = 19280 - 4622

# 4. convince the museum board
sns.lineplot(data=museum_data)

# 5. assess seasonality
sns.lineplot(data=museum_data['Avila Adobe'])
