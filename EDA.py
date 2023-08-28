import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#import seaborn as sns

d1 = pd.read_csv('C:/Users/MAYURI NAIK/Downloads/Automobile_data.csv')

#display column names
print(d1.columns)

# to display total count of values including all rows and columns, rows * columns
print('\n')
print(d1.size)

# to display No. of rows, column names, datatypes,
print('\n')
d1.info()

# to display top 5 rows with all columns
print('\n')
print(d1.head)

#display mean(Name of the independent variable having minimum average value)
print('\n')
print(d1.mean)

#Name of the independent variable having high standard deviation
print('\n')
print(d1.std)

# to check for wrong entries like symbols -,?,#,*,etc. in each column
print('\n')
for col in d1.columns:
 print('{} : {}'.format(col,d1[col].unique()))

 # to display missing values, python doesnot treat ?, & as missing value, it shows no missing values as there are no NaN values
print('\n')
d1.isnull().sum()

# To replace symbols such as '?' , '&', .... with np.nan which indicates missing values
# After replacing all symbols, the new version of data1 is stored in data1_clean..
print('\n')
#d1_clean = d1.replace({ "?": np.nan, "&": np.nan })

# to display total count of missing values in each column e.g. normalized-losses is having 41 missing values
print('\n')
#d1_clean.isnull().sum()

#to display average value of each column...
print('\n')
#print('Column Name\t\tAvg')
#d1_clean.mean()


#print(d1.columns)
#print(a)

#d1.mean()
#b=d1.size
#print(b)

#d1_clean=d1.replace({"?":np.nan,"&":np.nan})
#print(d1_clean)
#print(d1.isnull().sum().sum())