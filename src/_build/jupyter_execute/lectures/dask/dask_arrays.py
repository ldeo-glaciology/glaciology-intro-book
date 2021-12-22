#!/usr/bin/env python
# coding: utf-8

# # Computing with Dask

# ## Dask Arrays
# 
# A dask array looks and feels a lot like a numpy array.
# However, a dask array doesn't directly hold any data.
# Instead, it symbolically represents the computations needed to generate the data.
# Nothing is actually computed until the actual numerical values are needed.
# This mode of operation is called "lazy"; it allows one to build up complex, large calculations symbolically before turning them over the scheduler for execution.
# 
# If we want to create a numpy array of all ones, we do it like this:

# In[1]:


import numpy as np
shape = (1000, 4000)
ones_np = np.ones(shape)
ones_np


# This array contains exactly 32 MB of data:

# In[2]:


ones_np.nbytes / 1e6


# Now let's create the same array using dask's array interface.

# In[3]:


import dask.array as da
ones = da.ones(shape)
ones


# The dask array representation reveals the concept of "chunks". "Chunks" describes how the array is split into sub-arrays. We did not specify any chunks, so Dask just used one single chunk for the array. This is not much different from a numpy array at this point.
# 
# ### Specifying Chunks
# 
# However, we could have split up the array into many chunks.
# 
# ![Dask Arrays](http://dask.pydata.org/en/latest/_images/dask-array-black-text.svg)
# _source: [Dask Array Documentation](http://dask.pydata.org/en/latest/array-overview.html)_
# 
# There are [several ways to specify chunks](http://dask.pydata.org/en/latest/array-creation.html#chunks).
# In this lecture, we will use a block shape.

# In[4]:


chunk_shape = (1000, 1000)
ones = da.ones(shape, chunks=chunk_shape)
ones


# Notice that we just see a symbolic represetnation of the array, including its shape, dtype, and chunksize.
# No data has been generated yet.
# When we call `.compute()` on a dask array, the computation is trigger and the dask array becomes a numpy array.

# In[5]:


ones.compute()


# In order to understand what happened when we called `.compute()`, we can visualize the dask _graph_, the symbolic operations that make up the array

# In[6]:


ones.visualize()


# Our array has four chunks. To generate it, dask calls `np.ones` four times and then concatenates this together into one array.
# 
# Rather than immediately loading a dask array (which puts all the data into RAM), it is more common to want to reduce the data somehow. For example

# In[7]:


sum_of_ones = ones.sum()
sum_of_ones.visualize()


# Here we see dask's strategy for finding the sum. This simple example illustrates the beauty of dask: it automatically designs an algorithm appropriate for custom operations with big data. 
# 
# If we make our operation more complex, the graph gets more complex.

# In[8]:


fancy_calculation = (ones * ones[::-1, ::-1]).mean()
fancy_calculation.visualize()


# ### A Bigger Calculation
# 
# The examples above were toy examples; the data (32 MB) is nowhere nearly big enough to warrant the use of dask.
# 
# We can make it a lot bigger!

# In[9]:


bigshape = (200000, 4000)
big_ones = da.ones(bigshape, chunks=chunk_shape)
big_ones


# In[10]:


big_ones.nbytes / 1e6


# This dataset is 3.2 GB, rather MB! This is probably close to or greater than the amount of available RAM than you have in your computer. Nevertheless, dask has no problem working on it.
# 
# _Do not try to `.visualize()` this array!_
# 
# When doing a big calculation, dask also has some tools to help us understand what is happening under the hood

# In[11]:


from dask.diagnostics import ProgressBar

big_calc = (big_ones * big_ones[::-1, ::-1]).mean()

with ProgressBar():
    result = big_calc.compute()
result


# ### Reduction 
# 
# All the usual numpy methods work on dask arrays.
# You can also apply numpy function directly to a dask array, and it will stay lazy.

# In[12]:


big_ones_reduce = (np.cos(big_ones)**2).mean(axis=0)
big_ones_reduce


# Plotting also triggers computation, since we need the actual values

# In[13]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (12,8)


# In[14]:


plt.plot(big_ones_reduce)


# ## Distributed Clusters
# 
# Once we are ready to make a bigger calculation with dask, we can use a Dask [Distributed](http://distributed.dask.org/en/stable/) cluster.
# 
# ```{warning}
# A common mistake is to move to distributed mode too soon.
# For smaller data, distributed will actually be _much slower_ than the default multi-threaded scheduler or **not using Dask at all**.
# You should only use distributed when your data is much larger than what your computer can handle in memory.
# ```
# 
# ### Local Cluster
# 
# A local cluster uses all the CPU cores of the machine it is running on.
# For our cloud-based Jupyterlab environments, that is just 2 cores--not very much.
# However, it's good to know about.

# In[15]:


from dask.distributed import Client, LocalCluster
cluster = LocalCluster()
client = Client(cluster)
client


# Note that the "Dashboard" link will open a new page where you can monitor a computation's progress.

# In[16]:


big_calc.compute()


# Here is another bigger calculation.

# In[17]:


random_values = da.random.normal(size=(2e8,), chunks=(1e6,))
hist, bins = da.histogram(random_values, bins=100, range=[-5, 5]) 
hist


# In[18]:


# actually trigger the computation
hist_c = hist.compute()


# In[19]:


# plot results
x = 0.5 * (bins[1:] + bins[:-1])
width = np.diff(bins)
plt.bar(x, hist_c, width);


# ### Dask Gateway - A Cluster in the Cloud
# 
# Pangeo Cloud makes it possible to launch a much larger cluster using many virtual machines in the cloud.
# This is beyond the scope of our class, but you can read more about it in the [Pangeo Cloud docs](https://pangeo.io/cloud.html#dask)

# ## Dask + XArray
# 
# Xarray can automatically wrap its data in dask arrays.
# This capability turns xarray into an extremely powerful tool for Big Data earth science
# 
# To see this in action, we will open a dataset from the [Pangeo Cloud Data Catalog](https://catalog.pangeo.io/) - the Copernicus [Sea Surface Height](browse/master/ocean/sea_surface_height/) dataset.

# In[20]:


from intake import open_catalog
cat = open_catalog("https://raw.githubusercontent.com/pangeo-data/pangeo-datastore/master/intake-catalogs/ocean.yaml")
ds  = cat["sea_surface_height"].to_dask()
ds


# Note that the values are not displayed, since that would trigger computation.

# In[21]:


ds.sla[0].plot()


# In[ ]:


# the computationally intensive step
sla_timeseries = ds.sla.mean(dim=('latitude', 'longitude')).load()


# In[ ]:


sla_timeseries.plot(label='full data')
sla_timeseries.rolling(time=365, center=True).mean().plot(label='rolling annual mean')
plt.ylabel('Sea Level Anomaly [m]')
plt.title('Global Mean Sea Level')
plt.legend()
plt.grid()

