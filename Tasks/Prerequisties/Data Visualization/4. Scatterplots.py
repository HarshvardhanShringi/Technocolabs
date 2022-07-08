# importing libraries
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import os
if not os.path.exists("../input/candy.csv"):
    os.symlink("../input/data-for-datavis/candy.csv", "../input/candy.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex4 import *

# Initializing data
candy_filepath = "../input/candy.csv"
candy_data = pd.read_csv(candy_filepath, index_col="id")

# 1. Reviewing data
candy_data.head()

# 2. Role of sugar
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

# 3. Take a closer look
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

# 4. Chocolate
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'], hue=candy_data['chocolate'])

# 5. Investigate Chocolate
sns.lmplot(x="pricepercent", y="winpercent", hue="chocolate", data=candy_data)

# 6. Everybody loves chocolate
sns.swarmplot(x=candy_data['chocolate'], y=candy_data['winpercent'])
