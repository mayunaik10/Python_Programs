#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[6]:


penguin=pd.read_csv('C:/Users/Jasmit/Downloads/penguin.csv')


# In[7]:


# Number of independent variables
X = penguin.iloc[:,1:4]
print(X)


# In[8]:


# Name of the independent variable having minimum average value
penguin['culmen_length_mm'].mean()


# In[9]:


# Name of the independent variable having minimum average value
penguin['culmen_depth_mm'].mean()


# In[10]:


# Name of the independent variable having high standard deviation
penguin.describe()


# In[11]:


#from above 'culmen_length_mm' has high sd


# In[12]:


# What is the dependent variable in the selected dataset
Y = penguin.iloc[:,4]
print(Y)


# In[13]:


# Display top 5 rows from the selected dataset
penguin.head()


# In[14]:


# Find the total count of missing values in each column(independent variables). 
penguin.isnull().sum()


# In[15]:


#here total 4 missing values are there in two independent variables.


# In[16]:


# Visualize all missing values, and identify the independent variable having maximum number of missing values?
sns.heatmap(penguin.isnull(),cbar=False,cmap='viridis')


# In[17]:


#  Choose one numeric independent variable having missing values and replace the missing values with the average value of the column. 
num_col = ['culmen_length_mm']
for col in num_col:
    penguin[col]=pd.to_numeric(penguin[col])
    penguin[col].fillna(penguin[col].mean(), inplace=True)
penguin.head()


# In[18]:


# Choose one independent variable and show frequency distribution using histogram
sns.histplot(penguin.culmen_depth_mm,bins=10)


# In[19]:


# Name of the independent variable having outliers? Use Box-plot to visualize.
sns.boxplot( "culmen_length_mm",data = penguin)


# In[20]:


# Display Correlation Matrix and find two pairs of independent variables, one having strong positive correlation and the other pair having strong negative correlation
f, ax = plt.subplots(figsize=(10, 8))
corr = penguin.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)


# In[21]:


# Use scatter plots to visualize the correlation between independent and dependent variables (use same two pairs identified in previous question)
x = "culmen_length_mm"
y = "flipper_length_mm"
sns.scatterplot(penguin[x], penguin[y])


# In[ ]:




