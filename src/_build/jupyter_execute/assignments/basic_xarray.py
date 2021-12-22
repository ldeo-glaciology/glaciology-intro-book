#!/usr/bin/env python
# coding: utf-8

# # Assignment 7: Xarray Fundamentals with Atmospheric Radiation Data
# 
# In this assignment, we will use Xarray to analyze top-of-atmosphere radiation data from [NASA's CERES project](https://ceres.larc.nasa.gov/).
# 
# <img src="https://upload.wikimedia.org/wikipedia/commons/b/bb/The-NASA-Earth%27s-Energy-Budget-Poster-Radiant-Energy-System-satellite-infrared-radiation-fluxes.jpg" width=65%>
# 
# _Public domain, by NASA, from Wikimedia Commons_
# 
# 
# A pre-downloaded and subsetted a portion of the CERES dataset is available here: http://ldeo.columbia.edu/~rpa/CERES_EBAF-TOA_Edition4.0_200003-201701.condensed.nc. The size of the data file is 702.53 MB. It may take a few minutes to download.
# 
# Please review the CERES [FAQs](https://ceres.larc.nasa.gov/resources/faqs) before getting started.
# 
# Start by importing Numpy, Matplotlib, and Xarray. Set the default figure size to (12, 6).

# In[1]:





# Next, download the NetCDF file using pooch.

# In[2]:


import pooch
fname = pooch.retrieve(
    'http://ldeo.columbia.edu/~rpa/CERES_EBAF-TOA_Edition4.0_200003-201701.condensed.nc',
    known_hash='a876cc7106e7dcb1344fbec5dcd7510e5cd947e62049a8cbc188ad05ffe00345'
)
print(fname)


# ## 1) Opening data and examining metadata

# ### 1.1) Open the dataset and display its contents 
# 

# In[ ]:





# ### 1.2) Print out the `long_name` attribute of each variable
# Print `variable`: `long name` for each variable. Format the output so that the start of the `long name` attributes are aligned. 

# In[ ]:





# ## 2) Basic reductions, arithmetic, and plotting

# ### 2.1) Calculate the time-mean of the entire dataset

# In[ ]:





# ### 2.2) From this, make a 2D plot of the the time-mean Top of Atmosphere Longwave, Shortwave, and Incoming Solar Radiation
# (Use "All-Sky" conditions)
# 
# Note the sign conventions on each variable.

# In[ ]:





# In[ ]:





# In[ ]:





# ### 2.3) Add up the three variables above and verify (visually) that they are equivalent to the TOA net flux
# 
# You have to pay attention to and think carefully about the sign conventions for each variable in order to get this to work.

# In[ ]:





# In[ ]:





# ## 3) Mean and weighted mean
# 
# ### 3.1) Calculate the global (unweighted) mean of TOA net radiation
# 
# Since the Earth is approximately in radiative balance, the net TOA radiation should be zero. But taking the naive mean from this dataset, you should find a number far from zero. Why?

# In[ ]:





# The answer is that each "pixel" or "grid point" of this dataset does not represent an equal area of Earth's surface. So naively taking the mean, i.e. giving equal weight to each point, gives the wrong answer.
# 
# On a lat / lon grid, the relative area of each grid point is proportional to $\cos(\lambda)$. ($\lambda$ is latitude)
# 
# ### 3.2) Create a `weight` array proportional to $\cos(\lambda)$
# 
# Think carefully a about radians vs. degrees
# 

# In[ ]:





# ### 3.3) Redo your global mean TOA net radiation calculation with this weight factor
# 
# Use xarray's [weighted array reductions](http://xarray.pydata.org/en/stable/user-guide/computation.html#weighted-array-reductions) to compute the weighted mean.

# In[ ]:





# This time around, you should have found something much closer to zero. Ask a climate scientist what the net energy imbalance of Earth due to global warming is estimated to be. Do you think our calculation is precise enough to detect this? 
# 
# ### 3.4) Now that you have a `weight` factor, verify that the TOA incoming solar, outgoing longwave, and outgoing shortwave approximately match up with infographic shown in the first cell of this assignment

# In[ ]:





# ## 4) Meridional Heat Transport Calculation
# 
# We can go beyond a weight factor and actually calculate the area of each pixel of the dataset, using the formula
# 
# $$ dA = R^2 \cos(\lambda) d\lambda d \varphi $$
# 
# where $d\lambda$ and $d\varphi$ are the spacing of the points in latitude and longitude (measured in radians). We can approximate Earth's radius as $R = 6,371$ km.
# 
# ### 4.1) calculate the pixel area using this formula and create a 2D (lon, lat) DataArray for it
# 
# (Xarray's `ones_like` function can help you easily create and broadcast DataArrays.) Verify that the sum of all the pixels equals the Earth's true surface area as evaluated using the formula for the area of a sphere (yes, the Earth is not a sphere ... it's just a homework problem).

# In[ ]:





# In[ ]:





# Multiplying the pixel area (m$^2$) from above with the radiative flux (W m$^{-2}$) gives you the total amount of radiation absorbed in each pixel in W.
# 
# ### 4.2) Calculate and plot the total amount of net radiation in each 1-degree latitude band
# 
# Label with correct units

# In[ ]:





# ### 4.3) Plot the cumulatuve sum in latitude of that quantity
# 
# Label with correct units. (Hint: check out xarray's [cumsum](http://xarray.pydata.org/en/stable/generated/xarray.DataArray.cumsum.html) function.)
# 
# This curve tells you how much energy must be transported meridionally by the ocean and atmosphere in order to account for the radiative imbalance at the top of the atmosphere.

# In[ ]:





# You should get a curve that looks something like this: http://www.cgd.ucar.edu/cas/papers/jclim2001a/Fig7.html

# ## 5) Selecting and Merging Data
# 
# For the next problem, use the following approximate locations of four different cities.
# 
# | city | lon | lat |
# | -- | -- | -- |
# | NYC |74 W | 40 N | 
# | Nome, Alaska | 165 W | 64 N | 
# | Columbo, Sri Lanka | 80 E | 7 N |
# | Hobart, Tasmania | 147 E | 43 S |
# 

# ### 5.1) Create a `Dataset` for each point from the global dataset

# In[ ]:





# In[ ]:





# ### 5.2) Merge these four datasets into a new dataset with the new dimension `city`
# 
# Create a new dimension coordinate to hold the city name.
# Display the merged dataset.

# In[ ]:





# ### 5.3) Plot the incoming solar and net radiation at each city
# 
# Make two separate plots.
# Try to have your legend created automatically from the data.

# In[ ]:





# In[ ]:





#  

# In[ ]:




