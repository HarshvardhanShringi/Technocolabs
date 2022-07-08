# importing libraries
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex7 import *

# Loading data
my_filepath = "../input/fivethirtyeight-comic-characters-dataset/dc-wikia-data.csv"
my_data = pd.read_csv(my_filepath)

# making barplot
sns.barplot(data=my_data)
