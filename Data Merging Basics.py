#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[16]:


taxi_owners = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\taxi_owners.p')


# In[6]:


taxi_veh = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\taxi_vehicles.p')


# In[17]:


print(taxi_owners.head())
print()
print(taxi_owners.info())


# In[18]:


print(taxi_veh.head())
print()
print(taxi_veh.info())


# In[19]:


# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())


# In[20]:


# Print the first few rows of the census_altered table to view the change 
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on='ward')

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)


# In[21]:


licenses = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\licenses.p')


# In[22]:


biz_owners = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\business_owners.p')


# In[23]:


#what is the most common business owner title. (i.e., secretary, CEO, or vice president)
# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values('account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())


# 

# ### Total riders in a month
# Your goal is to find the total number of rides provided to passengers passing through the Wilson station (station_name == 'Wilson') when riding Chicago's public transportation system on weekdays (day_type == 'Weekday') in July (month == 7). Luckily, Chicago provides this detailed data, but it is in three different tables. You will work on merging these tables together to answer the question.

# In[24]:


cal = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\cta_calendar.p')
ridership = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\cta_ridership.p')
stations = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\stations.p')


# In[25]:


# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) 							.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())


# A reasonable extension of our review of Chicago business data would include looking at demographics information about the neighborhoods where the businesses are. 

# In[26]:


wards = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\ward.p')
zip_demo = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\zip_demo.p')


# In[28]:


# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip')             			.merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))


# In[ ]:





# Assume that you are looking to start a business in the city of Chicago. Your perfect idea is to start a company that uses goats to mow the lawn for other businesses. However, you have to choose a location in the city to put your goat farm. You need a location with a great deal of space and relatively few businesses and people around to avoid complaints about the smell. 

# In[31]:


land_use = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\land_use.p')
census = pd.read_pickle(r'C:\Sai Vinay\Data Camp\Data Scientist With Python\Data Joining with Pandas\\census.p')


# In[32]:


# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward')                     .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant','account','pop_2010'], 
                                             ascending=[False,True,True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())


# In[ ]:




