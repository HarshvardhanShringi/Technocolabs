# importing libraries
import pandas as pd
pd.set_option("display.max_rows", 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *

# Initializing data
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#1. 
median_points = reviews.points.median()

#2.
countries = reviews.country.unique()

#3. 
reviews_per_country = reviews.country.value_counts()

#4.
centered_price = reviews.price - reviews.price.mean()

#5. 
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

#6. 
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

#7. 
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
