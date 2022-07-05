# 1.  Look at the data
import pandas as pd
import numpy as np

df = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")
print(df.head)
print(df.shape)
print(df.dtypes)
print(df.columns)


# 2.  How many missing data points do we have

na_cnt=[]
colno=len(df.columns)
for i in range(9):
    result=df[df.columns[i]].isnull().to_numpy().nonzero()
    if len(result[0])!=0:
        na_cnt.append(len(result[0]))
total_nan=sum(na_cnt)
total_cell=np.product(df.shape)
print((total_nan/total_cell)*100)

# 3 Figure out why data is missing

# 4,5. Drop Missing values

df.dropna (subset=[df.columns[-1]],axis=0, inplace = True)
print(df.shape)

# 6. Filling automatically

df[df.columns[-1]].replace(np.nan,0,inplace=True)
