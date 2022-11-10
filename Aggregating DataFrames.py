#!/usr/bin/env python
# coding: utf-8

# ### Name:     Sai Vinay M R
# ### Date:       10/11/2022
# 

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np


# In[3]:


sales=pd.read_csv(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Manipulation with pandas\sales_subset.csv')


# In[5]:


# Print the head of the sales DataFrame
print(sales.head())


# In[6]:


# Print the info about the sales DataFrame
print(sales.info())


# In[7]:


# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())


# In[8]:


# Print the median of weekly_sales
print(sales['weekly_sales'].median())


# In[9]:


# Print the maximum of the date column
print(sales['date'].max())


# In[10]:


# Print the minimum of the date column
print(sales['date'].min())


# In[11]:


'''In the custom function for this exercise, "IQR" is short for inter-quartile range, 
which is the 75th percentile minus the 25th percentile. It's an alternative to standard deviation 
that is helpful if your data contains outliers.'''

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))


# In[13]:


sales_1_1 = sales[(sales['store']==1)&(sales['department']==1)]
print(sales_1_1)


# In[14]:


# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date')


# In[15]:


# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])


# ### Dropping Duplicates
# 

# In[16]:


# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store','type'])
print(store_types.head())


# In[17]:


# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())


# In[19]:


# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']==True].drop_duplicates('date')

# Print date col of holiday_dates
print(holiday_dates['date'])


# ### Counting categorical variables

# In[20]:


# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)


# In[21]:


# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)


# In[22]:


# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)


# In[23]:


# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)


# ### Grouped summary statistics

# In[24]:


#What percent of sales occurred at each store type?


# In[25]:


# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()
print(sales_all)


# In[30]:


# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales['type']=='B']['weekly_sales'].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales['type']=='C']['weekly_sales'].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)


# In[31]:


# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
print(sales_by_type)

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)


# ### Multiple grouped summaries

# In[32]:


# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min,np.max,np.mean,np.median])

# Print sales_stats
print(sales_stats)


# In[33]:


# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')['unemployment','fuel_price_usd_per_l'].agg([np.min,np.max,np.mean,np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


# ### Pivot Table

# In[34]:


#Pivoting on one variable

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type')

# Print mean_sales_by_type
print(mean_sales_by_type)


# In[35]:


# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values='weekly_sales',index='department',columns='type', fill_value=0))


# In[ ]:




