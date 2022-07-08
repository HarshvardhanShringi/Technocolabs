from learntools.core import binder
binder.bind(globals())
from learntools.data_cleaning.ex4 import *
import pandas as pd
import numpy as np
import chardet

# 1. Encodindg
sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))
before = sample_entry.decode("big5-tw")
new_entry = before.encode()


# 2. Reading files with encoding problems
police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding='Windows-1252')

# 3. Saving with UTF 8
police_killings.to_csv("my_file.csv")
