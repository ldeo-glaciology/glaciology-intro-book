#!/usr/bin/env python
# coding: utf-8

# # Flow of the Antarctic Ice sheet
# 

# In[4]:


import fsspec
import xarray as xr
mapper = fsspec.get_mapper('gs://ldeo-glaciology/MEaSUREs')
M = xr.open_zarr(mapper) 
M


# In[5]:


import xarray.ufuncs as xu
speed = xu.sqrt(M.VX**2 + M.VY**2) 


# In[ ]:





# In[6]:


speed.isel(x=slice(4000,5500,2), y = slice(4000,5500,2)).plot()


# In[ ]:




