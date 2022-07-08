# Importing libraries
import pandas as pd
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.grouping_and_sorting import *

# Intializing dataframe
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#1. 
reviews_written = reviews.groupby('taster_twitter_handle').size()

#2. 
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

#3. 
price_extremes = reviews.groupby('variety').price.agg([min, max])

#4.
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

#5. 
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

#6.
reviewer_mean_ratings.describe()

#7. 
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
