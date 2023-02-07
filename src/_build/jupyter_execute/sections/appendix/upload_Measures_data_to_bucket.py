#!/usr/bin/env python
# coding: utf-8

# # Adding the MEASURES data to the google bucket
# for use  in antarctic-ice-flow.ipnb

# code to put measures in the bucket (where is the original code I used!?!)

# ## Download
# To download the data from NSIDC to your local machine, run the following command. You will need an free account with NASA Earthdata Login account. More details can be found [here](https://urs.earthdata.nasa.gov/profile). Then replace <uid> and <password> in the command below with your Earthdata Login username and password (do not include brackets).

# In[8]:


get_ipython().system('wget --http-user=jkingslake --http-password=Hendrix1 https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0484.002/1996.01.01/antarctica_ice_velocity_450m_v2.nc')


# ## Load

# Load the data lazily (so that it isnt all loaded into memory at once) using xarray

# In[11]:


import xarray as xr
ds = xr.open_dataset('antarctica_ice_velocity_450m_v2.nc', chunks = {})


# Inspect the size of the dataset and take a look at the coordinates, variables and dimensions. 

# In[12]:


print(f"the dataset is {ds.nbytes/1e9} Gb")


# In[13]:


ds


# ## Rechunk
# Zarr stores are ways of stored multi-dimensional data in a way this is optimized for fast access from distributed cloud computing. Zarr stores use a concept called chunks. Chunks are the smallest units of data that can be downloaded one-at-a-time. It is best to make them smaller than the total size fo the dataset, becuase then you can avoid downloading ~7 Gb every time, but makign them too small introduces overheads that slow things down. The chunk size that the dataset has by default after loading from a netcdf (as we did above) may not be ideal, so one needs to inspect the chunk size and 'rechunk' is nessesary. 
# 
# For this dataset, it turns out that if you split each variable into four chunks you get about the right size of chunk. The following cell does this. 

# In[31]:


import numpy as np
nx = ds.x.shape[0]
ny = ds.y.shape[0]
ds_rechunked = ds.chunk({'y': np.ceil(ny/2), 'x': np.ceil(nx/2)})
ds_rechunked


# ## Write to bucket
# To write this to the google bucket, we require an authentication token, that is private. To do yourself you will need your own google bucket and token specific to that bucket. 

# In[32]:


import zarr
import json
import gcsfs
import xarray as xr 


# The cell below uses the token to generate a 'file-like object' called `mapper`, which can then be used with the xarray method `to_zarr` to write the dataset to the zarr store.  

# In[37]:


with open('/Users/jkingslake/Documents/science/ldeo-glaciology-bc97b12df06b.json') as token_file:
    token = json.load(token_file)
gcs = gcsfs.GCSFileSystem(token=token)
mapper = gcs.get_mapper('gs://ldeo-glaciology/temp/measures') 


# In[38]:


ds_rechunked.to_zarr(mapper)


# ## Reload
# To check that the data was uploaded correctly, reload the data using the syntax that will be used in the main page making use of these data

# In[36]:


import fsspec
mapper_reload = fsspec.get_mapper('gs://ldeo-glaciology/measures')
ds_reloaded = xr.open_zarr(mapper_reload) 
ds_reloaded


# In[3]:


MEASURES = xr.open_zarr(mapper)  
MEASURES


# In[ ]:




