#!/usr/bin/env python
# coding: utf-8

# # Numpy and Matplotlib
# 
# This lecture will introduce NumPy and Matplotlib.
# These are two of the most fundamental parts of the scientific python "ecosystem".
# Most everything else is built on top of them.
# 
# 
# <img src="https://numpy.org/images/logos/numpy.svg" width="100px" />
# 
# **Numpy**: _The fundamental package for scientific computing with Python_
# 
# - Website: <https://numpy.org/>
# - GitHub: <https://github.com/numpy/numpy>
# 
# <img src="https://matplotlib.org/_static/logo2_compressed.svg" width="300px" />
# 
# **Matlotlib**: _Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python._
# 
# - Website: <https://matplotlib.org/>
# - GitHub: <https://github.com/matplotlib/matplotlib>
# 
# ## Importing and Examining a New Package
# 
# This will be our first experience with _importing_ a package which is not part of the Python [standard library](https://docs.python.org/3/library/).

# In[1]:


import numpy as np


# What did we just do? We _imported_ a package. This brings new variables (mostly functions) into our interpreter. We access them as follows.

# In[2]:


# find out what is in our namespace
dir()


# In[3]:


# find out what's in numpy
dir(np)


# In[4]:


# find out what version we have
np.__version__


# There is no way we could explicitly teach each of these functions. The numpy documentation is crucial!
# 
# https://numpy.org/doc/stable/reference/
# 
# ## NDArrays
# 
# The core class is the numpy ndarray (n-dimensional array).
# 
# The main difference between a numpy array an a more general data container such as `list` are the following:
# - Numpy arrays can have N dimensions (while lists, tuples, etc. only have 1)
# - Numpy arrays hold values of the same datatype (e.g. `int`, `float`), while `lists` can contain anything.
# - Numpy optimizes numerical operations on arrays. Numpy is _fast!_

# In[5]:


from IPython.display import Image
Image(url='http://docs.scipy.org/doc/numpy/_images/threefundamental.png')


# In[6]:


# create an array from a list
a = np.array([9,0,2,1,0])


# In[7]:


# find out the datatype
a.dtype


# In[8]:


# find out the shape
a.shape


# In[9]:


# what is the shape
type(a.shape)


# In[10]:


# another array with a different datatype and shape
b = np.array([[5,3,1,9],[9,2,3,0]], dtype=np.float64)

# check dtype and shape
b.dtype, b.shape


# ```{note}
# The fastest varying dimension is the last dimension! The outer level of the hierarchy is the first dimension. (This is called "c-style" indexing)
# ```

# ## Array Creation
# 
# There are lots of ways to create arrays.

# In[11]:


# create some uniform arrays
c = np.zeros((9,9))
d = np.ones((3,6,3), dtype=np.complex128)
e = np.full((3,3), np.pi)
e = np.ones_like(c)
f = np.zeros_like(d)


# `arange` works very similar to `range`, but it populates the array "eagerly" (i.e. immediately), rather than generating the values upon iteration.

# In[12]:


np.arange(10)


# `arange` is left inclusive, right exclusive, just like `range`, but also works with floating-point numbers.

# In[13]:


np.arange(2,4,0.25)


# A frequent need is to generate an array of N numbers, evenly spaced between two values. That is what `linspace` is for.

# In[14]:


np.linspace(2,4,20)


# In[15]:


# log spaced
np.logspace(1,2,10)


# Numpy also has some utilities for helping us generate multi-dimensional arrays.
# `meshgrid` creates 2D arrays out of a combination of 1D arrays.

# In[16]:


x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.linspace(-np.pi, np.pi, 50)
xx, yy = np.meshgrid(x, y)
xx.shape, yy.shape


# ## Indexing
# 
# Basic indexing is similar to lists

# In[17]:


# get some individual elements of xx
xx[0,0], xx[-1,-1], xx[3,-5]


# In[18]:


# get some whole rows and columns
xx[0].shape, xx[:,-1].shape


# In[19]:


# get some ranges
xx[3:10,30:40].shape


# There are many advanced ways to index arrays. You can [read about them](https://numpy.org/doc/stable/reference/arrays.indexing.html) in the manual. Here is one example.

# In[20]:


# use a boolean array as an index
idx = xx<0
yy[idx].shape


# In[21]:


# the array got flattened
xx.ravel().shape


# ## Visualizing Arrays with Matplotlib
# 
# It can be hard to work with big arrays without actually seeing anything with our eyes!
# We will now bring in Matplotib to start visualizating these arrays.
# For now we will just skim the surface of Matplotlib.
# Much more depth will be provided in the next chapter.

# In[22]:


from matplotlib import pyplot as plt


# For plotting a 1D array as a line, we use the `plot` command.

# In[23]:


plt.plot(x)


# There are many ways to visualize 2D data.
# He we use `pcolormesh`.

# In[24]:


plt.pcolormesh(xx)


# In[25]:


plt.pcolormesh(yy)


# ## Array Operations ##
# 
# There are a huge number of operations available on arrays. All the familiar arithemtic operators are applied on an element-by-element basis.
# 
# ### Basic Math

# In[26]:


f = np.sin(xx) * np.cos(0.5*yy)


# In[27]:


plt.pcolormesh(f)


# ## Manipulating array dimensions ##

# Swapping the dimension order is accomplished by calling `transpose`.

# In[28]:


f_transposed = f.transpose()
plt.pcolormesh(f_transposed)


# We can also manually change the shape of an array...as long as the new shape has the same number of elements.

# In[29]:


g = np.reshape(f, (8,9))


# However, be careful with reshapeing data!
# You can accidentally lose the structure of the data.

# In[30]:


g = np.reshape(f, (200,25))
plt.pcolormesh(g)


# We can also "tile" an array to repeat it many times.

# In[31]:


f_tiled = np.tile(f,(3, 2))
plt.pcolormesh(f_tiled)


# Another common need is to add an extra dimension to an array.
# This can be accomplished via indexing with `None`.

# In[32]:


x.shape


# In[33]:


x[None, :].shape


# In[34]:


x[None, :, None, None].shape


# ## Broadcasting
# 
# 
# Not all the arrays we want to work with will have the same size.
# One approach would be to manually "expand" our arrays to all be the same size, e.g. using `tile`.
# _Broadcasting_ is a more efficient way to multiply arrays of different sizes
# Numpy has specific rules for how broadcasting works.
# These can be confusing but are worth learning if you plan to work with Numpy data a lot.
# 
# The core concept of broadcasting is telling Numpy which dimensions are supposed to line up with each other.

# In[35]:


Image(url='http://scipy-lectures.github.io/_images/numpy_broadcasting.png',
     width=720)


# Dimensions are automatically aligned _starting with the last dimension_.
# If the last two dimensions have the same length, then the two arrays can be broadcast.

# In[36]:


print(f.shape, x.shape)
g = f * x
print(g.shape)


# In[37]:


plt.pcolormesh(g)


# However, if the last two dimensions are _not_ the same, Numpy cannot just automatically figure it out.

# In[38]:


# multiply f by y
print(f.shape, y.shape)
h = f * y


# We can help numpy by adding an extra dimension to `y` at the end.
# Then the length-50 dimensions will line up.

# In[39]:


print(f.shape, y[:, None].shape)
h = f * y[:, None]
print(h.shape)


# In[40]:


plt.pcolormesh(h)


# ## Reduction Operations
# 
# In scientific data analysis, we usually start with a lot of data and want to reduce it down in order to make plots of summary tables.
# Operations that reduce the size of numpy arrays are called "reductions".
# There are many different reduction operations. Here we will look at some of the most common ones.

# In[41]:


# sum
g.sum()


# In[42]:


# mean
g.mean()


# In[43]:


# standard deviation
g.std()


# A key property of numpy reductions is the ability to operate on just one axis.

# In[44]:


# apply on just one axis
g_ymean = g.mean(axis=0)
g_xmean = g.mean(axis=1)


# In[45]:


plt.plot(x, g_ymean)


# In[46]:


plt.plot(g_xmean, y)


# ## Data Files
# 
# It can be useful to save numpy data into files.

# In[47]:


np.save('g.npy', g)


# ```{warning}
# Numpy `.npy` files are a convenient way to store temporary data, but they are not considered a robust archival format.
# Later we will learn about NetCDF, the recommended way to store earth and environmental data.
# ```

# In[48]:


g_loaded = np.load('g.npy')

np.testing.assert_equal(g, g_loaded)


# In[ ]:




