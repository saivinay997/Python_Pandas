#!/usr/bin/env python
# coding: utf-8

# ### Name:     Sai Vinay M R
# ### Date:       10/11/2022

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np


# In[2]:


homelessness = pd.read_csv(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Manipulation with pandas\homelessness.csv')


# In[ ]:





# In[3]:


# Print the head of the homelessness data
print(homelessness.head())


# In[4]:


# Print the values of homelessness
print(homelessness.values)


# In[5]:


# Print the column index of homelessness
print(homelessness.columns)


# In[6]:


# Print the row index of homelessness
print(homelessness.index)


# In[7]:


# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())


# In[8]:


# Select the individuals column
individuals = homelessness['individuals']

# Print the head of the result
print(individuals.head())


# In[9]:


# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals']>10000]

# See the result
print(ind_gt_10k)


# In[10]:


# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness['region']=='South Atlantic')|(homelessness['region']=='Mid-Atlantic')]


# See the result
print(south_mid_atlantic)


# In[12]:


# Add total col as sum of individuals and family_members
homelessness['total']=homelessness['individuals']+homelessness['family_members']

# Add p_individuals col as proportion of total that are individuals
homelessness['p_individuals']=homelessness['individuals']/homelessness['total']

# See the result
print(homelessness.head())


# In[13]:


#In this exercise, you'll answer the question, 
#"Which state has the highest number of homeless individuals per 10,000 people in the state?"

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop'] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k']>20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state','indiv_per_10k']]

# See the result
print(result)


# In[ ]:




