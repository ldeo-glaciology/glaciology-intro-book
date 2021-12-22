#!/usr/bin/env python
# coding: utf-8

# # Xarray Tips and Tricks

# ## Build a multi-file dataset from an OpenDAP server
# 
# One thing we love about xarray is the `open_mfdataset` function, which combines many netCDF files into a single xarray Dataset.
# 
# But what if the files are stored on a remote server and accessed over OpenDAP. An example can be found in NOAA's NCEP Reanalysis catalog.
# 
# https://www.esrl.noaa.gov/psd/thredds/catalog/Datasets/ncep.reanalysis/surface/catalog.html
# 
# The dataset is split into different files for each variable and year. For example, a single file for surface air temperature looks like:
# 
# http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis/surface/air.sig995.1948.nc
# 
# We can't just call
# 
#     open_mfdataset("http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis/surface/air.sig995.*.nc")
#     
# Because wildcard expansion doesn't work with OpenDAP endpoints. The solution is to manually create a list of files to open.

# In[1]:


base_url = 'http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis/surface/air.sig995'

files = [f'{base_url}.{year}.nc' for year in range(1948, 2019)]
files


# In[2]:


import xarray as xr
get_ipython().run_line_magic('matplotlib', 'inline')

ds = xr.open_mfdataset(files)
ds


# We have now opened the entire ensemble of files on the remote server as a single xarray Dataset!

# ## Perform Correlation Analysis
# 
# Many people want to look at correlations (usually in time) in their final projects.
# Unfortunately, this is not currently part of xarray (but it will be added soon! -- see [open issue](https://github.com/pydata/xarray/issues/1115)).
# 
# In the meantime, the following functions works pretty well.

# In[3]:


def covariance(x, y, dims=None):
    return xr.dot(x - x.mean(dims), y - y.mean(dims), dims=dims) / x.count(dims)

def corrrelation(x, y, dims=None):
    return covariance(x, y, dims) / (x.std(dims) * y.std(dims))


# In[4]:


ds = xr.open_dataset('NOAA_NCDC_ERSST_v3b_SST.nc')
ds


# In[5]:


sst = ds.sst
sst_clim = sst.groupby('time.month').mean(dim='time')
sst_anom = sst.groupby('time.month') - sst_clim

get_ipython().run_line_magic('matplotlib', 'inline')
sst_anom[0].plot()


# In[6]:


sst_ref = sst_anom.sel(lon=200, lat=0, method='nearest')
sst_ref.plot()


# In[7]:


sst_cor = corrrelation(sst_anom, sst_ref, dims='time')
pc = sst_cor.plot()
pc.axes.set_title('Correlation btw. global SST Anomaly and SST Anomaly at one point')


# ## Fix poorly encoded time coordinates
# 
# Many datasets, especially from INGRID, are encoded with "months since" as the time unit. Trying to open these in xarray currently gives an error.

# In[8]:


import cftime
cftime.__version__


# In[9]:


import xarray as xr

url = 'http://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NCEP/.CPC/.CAMS_OPI/.v0208/.mean/.prcp/dods'
ds = xr.open_dataset(url)


# One way to avoid this is to simply not decode the times:

# In[10]:


ds = xr.open_dataset(url, decode_times=False)
ds


# However, this is not satisfying, because now we can't use xarray's time aware features (like resample).
# 
# A better option has recently become possible. First we need the latest development version of the [cftime](https://github.com/Unidata/cftime) package.

# In[11]:


def fix_calendar(ds, timevar='T'):
    if ds[timevar].attrs['calendar'] == '360':
        ds[timevar].attrs['calendar'] = '360_day'
    return ds

ds = fix_calendar(ds)
ds = xr.decode_cf(ds)
ds


# In[ ]:




