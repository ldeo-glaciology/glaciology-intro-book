#!/usr/bin/env python
# coding: utf-8

# # Assignment: Making Maps with Cartopy
# 
# ### 1) Plot data from NARR
# 
# NARR is NCEP's [North American Regional Reanalysis](https://www.esrl.noaa.gov/psd/data/gridded/data.narr.html), a widely used product for studying the weather and climate of the continental US. The data is available from NOAA's [Earth System Research Laboratory](https://www.esrl.noaa.gov/) via [OPeNDAP](https://en.wikipedia.org/wiki/OPeNDAP), meaing that xarray can open the data "remotely" without downloading a file.
# 
# For this problem, you should open this geopential height file:
# 
#     https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/NARR/Dailies/pressure/hgt.201810.nc
#     
# And this precipitation file:
# 
#     https://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/NARR/Dailies/monolevel/apcp.2018.nc
#     
# Your goal is to make a map that looks like the one below. It shows total precipitation on Oct. 15, 2018 in blue, plus contours of the 500 mb geopotential surface.
# 
# _Hint: examine the dataset variables and attirbutes carefully in order to determine the projection of the data._
# 
# ![narr_map](cartopy_figures/narr_map.png)

# ### 2) Antarctic Sea Ice
# 
# Download this file and then use it to plot the concentration of Antarctic Sea Ice on Aug. 7, 2017. Again, you will need to explore the file contents in order to determine the correct projection.
# 

# In[ ]:


import pooch
url = "ftp://sidads.colorado.edu/pub/DATASETS/NOAA/G02202_V3/south/daily/2017/seaice_conc_daily_sh_f17_20170807_v03r01.nc"
fname = pooch.retrieve(url, known_hash=None)


# ![sea_ice_map](cartopy_figures/sea_ice_map.png)

# ### 3) Global USGS Earthquakes
# 
# Reload the file we explored in homework 5 using pandas
# 
#     http://www.ldeo.columbia.edu/~rpa/usgs_earthquakes_2014.csv
#     
# and use the data to recreate this map.

# ![earthquake_map](cartopy_figures/earthquake_map.png)
