#!/usr/bin/env python
# coding: utf-8

# ### Name:     Sai Vinay M R
# ### Date:       10/11/2022

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np


# In[2]:


temperatures = pd.read_csv(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Manipulation with pandas\temperatures.csv') 


# In[3]:


# Look at temperatures
print(temperatures.head())


# In[5]:


# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind.head())


# In[6]:


# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())


# In[7]:


# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))


# In[8]:


# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]


# In[9]:


# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])


# In[10]:


# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])


# In[11]:


# Setting multi-level indexes

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country','city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil','Rio De Janeiro'),('Pakistan','Lahore')]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])


# In[12]:


# Sorting by index values

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())


# In[13]:


# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level='city'))


# In[14]:


# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=['country','city'],ascending=[True,False]))


# ### Slicing and subsetting with .loc and .iloc

# In[15]:


# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()


# In[16]:


# Subset rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])


# In[17]:


# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc['Lahore':'Moscow'])


# In[18]:


# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan','Lahore'):('Russia','Moscow')])


# In[19]:


# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad')])


# In[20]:


# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,'date':'avg_temp_c'])


# In[21]:


# Subset in both directions at once
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad'),'date':'avg_temp_c'])


# In[22]:


# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2011-12-31')]


# In[23]:


# Set date as the index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()


# In[24]:


# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010':'2011'])


# In[25]:


# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08':'2011-02'])


# In[26]:


# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22:23,1:2])


# In[27]:


# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])


# In[28]:


# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])


# In[29]:


# Use slicing in both directions at once
print(temperatures.iloc[:5,2:4])


# ### Working with pivot tables

# In[37]:


import datetime as dt


# In[40]:


# df['Date'] = pd.to_datetime(df['Date'])
# df['Month'] = df['Date'].dt.month

# Add a year column to temperatures
temperatures['date'] = pd.to_datetime(temperatures['date'])
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c',index=['country','city'],columns='year')

# See the result
print(temp_by_country_city_vs_year)


# In[41]:


# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt':'India']


# In[42]:


# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')]


# In[43]:


# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),'2005':'2010']


# In[44]:


# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()
print(mean_temp_by_year.head())


# In[45]:


# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year==mean_temp_by_year.max()])


# In[47]:


# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city==mean_temp_by_city.min()])


# In[ ]:




