# importing libraries
import pandas as pd
pd.set_option('max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *

# 2Initializing dataframe
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'], index=['2017 Sales', '2018 Sales'])

# 3 
quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
ingredients = pd.Series(quantities, index=items, name='Dinner')

# 4 initialzig dataframe
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])

animals.to_csv("cows_and_goats.csv")
