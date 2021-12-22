#!/usr/bin/env python
# coding: utf-8

# # Xarray Interpolation, Groupby, Resample, Rolling, and Coarsen
# 
# In this lesson, we cover some more advanced aspects of xarray.

# In[1]:


import numpy as np
import xarray as xr
from matplotlib import pyplot as plt
get_ipython().run_line_magic('xmode', 'Minimal')


# ## Interpolation
# 
# In the previous lesson on Xarray, we learned how to select data based on its dimension coordinates and align data with dimension different coordinates.
# But what if we want to estimate the value of the data variables at _different coordinates_.
# This is where interpolation comes in.

# In[2]:


# we write it out explicitly so we can see each point.
x_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
f = xr.DataArray(x_data**2, dims=['x'], coords={'x': x_data})
f


# In[3]:


f.plot(marker='o')


# We only have data on the integer points in x.
# But what if we wanted to estimate the value at, say, 4.5?

# In[4]:


f.sel(x=4.5)


# Interpolation to the rescue!

# In[5]:


f.interp(x=4.5)


# Interpolation uses [scipy.interpolate](https://docs.scipy.org/doc/scipy/reference/interpolate.html) under the hood.
# There are different modes of interpolation.

# In[6]:


# default
f.interp(x=4.5, method='linear').values


# In[7]:


f.interp(x=4.5, method='nearest').values


# In[8]:


f.interp(x=4.5, method='cubic').values


# We can interpolate to a whole new coordinate at once:

# In[9]:


x_new = x_data + 0.5
f_interp_linear = f.interp(x=x_new, method='linear')
f_interp_cubic = f.interp(x=x_new, method='cubic')
f.plot(marker='o', label='original')
f_interp_linear.plot(marker='o', label='linear')
f_interp_cubic.plot(marker='o', label='cubic')
plt.legend()


# Note that values outside of the original range are not supported:

# In[10]:


f_interp_linear.values


# ```{note}
# You can apply interpolation to any dimension, and even to multiple dimensions at a time.
# (Multidimensional interpolation only supports `mode='nearest'` and `mode='linear'`.)
# But keep in mind that _Xarray has no built-in understanding of geography_.
# If you use `interp` on lat / lon coordinates, it will just perform naive interpolation of the lat / lon values.
# More sophisticated treatment of spherical geometry requires another package such as [xesmf](https://xesmf.readthedocs.io/).
# ```

# ## Groupby
# 
# Xarray copies Pandas' very useful groupby functionality, enabling the "split / apply / combine" workflow on xarray DataArrays and Datasets. In the first part of the lesson, we will learn to use groupby by analyzing sea-surface temperature data.

# First we load a dataset. We will use the [NOAA Extended Reconstructed Sea Surface Temperature (ERSST) v5](https://www.ncdc.noaa.gov/data-access/marineocean-data/extended-reconstructed-sea-surface-temperature-ersst-v5) product, a widely used and trusted gridded compilation of of historical data going back to 1854.
# 
# Since the data is provided via an [OPeNDAP](https://en.wikipedia.org/wiki/OPeNDAP) server, we can load it directly without downloading anything:

# In[11]:


url = 'http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/noaa.ersst.v5/sst.mnmean.nc'
ds = xr.open_dataset(url, drop_variables=['time_bnds'])
ds = ds.sel(time=slice('1960', '2018')).load()
ds


# Let's do some basic visualizations of the data, just to make sure it looks reasonable.

# In[12]:


ds.sst[0].plot(vmin=-2, vmax=30)


# Note that xarray correctly parsed the time index, resulting in a Pandas datetime index on the time dimension.

# In[13]:


ds.time


# In[14]:


ds.sst.sel(lon=300, lat=50).plot()


# As we can see from the plot, the timeseries at any one point is totally dominated by the seasonal cycle. We would like to remove this seasonal cycle (called the "climatology") in order to better see the long-term variaitions in temperature. We will accomplish this using **groupby**.
# 
# The syntax of Xarray's groupby is almost identical to Pandas.
# We will first apply groupby to a single DataArray.

# In[15]:


get_ipython().run_line_magic('pinfo', 'ds.sst.groupby')


# ### Split Step
# 
# The most important argument is `group`: this defines the unique values we will us to "split" the data for grouped analysis. We can pass either a DataArray or a name of a variable in the dataset. Lets first use a DataArray. Just like with Pandas, we can use the time indexe to extract specific components of dates and times. Xarray uses a special syntax for this `.dt`, called the `DatetimeAccessor`.

# In[16]:


ds.time.dt


# In[17]:


ds.time.dt.month


# ds.time.dt.year

# We can use these arrays in a groupby operation:

# In[18]:


gb = ds.sst.groupby(ds.time.dt.month)
gb


# Xarray also offers a more concise syntax when the variable you're grouping on is already present in the dataset. This is identical to the previous line:

# In[19]:


gb = ds.sst.groupby('time.month')
gb


# Now that the data are split, we can manually iterate over the group. The iterator returns the key (group name) and the value (the actual dataset corresponding to that group) for each group.

# In[20]:


for group_name, group_da in gb:
    # stop iterating after the first loop
    break 
print(group_name)
group_da


# ### Map & Combine
# 
# Now that we have groups defined, it's time to "apply" a calculation to the group. Like in Pandas, these calculations can either be:
# - _aggregation_: reduces the size of the group
# - _transformation_: preserves the group's full size
# 
# At then end of the apply step, xarray will automatically combine the aggregated / transformed groups back into a single object.
# 
# ```{warning}
# Xarray calls the "apply" step `map`. This is different from Pandas!
# ```
# 
# The most fundamental way to apply is with the `.map` method.

# In[21]:


get_ipython().run_line_magic('pinfo', 'gb.map')


# #### Aggregations
# 
# `.apply` accepts as its argument a function. We can pass an existing function:

# In[22]:


gb.map(np.mean)


# Because we specified no extra arguments (like `axis`) the function was applied over all space and time dimensions. This is not what we wanted. Instead, we could define a custom function. This function takes a single argument--the group dataset--and returns a new dataset to be combined:

# In[23]:


def time_mean(a):
    return a.mean(dim='time')

gb.apply(time_mean)


# Like Pandas, xarray's groupby object has many built-in aggregation operations (e.g. `mean`, `min`, `max`, `std`, etc):

# In[24]:


# this does the same thing as the previous cell
sst_mm = gb.mean(dim='time')
sst_mm


# So we did what we wanted to do: calculate the climatology at every point in the dataset. Let's look at the data a bit.
# 
# _Climatlogy at a specific point in the North Atlantic_

# In[25]:


sst_mm.sel(lon=300, lat=50).plot()


# _Zonal Mean Climatolgoy_

# In[26]:


sst_mm.mean(dim='lon').transpose().plot.contourf(levels=12, vmin=-2, vmax=30)


# _Difference between January and July Climatology_

# In[27]:


(sst_mm.sel(month=1) - sst_mm.sel(month=7)).plot(vmax=10)


# #### Transformations
# 
# Now we want to _remove_ this climatology from the dataset, to examine the residual, called the _anomaly_, which is the interesting part from a climate perspective.
# Removing the seasonal climatology is a perfect example of a transformation: it operates over a group, but doesn't change the size of the dataset. Here is one way to code it.

# In[28]:


def remove_time_mean(x):
    return x - x.mean(dim='time')

ds_anom = ds.groupby('time.month').apply(remove_time_mean)
ds_anom


# ```{note}
# In the above example, we applied `groupby` to a `Dataset` instead of a `DataArray`.
# ```
# 
# Xarray makes these sorts of transformations easy by supporting _groupby arithmetic_.
# This concept is easiest explained with an example:

# In[29]:


gb = ds.groupby('time.month')
ds_anom = gb - gb.mean(dim='time')
ds_anom


# Now we can view the climate signal without the overwhelming influence of the seasonal cycle.
# 
# _Timeseries at a single point in the North Atlantic_

# In[30]:


ds_anom.sst.sel(lon=300, lat=50).plot()


# _Difference between Jan. 1 2018 and Jan. 1 1960_

# In[31]:


(ds_anom.sel(time='2018-01-01') - ds_anom.sel(time='1960-01-01')).sst.plot()


# ## Grouby-Related: Resample, Rolling, Coarsen
# 
# 
# ### Resample
# 
# Resample in xarray is nearly identical to Pandas.
# **It can be applied only to time-index dimensions.** Here we compute the five-year mean.
# It is effectively a group-by operation, and uses the same basic syntax.
# Note that resampling changes the length of the the output arrays.

# In[32]:


ds_anom_resample = ds_anom.resample(time='5Y').mean(dim='time')
ds_anom_resample


# In[33]:


ds_anom.sst.sel(lon=300, lat=50).plot()
ds_anom_resample.sst.sel(lon=300, lat=50).plot(marker='o')


# In[34]:


(ds_anom_resample.sel(time='2015-01-01', method='nearest') -
 ds_anom_resample.sel(time='1965-01-01', method='nearest')).sst.plot()


# ### Rolling
# 
# Rolling is also similar to pandas.
# It does not change the length of the arrays.
# Instead, it allows a moving window to be applied to the data at each point.

# In[35]:


ds_anom_rolling = ds_anom.rolling(time=12, center=True).mean()
ds_anom_rolling


# In[36]:


ds_anom.sst.sel(lon=300, lat=50).plot(label='monthly anom')
ds_anom_resample.sst.sel(lon=300, lat=50).plot(marker='o', label='5 year resample')
ds_anom_rolling.sst.sel(lon=300, lat=50).plot(label='12 month rolling mean', color='k')
plt.legend()


# ## Coarsen
# 
# `coarsen` is a simple way to reduce the size of your data along one or more axes.
# It is very similar to `resample` when operating on time dimensions; the key differnce is that `coarsen` only operates on fixed blocks of data, irrespective of the coordinate values, while `resample` actually looks at the coordinates to figure out, e.g. what month a particular data point is in. 
# 
# For regularly-spaced monthly data beginning in January, the following should be equivalent to annual resampling.
# However, results would different for irregularly-spaced data.

# In[37]:


ds.coarsen(time=12).mean()


# Coarsen also works on spatial coordinates (or any coordiantes).

# In[38]:


ds_coarse = ds.coarsen(lon=4, lat=4, boundary='pad').mean()
ds_coarse.sst.isel(time=0).plot(vmin=2, vmax=30, figsize=(12, 5), edgecolor='k')


# ## An Advanced Example
# 
# In this example we will show a realistic workflow with Xarray.
# We will
# - Load a "basin mask" dataset
# - Interpolate the basins to our SST dataset coordinates
# - Group the SST by basin
# - Convert to Pandas Dataframe and plot mean SST by basin

# In[39]:


basin = xr.open_dataset('http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NODC/.WOA09/.Masks/.basin/dods')
basin


# In[40]:


basin = basin.rename({'X': 'lon', 'Y': 'lat'})
basin


# In[41]:


basin_surf = basin.basin[0]
basin_surf


# In[42]:


basin_surf.plot(vmax=10)


# In[43]:


basin_surf_interp = basin_surf.interp_like(ds.sst, method='nearest')
basin_surf_interp.plot(vmax=10)


# In[44]:


ds.sst.groupby(basin_surf_interp).first()


# In[45]:


basin_mean_sst = ds.sst.groupby(basin_surf_interp).mean()
basin_mean_sst


# In[46]:


df = basin_mean_sst.mean('time').to_dataframe()
df


# In[47]:


import pandas as pd
basin_names = basin_surf.attrs['CLIST'].split('\n')
basin_df = pd.Series(basin_names, index=np.arange(1, len(basin_names)+1))
basin_df


# In[48]:


df = df.join(basin_df.rename('basin_name'))


# In[49]:


df.plot.bar(y='sst', x='basin_name')


# In[ ]:




