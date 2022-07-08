# importing libraries
import pandas as pd
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.renaming_and_combining import *

# initializing dataframe
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# 1
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

#2. 
reindexed = reviews.rename_axis('wines', axis='rows')

#3. 
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

#4. 
combined_products = pd.concat([gaming_products, movie_products])

#5. 
powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")

#6. 
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
