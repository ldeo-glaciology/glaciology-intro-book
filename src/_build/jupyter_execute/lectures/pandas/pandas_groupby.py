#!/usr/bin/env python
# coding: utf-8

# # Pandas: Groupby
# 
# `groupby` is an amazingly powerful function in pandas. But it is also complicated to use and understand.
# The point of this lesson is to make you feel confident in using `groupby` and its cousins, `resample` and `rolling`. 
# 
# These notes are loosely based on the [Pandas GroupBy Documentation](http://pandas.pydata.org/pandas-docs/stable/groupby.html).
# 
# The "split/apply/combine" concept was first introduced in a paper by Hadley Wickham: <https://www.jstatsoft.org/article/view/v040i01>.
# 
# 
# Imports:

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (12,7)
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# First we read the Earthquake data from our previous assignment:

# In[2]:


df = pd.read_csv('http://www.ldeo.columbia.edu/~rpa/usgs_earthquakes_2014.csv', parse_dates=['time'], index_col='id')
df['country'] = df.place.str.split(', ').str[-1]
df_small = df[df.mag<4]
df = df[df.mag>4]
df.head()


# ## An Example
# 
# This is an example of a "one-liner" that you can accomplish with groupby.

# In[3]:


df.groupby('country').mag.count().nlargest(20).plot(kind='bar', figsize=(12,6))


# In[4]:


df_small.groupby('country').mag.count().nlargest(20).plot(kind='bar', figsize=(12,6))


# ## What Happened?
# 
# Let's break apart this operation a bit. The workflow with `groubpy` can be divided into three general steps:
# 
# 1. **Split**: Partition the data into different groups based on some criterion.
# 1. **Apply**: Do some caclulation within each group. Different types of "apply" steps might be
#   1. *Aggregation*: Get the mean or max within the group.
#   1. *Transformation*: Normalize all the values within a group
#   1. *Filtration*: Eliminate some groups based on a criterion.
# 1. **Combine**: Put the results back together into a single object.
# 
# ![split-apply-combine](https://miro.medium.com/max/1840/1*JbF6nhrQsn4f-TaSF6IR9g.png)
# 
# ### The `groupby` method
# 
# Both `Series` and `DataFrame` objects have a groupby method. It accepts a variety of arguments, but the simplest way to think about it is that you pass another series, whose unique values are used to split the original object into different groups.
# 
# via <https://medium.com/analytics-vidhya/split-apply-combine-strategy-for-data-mining-4fd6e2a0cc99>

# In[5]:


df.groupby(df.country)


# There is a shortcut for doing this with dataframes: you just pass the column name:

# In[6]:


df.groupby('country')


# ### The `GroubBy` object
# 
# When we call, `groupby` we get back a `GroupBy` object:

# In[7]:


gb = df.groupby('country')
gb


# The length tells us how many groups were found:

# In[8]:


len(gb)


# All of the groups are available as a dictionary via the `.groups` attribute:

# In[9]:


groups = gb.groups
len(groups)


# In[10]:


list(groups.keys())


# ### Iterating and selecting groups
# 
# You can loop through the groups if you want.

# In[11]:


for key, group in gb:
    display(group.head())
    print(f'The key is "{key}"')
    break


# And you can get a specific group by key.

# In[12]:


gb.get_group('Chile').head()


# ## Aggregation
# 
# Now that we know how to create a `GroupBy` object, let's learn how to do aggregation on it.
# 
# One way us to use the `.aggregate` method, which accepts another function as its argument. The result is automatically combined into a new dataframe with the group key as the index.

# In[13]:


gb.aggregate(np.max).head()


# By default, the operation is applied to every column. That's usually not what we want. We can use both `.` or `[]` syntax to select a specific column to operate on. Then we get back a series.

# In[14]:


gb.mag.aggregate(np.max).head()


# In[15]:


gb.mag.aggregate(np.max).nlargest(10)


# There are shortcuts for common aggregation functions:

# In[16]:


gb.mag.max().nlargest(10)


# In[17]:


gb.mag.min().nsmallest(10)


# In[18]:


gb.mag.mean().nlargest(10)


# In[19]:


gb.mag.std().nlargest(10)


# We can also apply multiple functions at once:

# In[20]:


gb.mag.aggregate([np.min, np.max, np.mean]).head()


# In[21]:


gb.mag.aggregate([np.min, np.max, np.mean]).nlargest(10, 'mean').plot(kind='bar')


# ## Transformation
# 
# The key difference between aggregation and transformation is that aggregation returns a *smaller* object than the original, indexed by the group keys, while *transformation* returns an object with the same index (and same size) as the original object. Groupby + transformation is used when applying an operation that requires information about the whole group.
# 
# In this example, we standardize the earthquakes in each country so that the distribution has zero mean and unit variance. We do this by first defining a function called `standardize` and then passing it to the `transform` method.
# 
# I admit that I don't know why you would want to do this. `transform` makes more sense to me in the context of time grouping operation. See below for another example.

# In[22]:


def standardize(x):
    return (x - x.mean())/x.std()

mag_standardized_by_country = gb.mag.transform(standardize)
mag_standardized_by_country.head()


# ## Time Grouping
# 
# We already saw how pandas has a strong built-in understanding of time. This capability is even more powerful in the context of `groupby`. With datasets indexed by a pandas `DateTimeIndex`, we can easily group and resample the data using common time units.
# 
# To get started, let's load the timeseries data we already explored in past lessons.

# In[23]:


import urllib
import pandas as pd

header_url = 'ftp://ftp.ncdc.noaa.gov/pub/data/uscrn/products/daily01/HEADERS.txt'
with urllib.request.urlopen(header_url) as response:
    data = response.read().decode('utf-8')
lines = data.split('\n')
headers = lines[1].split(' ')

ftp_base = 'ftp://ftp.ncdc.noaa.gov/pub/data/uscrn/products/daily01/'
dframes = []
for year in range(2016, 2019):
    data_url = f'{year}/CRND0103-{year}-NY_Millbrook_3_W.txt'               
    df = pd.read_csv(ftp_base + data_url, parse_dates=[1],
                     names=headers, header=None, sep='\s+',
                     na_values=[-9999.0, -99.0])
    dframes.append(df)

df = pd.concat(dframes)
df = df.set_index('LST_DATE')


# In[24]:


df.head()


# This timeseries has daily resolution, and the daily plots are somewhat noisy.

# In[25]:


df.T_DAILY_MEAN.plot()


# A common way to analyze such data in climate science is to create a "climatology," which contains the average values in each month or day of the year. We can do this easily with groupby. Recall that `df.index` is a pandas `DateTimeIndex` object.

# In[26]:


monthly_climatology = df.groupby(df.index.month).mean()
monthly_climatology


# Each row in this new dataframe respresents the average values for the months (1=January, 2=February, etc.)
# 
# We can apply more customized aggregations, as with any groupby operation. Below we keep the mean of the mean, max of the max, and min of the min for the temperature measurements.

# In[27]:


monthly_T_climatology = df.groupby(df.index.month).aggregate({'T_DAILY_MEAN': 'mean',
                                                              'T_DAILY_MAX': 'max',
                                                              'T_DAILY_MIN': 'min'})
monthly_T_climatology.head()


# In[28]:


monthly_T_climatology.plot(marker='o')


# If we want to do it on a finer scale, we can group by day of year.

# In[29]:


daily_T_climatology = df.groupby(df.index.dayofyear).aggregate({'T_DAILY_MEAN': 'mean',
                                                            'T_DAILY_MAX': 'max',
                                                            'T_DAILY_MIN': 'min'})
daily_T_climatology.plot(marker='.')


# ### Calculating anomalies
# 
# A common mode of analysis in climate science is to remove the climatology from a signal to focus only on the "anomaly" values. This can be accomplished with transformation.

# In[30]:


def standardize(x):
    return (x - x.mean())/x.std()

anomaly = df.groupby(df.index.month).transform(standardize)
anomaly.plot(y='T_DAILY_MEAN')


# ### Resampling
# 
# Another common operation is to change the resolution of a dataset by resampling in time. Pandas exposes this through the [resample](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#resampling) function. The resample periods are specified using pandas [offset index](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases) syntax.
# 
# Below we resample the dataset by taking the mean over each month.

# In[31]:


df.resample('M').mean().plot(y='T_DAILY_MEAN', marker='o')


# Just like with `groupby`, we can apply any aggregation function to our `resample` operation.

# In[32]:


df.resample('M').max().plot(y='T_DAILY_MAX', marker='o')


# ### Rolling Operations
# 
# The final category of operations applies to "rolling windows". (See [rolling](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html) documentation.) We specify a function to apply over a moving window along the index. We specify the size of the window and, optionally, the weights. We also use the keyword `centered` to tell pandas whether to center the operation around the midpoint of the window.

# In[33]:


df.rolling(30, center=True).T_DAILY_MEAN.mean().plot()
df.rolling(30, center=True, win_type='triang').T_DAILY_MEAN.mean().plot()

