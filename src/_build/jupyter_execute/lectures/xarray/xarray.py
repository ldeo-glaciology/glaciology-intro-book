#!/usr/bin/env python
# coding: utf-8

# # Xarray Fundamentals

# ## Xarray data structures
# 
# Like Pandas, xarray has two fundamental data structures:
# * a `DataArray`, which holds a single multi-dimensional variable and its coordinates
# * a `Dataset`, which holds multiple variables that potentially share the same coordinates
# 
# ### DataArray
# 
# A `DataArray` has four essential attributes:
# * `values`: a `numpy.ndarray` holding the array’s values
# * `dims`: dimension names for each axis (e.g., `('x', 'y', 'z')`)
# * `coords`: a dict-like container of arrays (coordinates) that label each point (e.g., 1-dimensional arrays of numbers, datetime objects or strings)
# * `attrs`: an `OrderedDict` to hold arbitrary metadata (attributes)
# 
# Let's start by constructing some DataArrays manually 

# In[1]:


import numpy as np
import xarray as xr
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (8,5)


# A simple DataArray without dimensions or coordinates isn't much use.

# In[2]:


da = xr.DataArray([9, 0, 2, 1, 0])
da


# We can add a dimension name...

# In[3]:


da = xr.DataArray([9, 0, 2, 1, 0], dims=['x'])
da


# But things get most interesting when we add a coordinate:

# In[4]:


da = xr.DataArray([9, 0, 2, 1, 0],
                  dims=['x'],
                  coords={'x': [10, 20, 30, 40, 50]})
da


# This coordinate has been used to create an _index_, which works very similar to a Pandas index.
# In fact, under the hood, Xarray just reuses Pandas indexes.

# In[5]:


da.indexes


# Xarray has built-in plotting, like pandas.

# In[6]:


da.plot(marker='o')


# ### Multidimensional DataArray
# 
# If we are just dealing with 1D data, Pandas and Xarray have very similar capabilities. Xarray's real potential comes with multidimensional data.
# 
# Let's go back to the multidimensional ARGO data we loaded in the numpy lesson.

# In[7]:


import pooch
url = "https://www.ldeo.columbia.edu/~rpa/float_data_4901412.zip"
files = pooch.retrieve(url, processor=pooch.Unzip(), known_hash="2a703c720302c682f1662181d329c9f22f9f10e1539dc2d6082160a469165009")
files


# In[8]:


T = np.load(files[0])
S = np.load(files[1])
date = np.load(files[2])
lon = np.load(files[3])
levels = np.load(files[4])
P = np.load(files[5])
lat = np.load(files[6])


# Let's organize the data and coordinates of the salinity variable into a DataArray.

# In[9]:


da_salinity = xr.DataArray(S, dims=['level', 'date'],
                           coords={'level': levels,
                                   'date': date},)
da_salinity


# In[10]:


da_salinity.plot(yincrease=False)


# Attributes can be used to store metadata. What metadata should you store? The [CF Conventions](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html#_description_of_the_data) are a great resource for thinking about climate metadata. Below we define two of the required CF-conventions attributes.

# In[11]:


da_salinity.attrs['units'] = 'PSU'
da_salinity.attrs['standard_name'] = 'sea_water_salinity'
da_salinity


# Now if we plot the data again, the name and units are automatically atachhed to the figure.

# In[12]:


da_salinity.plot()


# ### Datasets
# 
# A Dataset holds many DataArrays which potentially can share coordinates. In analogy to pandas:
# 
#     pandas.Series : pandas.Dataframe :: xarray.DataArray : xarray.Dataset
#     
# Constructing Datasets manually is a bit more involved in terms of syntax. The Dataset constructor takes three arguments:
# 
# * `data_vars` should be a dictionary with each key as the name of the variable and each value as one of:
#   * A `DataArray` or Variable
#   * A tuple of the form `(dims, data[, attrs])`, which is converted into arguments for Variable
#   * A pandas object, which is converted into a `DataArray`
#   * A 1D array or list, which is interpreted as values for a one dimensional coordinate variable along the same dimension as it’s name
# * `coords` should be a dictionary of the same form as data_vars.
# * `attrs` should be a dictionary.
# 
# Let's put together a Dataset with temperature, salinity and pressure all together

# In[13]:


argo = xr.Dataset(
    data_vars={
        'salinity':    (('level', 'date'), S),
        'temperature': (('level', 'date'), T),
        'pressure':    (('level', 'date'), P)
    },
    coords={
        'level': levels,
        'date': date
    }
)
argo


# What about lon and lat? We forgot them in the creation process, but we can add them after the fact.

# In[14]:


argo.coords['lon'] = lon
argo


# That was not quite right...we want lon to have dimension `date`:

# In[15]:


del argo['lon']
argo.coords['lon'] = ('date', lon)
argo.coords['lat'] = ('date', lat)
argo


# ### Coordinates vs. Data Variables
# 
# Data variables can be modified through arithmentic operations or other functions. Coordinates are always keept the same.

# In[16]:


argo * 10000


# Clearly lon and lat are coordinates rather than data variables. We can change their status as follows:

# In[17]:


argo = argo.set_coords(['lon', 'lat'])
argo


# The `*` symbol in the representation above indicates that `level` and `date` are "dimension coordinates" (they describe the coordinates associated with data variable axes) while `lon` and `lat` are "non-dimension coordinates". We can make any variable a non-dimension coordiante.
# 
# Alternatively, we could have assigned directly to coords as follows:

# In[18]:


argo.coords['lon'] = ('date', lon)
argo.coords['lat'] = ('date', lat)


# ## Selecting Data (Indexing)
# 
# We can always use regular numpy indexing and slicing on DataArrays

# In[19]:


argo.salinity[2]


# In[20]:


argo.salinity[2].plot()


# In[21]:


argo.salinity[:, 10]


# In[22]:


argo.salinity[:, 10].plot()


# However, it is often much more powerful to use xarray's `.sel()` method to use label-based indexing.

# In[23]:


argo.salinity.sel(level=2)


# In[24]:


argo.salinity.sel(level=2).plot()


# In[25]:


argo.salinity.sel(date='2012-10-22')


# In[26]:


argo.salinity.sel(date='2012-10-22').plot(y='level', yincrease=False)


# `.sel()` also supports slicing. Unfortunately we have to use a somewhat awkward syntax, but it still works.

# In[27]:


argo.salinity.sel(date=slice('2012-10-01', '2012-12-01'))


# In[28]:


argo.salinity.sel(date=slice('2012-10-01', '2012-12-01')).plot()


# `.sel()` also works on the whole Dataset

# In[29]:


argo.sel(date='2012-10-22')


# ## Computation
# 
# Xarray dataarrays and datasets work seamlessly with arithmetic operators and numpy array functions.

# In[30]:


temp_kelvin = argo.temperature + 273.15
temp_kelvin.plot(yincrease=False)


# We can also combine multiple xarray datasets in arithemtic operations

# In[31]:


g = 9.8
buoyancy = g * (2e-4 * argo.temperature - 7e-4 * argo.salinity)
buoyancy.plot(yincrease=False)


# ## Broadcasting, Aligment, and Combining Data
# 
# ### Broadcasting
# 
# Broadcasting arrays in numpy is a nightmare. It is much easier when the data axes are labeled!
# 
# This is a useless calculation, but it illustrates how perfoming an operation on arrays with differenty coordinates will result in automatic broadcasting

# In[32]:


level_times_lat = argo.level * argo.lat
level_times_lat


# In[33]:


level_times_lat.plot()


# ### Alignment
# 
# If you try to perform operations on DataArrays that share a dimension name, Xarray will try to _align_ them first.
# This works nearly identically to Pandas, except that there can be multiple dimensions to align over.
# 
# To see how alignment works, we will create some subsets of our original data.

# In[34]:


sa_surf = argo.salinity.isel(level=slice(0, 20))
sa_mid = argo.salinity.isel(level=slice(10, 30))


# By default, when we combine multiple arrays in mathematical operations, Xarray performs an "inner join".

# In[35]:


(sa_surf * sa_mid).level


# We can override this behavior by manually aligning the data

# In[36]:


sa_surf_outer, sa_mid_outer = xr.align(sa_surf, sa_mid, join='outer')
sa_surf_outer.level


# As we can see, missing data (NaNs) have been filled in where the array was extended.

# In[37]:


sa_surf_outer.plot(yincrease=False)


# We can also use `join='right'` and `join='left'`.

# ### Combing Data: Concat and Merge
# 
# The ability to combine many smaller arrays into a single big Dataset is one of the main advantages of Xarray.
# To take advantage of this, we need to learn two operations that help us combine data:
# - `xr.contact`: to concatenate multiple arrays into one bigger array along their dimensions
# - `xr.merge`: to combine multiple different arrays into a dataset
# 
# First let's look at concat. Let's re-combine the subsetted data from the previous step.

# In[38]:


sa_surf_mid = xr.concat([sa_surf, sa_mid], dim='level')
sa_surf_mid


# ```{warning}
# Xarray won't check the values of the coordinates before `concat`. It will just stick everything together into a new array.
# ```
# 
# In this case, we had overlapping data. We can see this by looking at the `level` coordinate.

# In[39]:


sa_surf_mid.level


# In[40]:


plt.plot(sa_surf_mid.level.values, marker='o')


# We can also concat data along a _new_ dimension, e.g.

# In[41]:


sa_concat_new = xr.concat([sa_surf, sa_mid], dim='newdim')
sa_concat_new


# Note that the data were aligned using an _outer_ join along the non-concat dimensions.
# 
# Instead of specifying a new dimension name, we can pass a new Pandas index object explicitly to `concat`.
# This will create a new dimension coordinate and corresponding index.
# 
# We can merge both DataArrays and Datasets.

# In[42]:


xr.merge([argo.salinity, argo.temperature])


# If the data are not aligned, they will be aligned before merge.
# We can specify the join options in `merge`.

# In[43]:


xr.merge([
    argo.salinity.sel(level=slice(0, 30)),
    argo.temperature.sel(level=slice(30, None))
])


# In[44]:


xr.merge([
    argo.salinity.sel(level=slice(0, 30)),
    argo.temperature.sel(level=slice(30, None))
], join='left')


# ## Reductions
# 
# Just like in numpy, we can reduce xarray DataArrays along any number of axes:

# In[45]:


argo.temperature.mean(axis=0)


# In[46]:


argo.temperature.mean(axis=1)


# However, rather than performing reductions on axes (as in numpy), we can perform them on dimensions. This turns out to be a huge convenience

# In[47]:


argo_mean = argo.mean(dim='date')
argo_mean


# In[48]:


argo_mean.salinity.plot(y='level', yincrease=False)


# In[49]:


argo_std = argo.std(dim='date')
argo_std.salinity.plot(y='level', yincrease=False)


# ### Weighted Reductions
# 
# Sometimes we want to perform a reduction (e.g. a mean) where we assign different weight factors to each point in the array.
# Xarray supports this via [weighted array reductions](http://xarray.pydata.org/en/stable/user-guide/computation.html#weighted-array-reductions).
# 
# As a toy example, imagine we want to weight values in the upper ocean more than the lower ocean.
# We could imagine creating a weight array exponentially proportional to pressure as follows:

# In[50]:


mean_pressure = argo.pressure.mean(dim='date')
p0 = 250  # dbat
weights = np.exp(-mean_pressure / p0)
weights.plot()


# The weighted mean over the `level` dimensions is calculated as follows:

# In[51]:


temp_weighted_mean = argo.temperature.weighted(weights).mean('level')


# Comparing to the unweighted mean, we see the difference:

# In[52]:


temp_weighted_mean.plot(label='weighted')
argo.temperature.mean(dim='level').plot(label='unweighted')
plt.legend()


# ## Loading Data from netCDF Files
# 
# NetCDF (Network Common Data Format) is the most widely used format for distributing geoscience data. NetCDF is maintained by the [Unidata](https://www.unidata.ucar.edu/) organization.
# 
# Below we quote from the [NetCDF website](https://www.unidata.ucar.edu/software/netcdf/docs/faq.html#whatisit):
# 
# >NetCDF (network Common Data Form) is a set of interfaces for array-oriented data access and a freely distributed collection of data access libraries for C, Fortran, C++, Java, and other languages. The netCDF libraries support a machine-independent format for representing scientific data. Together, the interfaces, libraries, and format support the creation, access, and sharing of scientific data.
# >
# >NetCDF data is:
# >
# > - Self-Describing. A netCDF file includes information about the data it contains.
# > - Portable. A netCDF file can be accessed by computers with different ways of storing integers, characters, and floating-point numbers.
# > - Scalable. A small subset of a large dataset may be accessed efficiently.
# > - Appendable. Data may be appended to a properly structured netCDF file without copying the dataset or redefining its structure.
# > - Sharable. One writer and multiple readers may simultaneously access the same netCDF file.
# > - Archivable. Access to all earlier forms of netCDF data will be supported by current and future versions of the software.
# 
# Xarray was designed to make reading netCDF files in python as easy, powerful, and flexible as possible. (See [xarray netCDF docs](http://xarray.pydata.org/en/latest/io.html#netcdf) for more details.)
# 
# Below we download and load some the NASA [GISSTemp](https://data.giss.nasa.gov/gistemp/) global temperature anomaly dataset.

# In[53]:


gistemp_file = pooch.retrieve(
    'https://data.giss.nasa.gov/pub/gistemp/gistemp1200_GHCNv4_ERSSTv5.nc.gz',
    known_hash='eb645c5de8f43f0850cffac446066ea7e593b156ea26df4b5117f96ba757e654',
    processor=pooch.Decompress(),
)


# In[54]:


ds = xr.open_dataset(gistemp_file)
ds


# In[55]:


ds.tempanomaly.isel(time=-1).plot()


# In[56]:


ds.tempanomaly.mean(dim=('lon', 'lat')).plot()


# In[ ]:




