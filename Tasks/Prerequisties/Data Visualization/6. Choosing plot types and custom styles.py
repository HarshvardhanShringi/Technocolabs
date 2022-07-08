# importing libraires
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import os
if not os.path.exists("../input/spotify.csv"):
    os.symlink("../input/data-for-datavis/spotify.csv", "../input/spotify.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex6 import *

# Initializing dataframe
spotify_filepath = "../input/spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)
sns.set_style("ticks")

# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
