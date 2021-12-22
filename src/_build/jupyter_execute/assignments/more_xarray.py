#!/usr/bin/env python
# coding: utf-8

# # Assignment: More Xarray with El Niño-Southern Oscillation (ENSO) Data
# 
# Here will will calculate the NINO 3.4 index of El Nino variabillity and use it to analyze datasets.
# 
# First read [this page from NOAA](https://www.ncdc.noaa.gov/teleconnections/enso/indicators/sst). It tells you the following:
# 
# - The Niño 3.4 region is defined as the region between +/- 5 deg. lat, 170 W - 120 W lon.
# - Warm or cold phases of the Oceanic Niño Index are defined by a five consecutive 3-month running mean of sea surface temperature (SST) anomalies in the Niño 3.4 region that is above the threshold of +0.5°C (warm), or below the threshold of -0.5°C (cold). This is known as the Oceanic Niño Index (ONI).
# 
# (Note that "anomaly" means that the seasonal cycle, also called the "climatology" has been removed.)

# Start by importing Numpy, Matplotlib, and Xarray. Set the default figure size to (12, 6).

# In[ ]:





# ### 1. Reproduce the SST curve from the figure below
# 
# Use the `sst.mnmean.nc` file that we worked with in class, located at <http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/noaa.ersst.v5/sst.mnmean.nc>.
# 
# You don't have to match the stylistic details, or use different colors above and below zero, just the "3mth running mean" curve.

# ![enso](https://www.ncdc.noaa.gov/monitoring-content/teleconnections/eln-f-pg.gif)

# Load the data as an Xarray dataset. Drop the `time_bnds` variable as we did in class and trim the data to 1950 onward for this assignment.

# In[ ]:





# Now calculate the climatology and the SST anomaly.

# In[ ]:





# Now reproduce the plot. Keep the rolling 3-month average of the SST anomaly as a DataArray for the next question.

# In[ ]:





# ### 2. Calculate boolean timeseries representing the positive / negative ENSO phases
# 
# Refer to the definitions of warm/cold phases above.

# In[ ]:





# Plot them somehow.

# In[ ]:





# ### 3. Plot composites of SST anomaly for the positive and negative ENSO regimes

# These should be pcolormesh maps. First positive ONI.

# In[ ]:





# And negative ONI.

# In[ ]:





# ### 4. Calculate the composite of preciptiation for positive and negative ENSO phases.
# 
# First load the precip dataset. Code to fix the broken time coordinate is included.

# In[1]:


import pandas as pd
import xarray as xr
url = 'http://iridl.ldeo.columbia.edu/SOURCES/.NASA/.GPCP/.V2p1/.multi-satellite/.prcp/dods'
dsp = xr.open_dataset(url, decode_times=False)
true_time = (pd.date_range(start='1960-01-01', periods=len(dsp['T']), freq='MS'))
dsp['T'] = true_time
dsp = dsp.rename({'T': 'time'})
dsp.load()


# Now plot the *difference* between the time-mean of `prcp` during positive and negative ENSO phases.

# In[ ]:




