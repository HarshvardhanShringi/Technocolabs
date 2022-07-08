# Importing libraries
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import os
if not os.path.exists("../input/ign_scores.csv"):
    os.symlink("../input/data-for-datavis/ign_scores.csv", "../input/ign_scores.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex3 import *

# 1. Loading data
ign_filepath = "../input/ign_scores.csv"
ign_data = pd.read_csv(ign_filepath, index_col="Platform")

# 2. Reviewing data
ign_data

# 3. Comparing platform
sns.barplot(x=ign_data['Racing'], y=ign_data.index)

# 4. Possible combinations
sns.heatmap(ign_data, annot=True)
