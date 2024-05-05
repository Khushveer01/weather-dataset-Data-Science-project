#!/usr/bin/env python
# coding: utf-8

# # Working on Real Project with Python
# (A part of Big Data Analysis)

# # The Weather Dataset
# Here, The Weather Dataset is a time series data set with per-hour information about the weather conditions at a particular 
# location, it records Temperature, Dew point Temperature, Relative Humidity, Wind Speed Visibility, Pressure, and Conditions.
# 
# This data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame

# In[1]:


import pandas as pd 


# In[2]:


data=pd.read_csv(r"F:\data_weather.csv")


# # How to Analyze DataFrames?
.head() it shows the first N rows in the data(by default, N=5)
# In[4]:


data.head()

.shape It shows the total no. of columns of the dataframe.
# In[5]:


data.shape

.index This attribute provides the index of the dataframe.
# In[8]:


data.index

.columns It shows the name of each column.
# In[9]:


data.columns

.dtypes It shows the datatype of each column
# In[10]:


data.dtypes

.unique() In a column, it shows all the unique values , it can be applied on a single column only, not on the whole dataframe. 
# In[13]:


data['Weather'].unique()

.nunique() It shows the total no. of unique value in each column. It can be applied on a single column as well as on whole 
dataframe
# In[14]:


data.nunique()

.count It shows the total no. of non-null in each column. It can be applied on a single column as well as on whole dataframe.
# In[15]:


data.count()

.value_counts In a column, it shows at the unique values with their count, it can be applied on a single column only.
# In[16]:


data['Weather'].value_counts()


# In[ ]:


.info() Provides basic information about the dataframe.


# In[17]:


data.info()


# # Q1) Find all the unique 'Wind Speed' values in the data. 

# In[8]:


import pandas as pd 
data=pd.read_csv(r"F:\data_weather.csv")


# In[9]:


data.head(2)


# In[10]:


data.nunique()


# In[12]:


data['Wind Speed_km/h'].nunique()


# In[13]:


data['Wind Speed_km/h'].unique()


# # Q2) Find the number of times when the 'Weather is exactly clear'.

# In[14]:


data.head(2)


# In[16]:


# value counts()
data.Weather.value_counts()


# In[18]:


# Filtering
data[data.Weather == 'Clear']


# In[19]:


# group by
data.groupby('Weather').get_group('Clear')


# # Q3) Find the number of times when the 'Wind Speed was exactly 4km/h'

# In[20]:


data.head(2)


# In[21]:


data[data['Wind Speed_km/h']==4]


# # Q4) Find out all the Null Values in the data.

# In[22]:


data.isnull().sum()


# In[23]:


data.notnull().sum()


# # Q5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[24]:


data.head(2)


# In[27]:


data.rename(columns={'Weather' :  'Weather Condition'},inplace=True)


# In[28]:


data.head()


# # Q6) What is the mean'Visibility'?

# In[29]:


data.head(2)


# In[30]:


data.Visibility_km.mean()


# # Q7) What is the Standard Deviations of 'Pressure' in this data?

# In[31]:


data.Press_kPa.std()


# # Q8) what is the Variance of 'Relative Humidity' in this data?

# In[32]:


data['Rel Hum_%'].var()


# # Q9) Find all instances when'Snow' was recorded.

# In[33]:


#value counts
data.head(2)


# In[34]:


data['Weather Condition'].value_counts()


# In[36]:


#filtering
data[data['Weather Condition'] == 'Snow']


# In[37]:


# str contains
data[data['Weather Condition'].str.contains('Snow')]


# # Q10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[38]:


data.head(2)


# In[39]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km'] == 25)]


# # Q11) What is the Mean value of each column against each 'Weather Condition'?

# In[40]:


data.head(2)


# In[41]:


data.groupby('Weather Condition').mean()


# # Q12) What is the Minimum and Maximum value of each column against each 'Weather Condition'?

# In[42]:


data.head(2)


# In[43]:


data.groupby('Weather Condition').min()


# In[44]:


data.groupby('Weather Condition').max()


# # Q13) Show all the Records where Weather Condition is Fog.

# In[45]:


data[data['Weather Condition'] == 'Fog']


# # Q14) Find all instances when 'Weather is clear' or 'Visibility is above 40'.

# In[47]:


data[(data['Weather Condition'] == 'Clear')|(data['Visibility_km']>40)]


# # Q15) Find all the instances when'Weather is clear' and 'Relative Humidity is greater than 50' or 'Visibility is above 40' 

# In[48]:


data.head(2)


# In[49]:


data[(data['Weather Condition'] == 'Clear')&(data['Rel Hum_%']>50)|(data['Visibility_km']>40)]


# In[ ]:




