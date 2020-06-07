#!/usr/bin/env python
# coding: utf-8

# # **Analyzing COVID-19 cases in NYC**

# In March 2020, WHO declared COVID-19 outbreak a global pandemic. Since then, this virus has spread rapidly and affected more than 4 million people; while it has taken the lives of nearly 290,000 people worldwide (as of May 9, 2020). New York City is among one the most severely affected cities in the world, which accounts for nearly 50% of confirmed cases in the U.S. 
# 
# In this notebook, we will examine the relationship between number of COVID-19 confirmed cases with median income per zip code in New York City (NYC).

# ## Data Sources

# -  tests-by-zcta.txt: file about the number of tests given and the number of positive cases in each zip code in NYC
# -  Income 2018.csv: file about the median income in each zip code in NYC
# -  population_zip_code.xlsx: file about the population in each zip code in NYC

# ## 1 Installing packages

# In[1]:


get_ipython().system(u'pip install geopandas')
get_ipython().system(u'pip install descartes')
get_ipython().system(u'pip install matplotlib')
get_ipython().system(u'pip install numpy')
get_ipython().system(u'pip install pandas')


# ### Import libraries

# In[2]:


import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

get_ipython().magic(u'matplotlib inline')


# ## 2 Loading and Wrangling Data

# We start with loading data from each file.

# ### Loading and Wrangling 'Test' Data

# In[3]:


df_test = pd.read_csv ('tests-by-zcta.txt', delimiter =',')
df_test.head()


# In[4]:


print('Data shape: ', df_test.shape)


# The 'test' table has 4 columns and 178 rows in total. The first row appears to be a total cases of each column. 

# In[5]:


df_test.info()


# In[6]:


df_test.describe()


# There is no missing data after the first row in this table. The statisitcs shows that there might be outliers in variable 'Positive' and 'Total'.

# In[7]:


df_test = df_test.drop([0])
df_test = df_test.rename(columns={'modzcta': 'Zip_Code', 'modzcta_cum_perc_pos': 'Positive_Rate'})
print(df_test.head(10))


# For data wrangling, we remove the first row of this dataframe to eliminate the missing record. Then, we will give meaningful name for the following variables 'MODZCTA' as 'Zip_Code', 'modzcta_cum_perc_pos' as 'Positive_Rate'.

# ### Loading 'Income' Data

# In[8]:


df_income = pd.read_csv ('Income 2018.csv')
df_income.head()


# In[9]:


print('Data shape: ', df_income.shape)


# The 'Income 2018' table has 3 columns and 1646 rows in total. 

# In[10]:


df_income.info()
df_income.describe()


# There is no missing data in this table. There might be outliers in Median_Income variables. A quick glance of this data shows us an income inequality between neighborhood in NYC.

# ### Loading and Wrangling Population Data

# In[11]:


df = pd.read_excel ('population_zip_code.xlsx')
df.tail(10)


# In[12]:


print('Data shape: ', df.shape)


# The 'population_zip_code' table has 3 columns and 1605 rows in total. Some rows contains mulitple zip codes in a record.

# In[13]:


df.info()


# In[14]:


df.describe()


# #### Data Wrangling

# In[15]:


# Create dataframe with "Rank" has no tie
df_tie = df[~df.Rank.str.contains("TIE", na=False)]
df_tie.sample(5)


# In[16]:


df_tie.info()


# In[17]:


#Replace "and" in Zip Code in Population table
df["Zip Code"]= df["Zip Code"].replace("and", ",", regex=True)


# In[18]:


#Split columns with "," into multiple rows
df_split = df.set_index(['Rank']).stack().str.split('/|, ,|,', expand=True).stack().unstack(-2).reset_index(-1, drop=True).reset_index()
df_split.tail(10)


# In[19]:


df_split.info()


# In[20]:


#Merge split dataframe with population table to get population variables
df_split_population = pd.merge(df, df_split, on="Rank", how = "left")
df_split_population = df_split_population.dropna()
df_split_population.tail(10)


# In[21]:


df_split_population.info()


# In[22]:


df_split_population = df_split_population.drop(['Zip Code_x'], axis=1)


# In[23]:


df_split_population.sample(10)


# In[24]:


count = df["Population"].isna().sum()
count


# In[25]:


df_split_population = df_split_population.rename(columns={'Zip Code_y': 'Zip Code'})


# In[26]:


#Combine Tie dataframe and new split dataframe
df_population = pd.concat([df_tie,df_split_population], sort= False)
df_population.sample(5)


# In[27]:


df_population.info()


# In[28]:


df_population.describe()


# In[29]:


df_population = df_population.rename(columns={'Zip Code': 'Zip_Code'})
df_population.head()


# In[30]:


df_population = df_population.drop(['Rank'], axis=1)


# In[31]:


df_population.tail(20)


# In[32]:


df_population.info()


# In[33]:


to_excel = df_population.to_excel('population.xlsx')


# In[34]:


#Convert Zip_Code type from object to integer
convert_dict = {'Zip_Code': float, 
               } 
  
df_population = df_population.astype(convert_dict) 
print(df_population.dtypes) 


# In[35]:


df_population.info()


# ### Merging All Data

# In[36]:


#Merge Test and Income tables
df_merge = pd.merge(df_test, df_income, on='Zip_Code')
df_merge.head()


# In[37]:


#Merge Population table with Merge table
df_merge_population = pd.merge(df_merge, df_population, on='Zip_Code')
df_merge_population.head()


# In[38]:


df_merge_population.info()
df_merge_population.count()


# ## 3 Exploratory Data Analysis

# First of all, let's explore the distribution of the data and its relationship among each other.

# In[39]:


sns.pairplot(df_merge_population[['Positive','Total','Positive_Rate','Median_Income','Population']])
plt.show()


# Variable 'Positive' and 'Total' are skewed right. Thus, we need to normalize these variables by figuring the number of positive tests and total number of test per 1000 people.

# In[40]:


#Calculate number of positive cases per 1000 people per Zip Code
df_merge_population ['Positive_per_1000']= 1000*df_merge_population ['Positive']/df_merge_population['Population']

#Calculate number of tests cases per 1000 people per Zip Code
df_merge_population ['Test_per_1000']= 1000*df_merge_population ['Total']/df_merge_population['Population']

df_merge_population.head()


# In[41]:


df_merge_population.head()


# In[42]:


df_merge_population.shape


# In[43]:


df_merge_population.describe()


# Our final dataframe has in total of 177 rows and 9 columns.
# - Zip_Code is a zip code in NYC
# - Positive is total confirmed cases
# - Total is a total COVID test done
# - Positive rate is the rate of positive cases divided by the total test given
# - Median_Income is a median income per zip code
# - The population is population per zip code
# - Positive_per_1000 is a number of confirmed cases per 1000 people in each zip code
# - Test_per_1000 is a number of tests given per 1000 people in each zip code. 

# In[44]:


df_merge_population.info()


# In[45]:


sns.pairplot(df_merge_population[['Positive_Rate','Median_Income','Positive_per_1000', 'Test_per_1000']])
plt.show()


# In[46]:


chart_positive_1000 = sns.jointplot(x='Median_Income', y='Positive_per_1000', data=df_merge_population, kind="reg")
chart_positive_1000.fig.suptitle('Correlation between Median Income and Confirmed Cases per 1k') 


# In[47]:


chart_test_1000 = sns.jointplot(x='Median_Income', y='Test_per_1000', data=df_merge_population, kind="reg")
chart_test_1000.fig.suptitle('Correlation between Median Income and Total Test per 1k') 


# In[48]:


chart_Positive_Rate = sns.jointplot(x='Median_Income', y='Positive_Rate', data=df_merge, kind="reg")
chart_Positive_Rate.fig.suptitle('Correlation between Median Income and Positive Rate') 


# In[49]:


df_merge_population_corr = df_merge_population.drop(['Zip_Code', 'Positive', 'Total'], axis=1)
corrMatrix = df_merge_population_corr.corr()
sns.heatmap(corrMatrix, annot=True, linewidth = 0.5, cmap='coolwarm',square=True, vmin = -1, vmax = 1)
plt.show()
# plt.figure(figsize=(5,4))
plt.tight_layout()


# When examining the relationship between median_income variable with number of positive test and total test, we can see the median income variable has a weak association with the number of tests are given and confirmed cases per 1000. However, median income does have a strong negative correlation with a positive rate. That means those who are tested and confirmed infected by the virus are more likely to live in lower-income areas.  This metric would raise concerns here as it is costly to access healthcare in the U.S. and low-income residents could possibly wait until the symptoms were severe before getting tested.

# In[50]:


chart_top10_test = df_merge_population.sort_values(by=['Test_per_1000'])[-5:].plot(x="Zip_Code", y="Test_per_1000", kind="barh")
plt.title ("Top 5 areas with the highest test per 1000")
plt.ylabel ("# of Test per 1000")
plt.xlabel ("Zip Code")
plt.show()


# In[51]:


chart_top10_positive = df_merge_population.sort_values(by=['Positive_per_1000'])[-5:].plot(x="Zip_Code", y="Positive_per_1000", kind="barh")
plt.title ("Top 5 areas with the highest positive per 1000")
plt.ylabel ("# of Positive per 1000")
plt.xlabel ("Zip Code")
plt.show()


# In[52]:


to_excel = df_merge_population.to_excel('clean.xlsx')


# ### Map

# The best way to see data is to use visualization so I map out the areas that are have confirmed cases with the median income.

# In[53]:


fp = "acs2018_5yr_B19001_86000US10543.shp"
map_df = gpd.read_file(fp)
# check the GeoDataframe
map_df.head()


# In[54]:


map_df.plot()


# In[55]:


plt.rcParams['figure.figsize'] = [30, 90] #height, width
map_df.plot()


# In[56]:


# join the geodataframe with the csv dataframe
merged = map_df.merge(df_merge_population, how='left', on="geoid")

merged.head()


# In[57]:


to_excel = merged.to_excel('final.xlsx')


# In[62]:


# set the value column that will be visualised
variable = 'Positive'
# set the range for the choropleth values
vmin, vmax = 0, 3000
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(30, 10))
# remove the axis
ax.axis('off')
# add a title and annotation
ax.set_title('Covid19 Confirmed Cases in NYC, updated Jun 1/2020', fontdict={'fontsize': '25', 'fontweight' : '3'})
ax.annotate('Source: NYC Department of Health and Mental Hygiene', xy=(0.6, .05), xycoords='figure fraction', fontsize=12, color='#555555')
# Create colorbar legend
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm.set_array([]) # or alternatively sm._A = []. Not sure why this step is necessary, but many recommends it
# add the colorbar to the figure
fig.colorbar(sm)
# create map
merged.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8')


# In[59]:


# set the value column that will be visualised
variable = 'Positive_per_1000'
# set the range for the choropleth values
vmin, vmax = 0, 40
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(30, 10))
# remove the axis
ax.axis('off')
# add a title and annotation
ax.set_title('Covid19 Confirmed Cases per 1000 in NYC, updated Jun 01/2020', fontdict={'fontsize': '25', 'fontweight' : '3'})
ax.annotate('Source: NYC Department of Health and Mental Hygiene', xy=(0.6, .05), xycoords='figure fraction', fontsize=12, color='#555555')
# Create colorbar legend
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm.set_array([]) # or alternatively sm._A = []. Not sure why this step is necessary, but many recommends it
# add the colorbar to the figure
fig.colorbar(sm)
# create map
merged.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8')


# In[60]:


# set the value column that will be visualised
variable = 'Positive_Rate'
# set the range for the choropleth values
vmin, vmax = 0, 70
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(30, 10))
# remove the axis
ax.axis('off')
# add a title and annotation
ax.set_title('Covid19 Positive Rate in NYC, updated Jun 01/2020', fontdict={'fontsize': '25', 'fontweight' : '3'})
ax.annotate('Source: NYC Department of Health and Mental Hygiene', xy=(0.6, .05), xycoords='figure fraction', fontsize=12, color='#555555')
# Create colorbar legend
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm.set_array([]) # or alternatively sm._A = []. Not sure why this step is necessary, but many recommends it
# add the colorbar to the figure
fig.colorbar(sm)
# create map
merged.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8')


# In[61]:


# set the value column that will be visualised
variable = 'Median_Income'
# set the range for the choropleth values
vmin, vmax = 0, 250000
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(30, 10))
# remove the axis
ax.axis('off')
# add a title and annotation
ax.set_title('Median Income in NYC', fontdict={'fontsize': '25', 'fontweight' : '3'})
ax.annotate('Source: U.S. Census Bureau (2014-2018)', xy=(0.6, .05), xycoords='figure fraction', fontsize=12, color='#555555')
# Create colorbar legend
sm = plt.cm.ScalarMappable(cmap='Greens', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm.set_array([]) # or alternatively sm._A = []. Not sure why this step is necessary, but many recommends it
# add the colorbar to the figure
fig.colorbar(sm)
# create map
merged.plot(column=variable, cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8')


# ## Conclusion

# The data about confirmed cases based on median income in each zip code alone does not give us enough evidence proving that COVID-19 cases mostly affect low-income areas. Knowing how rapidly the virus spreads in the community, we would need more data such as employment status, change of commuting or ridership before and after the pandemic, household size to justify whether low-income neighbourhoods are more vulnerable to this virus. 
