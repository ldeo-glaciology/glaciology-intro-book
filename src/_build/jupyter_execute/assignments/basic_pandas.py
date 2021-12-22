#!/usr/bin/env python
# coding: utf-8

# # Assignment 5: Pandas Fundamentals with Earthquake Data
# 
# In this assignment, we will review pandas fundamentals, such as how to
# 
# - Open csv files
# - Manipulate dataframe indexes
# - Parse date columns
# - Examine basic dataframe statistics
# - Manipulate text columns and extract values
# - Plot dataframe contents using
#   - Bar charts
#   - Histograms
#   - Scatter plots

# First, import Numpy, Pandas and Matplotlib and set the display options.

# In[ ]:





# Data for this assignment in .csv format downloaded from the [USGS Earthquakes Database](https://earthquake.usgs.gov/earthquakes/search/) is available at:
# 
# http://www.ldeo.columbia.edu/~rpa/usgs_earthquakes_2014.csv
# 
# You don't need to download this file. You can open it directly with Pandas.

# ### 1) Use Pandas' read_csv function directly on this URL to open it as a DataFrame
# (Don't use any special options). Display the first few rows and the DataFrame info.

# In[ ]:





# In[ ]:





# You should have seen that the dates were not automatically parsed into datetime types.
# 
# ### 2) Re-read the data in such a way that all date columns are identified as dates and the earthquake ID is used as the index
# 
# Verify that this worked using the `head` and `info` functions.
# 

# In[ ]:





# In[ ]:





# ### 3) Use `describe` to get the basic statistics of all the columns
# 
# Note the highest and lowest magnitude of earthquakes in the databse.

# In[ ]:





# ### 4) Use `nlargest` to get the top 20 earthquakes by magnitude
# 
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.nlargest.html

# In[ ]:





# Examine the structure of the `place` column. The state / country information seems to be in there. How would you get it out?
# 
# ### 5) Extract the state or country using Pandas [text data functions](https://pandas.pydata.org/pandas-docs/stable/text.html)
# 
# Add it as a new column to the dataframe called `country`. Note that some of the "countries" are actually U.S. states.

# In[ ]:





# ### 6) Display each unique value from the new column
# 
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.unique.html

# In[ ]:





# ### 7) Create a filtered dataset that only has earthquakes of magnitude 4 or larger and

# In[ ]:





# ### 8) Using the filtered dataset (magnitude > 4), count the number of earthquakes in each country/state. Make a bar chart of this number for the top 5 locations with the most earthquakes
# 
# Location name on the x axis, Earthquake count on the y axis

# In[ ]:





# ### 9) Make a histogram the distribution of the Earthquake magnitudes
# 
# https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.hist.html
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
# 
# Do one subplot for the filtered and one for the unfiltered dataset.
# Use a Logarithmic scale. What sort of relationship do you see?

# In[ ]:





# ### 11) Visualize the locations of earthquakes by making a scatterplot of their latitude and longitude
# 
# Use a two-column subplot with both the filtered and unfiltered datasets. Color the points by magnitude. Make it pretty
# 
# What difference do you note between the filtered and unfiltered datasets?

# In[ ]:




