# importing libraries
import pandas as pd
import numpy as np
from scipy import stats
from mlxtend.preprocessing import minmax_scaling
import seaborn as sns
import matplotlib.pyplot as plt


# Initalizing dataframes
kickstarters_2017 = pd.read_csv("../input/kickstarter-projects/ks-projects-201801.csv")

original_data = pd.DataFrame(kickstarters_2017.usd_goal_real)

# Normalization
scaled_data = minmax_scaling(original_data, columns=['usd_goal_real'])

# Scaling vs Orignal data
fig, ax=plt.subplots(1,2,figsize=(15,3))
sns.distplot(kickstarters_2017.usd_goal_real, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(scaled_data, ax=ax[1])
ax[1].set_title("Scaled data")


# Scaling goal column
original_goal_data = pd.DataFrame(kickstarters_2017.goal)

scaled_goal_data = minmax_scaling(original_goal_data, columns=['goal'])

index_of_positive_pledges = kickstarters_2017.usd_pledged_real > 0

# Normalizing usd_pledged_real column
positive_pledges = kickstarters_2017.usd_pledged_real.loc[index_of_positive_pledges]
normalized_pledges = pd.Series(stats.boxcox(positive_pledges)[0], 
                               name='usd_pledged_real', index=positive_pledges.index)

# Comparing and plotting
fig, ax=plt.subplots(1,2,figsize=(15,3))
sns.distplot(positive_pledges, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(normalized_pledges, ax=ax[1])
ax[1].set_title("Normalized data")


# Normalizing the pledged column
index_positive_pledges = kickstarters_2017.pledged > 0
positive_pledges_only = kickstarters_2017.pledged.loc[index_positive_pledges]
normalized_values = pd.Series(stats.boxcox(positive_pledges_only)[0], 
                              name='pledged', index=positive_pledges_only.index)

# Comparing and plotting
fig, ax = plt.subplots(1,2,figsize=(15,3))
sns.distplot(positive_pledges_only, ax=ax[0])
ax[0].set_title("Original Data")
sns.distplot(normalized_values, ax=ax[1])
ax[1].set_title("Normalized data")

