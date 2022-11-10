#!/usr/bin/env python
# coding: utf-8

# ### Name:     Sai Vinay M R
# ### Date:       10/11/2022

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


#pd.read_pickle(path, compression='infer')

avocados = pd.read_pickle('C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Manipulation with pandas\\avoplotto.pkl', compression='infer')


# In[17]:


# Look at the first few rows of data
print(avocados.head())

print(avocados.info())


# In[6]:


# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

print(nb_sold_by_size.head())

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar')

# Show the plot
plt.show()


# In[9]:


# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind='line', rot=45)

# Show the plot
plt.show()


# In[10]:


# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(y='avg_price',x='nb_sold',kind='scatter',title='Number of avocados sold vs. average price')

# Show the plot
plt.show()


# In[11]:


# Histogram of conventional avg_price 
avocados[avocados['type']=='conventional']['avg_price'].hist()

# Histogram of organic avg_price
avocados[avocados['type']=='organic']['avg_price'].hist()

# Add a legend
plt.legend(['conventional','organic'])

# Show the plot
plt.show()


# In[12]:


# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()


# In[20]:


# avocados_2016 = avocados.loc['2016-01-01':'2016-12-31' ]
avocados_2016 = avocados[(avocados['date']>='2016-01-01') & (avocados['date']<='2016-12-31')]

print(avocados_2016)


# In[21]:


# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()


# In[22]:


# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())


# In[24]:


#List the columns with missing values

cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

#Create histograms showing the distributions cols_with_missing

avocados_2016[cols_with_missing].hist()

#Show the plot
plt.show()


# In[23]:


# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()


# In[25]:


# Create a list of dictionaries with new data
avocados_list = [
    {'date': "2019-11-03", 'small_sold': 10376832, 'large_sold': 7835071},
    {'date': "2019-11-10", 'small_sold': 10717154, 'large_sold': 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)


# In[26]:


# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17","2019-12-01"],
  "small_sold": [10859987,9291631],
  "large_sold": [7674135,6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)


# In[ ]:




