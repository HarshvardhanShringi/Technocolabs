# Importing libraires
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Initializing dataframe
cancer_b_filepath = "../input/cancer_b.csv"
cancer_m_filepath = "../input/cancer_m.csv"
# Fill in the line below to read the (benign) file into a variable cancer_b_data
cancer_b_data = pd.read_csv(cancer_b_filepath, index_col="Id")
# Fill in the line below to read the (malignant) file into a variable cancer_m_data
cancer_m_data = pd.read_csv(cancer_m_filepath, index_col="Id")

#1. Reviewing ata
cancer_b_data.head()
cancer_m_data.head()

#2. Investigsting differences
sns.distplot(a=cancer_b_data['Area (mean)'], label="Benign", kde=False)
sns.distplot(a=cancer_m_data['Area (mean)'], label="Malignant", kde=False)

#3. A very usefull column
sns.kdeplot(data=cancer_b_data['Radius (worst)'], shade=True, label="Benign") 
sns.kdeplot(data=cancer_m_data['Radius (worst)'], shade=True, label="Malignant")
