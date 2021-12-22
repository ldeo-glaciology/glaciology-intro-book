#!/usr/bin/env python
# coding: utf-8

# # Assignment 6: Pandas Groupby with Hurricane Data

# Import Numpy, Pandas and Matplotlib and set the display options.

# In[ ]:





# Use the following code to load a CSV file of the [NOAA IBTrACS](https://www.ncdc.noaa.gov/ibtracs/index.php?name=ibtracs-data) hurricane dataset:

# In[ ]:


url = 'https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r00/access/csv/ibtracs.ALL.list.v04r00.csv'
df = pd.read_csv(url, parse_dates=['ISO_TIME'], usecols=range(12),
                 skiprows=[1], na_values=[' ', 'NOT_NAMED'],
                 keep_default_na=False, dtype={'NAME': str})
df.head()


# Basin Key: (NI - North Indian, SI - South Indian, WP - Western Pacific, SP - Southern Pacific, EP - Eastern Pacific, NA - North Atlantic)

# How many rows does this dataset have?

# In[ ]:





# How many North Atlantic hurricanes are in this dataset?

# In[ ]:





# ### 1) Get the unique values of the `BASIN`, `SUBBASIN`, and `NATURE` columns

# In[ ]:





# In[ ]:





# In[ ]:





# ### 2) Rename the `WMO_WIND` and `WMO_PRES` columns to `WIND` and `PRES`

# In[ ]:





# ### 3) Get the 10 largest rows in the dataset by `WIND`

# In[ ]:





# You will notice some names are repeated.
# 
# ### 4) Group the data on `SID` and get the 10 largest hurricanes by `WIND`

# In[ ]:





# ### 5) Make a bar chart of the wind speed of the 20 strongest-wind hurricanes
# 
# Use the name on the x-axis.

# In[ ]:





# ### 6) Plot the count of all datapoints by Basin
# 
# as a bar chart

# In[ ]:





# ### 7) Plot the count of unique hurricanes by Basin
# 
# as a bar chart.

# In[ ]:





# ### 8) Make a `hexbin` of the location of datapoints in Latitude and Longitude

# In[ ]:





# ### 9) Find Hurricane Katrina (from 2005) and plot its track as a scatter plot
# 
# First find the SID of this hurricane.

# In[ ]:





# Next get this hurricane's group and plot its position as a scatter plot. Use wind speed to color the points.

# In[ ]:





# ### 10) Make time the index on your dataframe

# In[ ]:





# ### 11) Plot the count of all datapoints per year as a timeseries
# 
# You should use `resample`

# In[ ]:





# ### 12) Plot all tracks from the North Atlantic in 2005
# 
# You will probably have to iterate through a `GroupBy` object

# In[ ]:





# ### 13) Create a filtered dataframe that contains only data since 1970 from the North Atlantic ("NA") Basin
# 
# Use this for the rest of the assignment

# In[ ]:





# ### 14) Plot the number of datapoints per day from this filtered dataframe
# 
# Make sure you figure is big enough to actually see the plot

# In[ ]:





# ### 15) Calculate the climatology of datapoint counts as a function of `dayofyear`
# 
# Plot the mean and standard deviation on a single figure

# In[ ]:





# ### 16) Use `transform` to calculate the anomaly of daily counts from the climatology
# 
# Resample the anomaly timeseries at annual resolution and plot a line with dots as markers.

# In[ ]:





# Which years stand out as having anomalous hurricane activity?

# 
