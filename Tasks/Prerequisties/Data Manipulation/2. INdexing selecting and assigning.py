# Importing libraries
import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *

# 1. 
desc = reviews.description

# 2.
first_description = reviews.description.iloc[0]

# 3. 
first_row = reviews.iloc[0]

# 4. 
first_descriptions = reviews.description.iloc[:10]

# 5. 
indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

# 6. 
cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

# 7. 
cols = ['country', 'variety']
df = reviews.loc[:99, cols]

# 8. 
italian_wines = reviews[reviews.country == 'Italy']

# 9. 
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand']) & (reviews.points >= 95)]
