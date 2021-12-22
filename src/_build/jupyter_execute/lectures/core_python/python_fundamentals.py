#!/usr/bin/env python
# coding: utf-8

# # Python Fundamentals
# 
# This material is mostly adapted from the [official python tutorial](https://docs.python.org/3/tutorial/), Copyright 2001-2019, Python Software Foundation. It is used here under the terms of the [Python License](https://docs.python.org/3/license.html).

# ## Invoking Python ##
# 
# There are three main ways to use Python.
# 
# 1. By running a Python file, e.g. `python myscript.py`
# 1. Through an interactive console (Python interpreter or iPython shell)
# 1. In an interactive notebook (e.g. Jupyter)
# 
# In this course, we will mostly be interacting with Python via Jupyter notebooks.

# ## Python Versions ##
# 
# There are two versions of the Python language out there: Python 2 and Python 3. In 2019, the vast majority of the scientific community now uses Python 3. As new Python learners, you should definitely learn Python 3. But it is important to be aware that Python 2 exists, since you might encounter it in the wild. 
# 
# Some of the main changes introduced in Python 3 are:
# 
# * ``print`` is a function
# * Integer division returns a float
# * Iterators behave differently
# * Unicode is used for encoding code
# 

# ## Basic Variables: Numbers and String ##

# In[1]:


# comments are anything that comes after the "#" symbol
a = 1       # assign 1 to variable a
b = "hello" # assign "hello" to variable b


# The following identifiers are used as reserved words, or keywords of the language, and cannot be used as ordinary identifiers. They must be spelled exactly as written here:
# 
#     False      class      finally    is         return
#     None       continue   for        lambda     try
#     True       def        from       nonlocal   while
#     and        del        global     not        with
#     as         elif       if         or         yield
#     assert     else       import     pass
#     break      except     in         raise
#     
# Additionally, the following a built in functions which are always available in your namespace once you open a Python interpreter
# 
#     abs() dict() help() min() setattr() all() dir() hex() next() slice() any()
#     divmod() id() object() sorted() ascii() enumerate() input() oct() staticmethod()
#     bin() eval() int() open() str() bool() exec() isinstance() ord() sum() bytearray()
#     filter() issubclass() pow() super() bytes() float() iter() print() tuple()
#     callable() format() len() property() type() chr() frozenset() list() range()
#     vars() classmethod() getattr() locals() repr() zip() compile() globals() map()
#     reversed() __import__() complex() hasattr() max() round() delattr() hash()
#     memoryview() set()
# 
# 

# In[2]:


# how to we see our variables?
print(a)
print(b)
print(a,b)


# All variables are objects. Every object has a type (class). To find out what type your variables are

# In[3]:


print(type(a))
print(type(b))


# In[4]:


# as a shortcut, iPython notebooks will automatically print whatever is on the last line
type(b)


# In[5]:


# we can check for the type of an object
print(type(a) is int)
print(type(a) is str)


# Different objects attributes and methods, which can be accessed via the syntax ``variable.method``
# 
# IPython will autocomplete if you press ``<tab>`` to show you the methods available.

# In[6]:


# this returns the method itself
b.capitalize


# In[7]:


# this calls the method
b.capitalize()
# there are lots of other methods


# In[8]:


# binary operations act differently on different types of objects
c = 'World'
print(b + c)
print(a + 2)
print(a + b)


# ## Math ##
# 
# Basic arithmetic and boolean logic is part of the core Python library.

# In[9]:


# addition / subtraction
1+1-5


# In[10]:


# multiplication
5 * 10


# In[11]:


# division
1/2


# In[12]:


# that was automatically converted to a float
type(1/2)


# In[13]:


# exponentiation
2**4


# In[14]:


# rounding
round(9/10)


# In[15]:


# built in complex number support
(1+2j) / (3-4j)


# In[16]:


# logic
True and True


# In[17]:


True and False


# In[18]:


True or True


# In[19]:


(not True) or (not False)


# ## Conditionals ##
# 
# The first step to programming. Plus an intro to Python syntax.

# In[20]:


x = 100
if x > 0:
    print('Positive Number')
elif x < 0:
    print('Negative Number')
else:
    print ('Zero!')


# In[21]:


# indentation is MANDATORY
# blocks are closed by indentation level
if x > 0:
    print('Positive Number')
    if x >= 100:
        print('Huge number!')


# ## More Flow Control ##

# In[22]:


# make a loop 
count = 0
while count < 10:
    # bad way
    # count = count + 1
    # better way
    count += 1
print(count)


# In[23]:


# use range
for i in range(5):
    print(i)


# __Important point__: in Python, we always count from 0!

# In[24]:


# what is range?
type(range)


# In[25]:


get_ipython().run_line_magic('pinfo', 'range')


# In[26]:


# iterate over a list we make up
for pet in ['dog', 'cat', 'fish']:
    print(pet, len(pet))


# What is the thing in brackets? __A list!__ Lists are one of the core Python data structures.
# 
# ## Lists ##

# In[27]:


l = ['dog', 'cat', 'fish']
type(l)


# In[28]:


# list have lots of methods
l.sort()
l


# In[29]:


# we can convert a range to a list
r = list(range(5))
r


# In[30]:


while r:
    p = r.pop()
    print('p:', p)
    print('r:', r)


# There are many different ways to interact with lists. Exploring them is part of the fun of Python.
# 
# __list.append(x)__ Add an item to the end of the list. Equivalent to a[len(a):] = [x].
# 
# __list.extend(L)__ 
# Extend the list by appending all the items in the given list. Equivalent to a[len(a):] = L.
# 
# __list.insert(i, x)__ Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
# 
# __list.remove(x)__ Remove the first item from the list whose value is x. It is an error if there is no such item.
# 
# __list.pop([i])__ Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
# 
# __list.clear()__ Remove all items from the list. Equivalent to del a[:].
# 
# __list.index(x)__ Return the index in the list of the first item whose value is x. It is an error if there is no such item.
# 
# __list.count(x)__ Return the number of times x appears in the list.
# 
# __list.sort()__ Sort the items of the list in place.
# 
# __list.reverse()__ Reverse the elements of the list in place.
# 
# __list.copy()__ Return a shallow copy of the list. Equivalent to a[:].
# 
# 
# Don't assume you know how list operations work!

# In[31]:


# "add" two lists
x = list(range(5))
y = list(range(10,15))
z = x + y
z


# In[32]:


# access items from a list
print('first', z[0])
print('last', z[-1])
print('first 3', z[:3])
print('last 3', z[-3:])
print('middle, skipping every other item', z[5:10:2])


# __MEMORIZE THIS SYNTAX!__ It is central to so much of Python and often proves confusing for users coming from other languages.
# 
# In terms of set notation, Python indexing is _left inclusive_, _right exclusive_. If you remember this, you will never go wrong.

# In[33]:


# that means we get an error from the following
N = len(z)
z[N]


# In[34]:


# this index notation also applies to strings
name = 'Ryan Abernathey'
print(name[:4])


# In[35]:


# you can also test for the presence of items in a list
5 in z


# Lists are not meant for math! They don't have a datatype.

# In[36]:


z[4] = 'fish'
z


# Python is full of tricks for iterating and working with lists

# In[37]:


# a cool Python trick: list comprehension
squares = [n**2 for n in range(5)]
squares


# In[38]:


# iterate over two lists together uzing zip
for item1, item2 in zip(x,y):
    print('first:', item1, 'second:', item2)


# ## Other Data Structures ##
# 
# We are almost there. We have the building blocks we need to do basic programming. But Python has some other data structures we need to learn about.
# 
# ## Tuples ##
# 
# Tuples are similar to lists, but they are _immutable_—they can't be extended or modified. What is the point of this? Generally speaking: to pack together inhomogeneous data. Tuples can then be unpacked and distributed by other parts of your code.
# 
# Tuples may seem confusing at first, but with time you will come to appreciate them.

# In[39]:


# tuples are created with parentheses, or just commas
a = ('Ryan', 33, True)
b = 'Takaya', 25, False
type(b)


# In[40]:


# can be indexed like arrays
print(a[1]) # not the first element!


# In[41]:


# and they can be unpacked
name, age, status = a


# ## Dictionaries ##
# 
# This is an extremely useful data structure. It maps __keys__ to __values__.
# 
# Dictionaries are unordered!

# In[42]:


# different ways to create dictionaries
d = {'name': 'Ryan', 'age': 33}
e = dict(name='Takaya', age=25)
e


# In[43]:


# access a value
d['name']


# Square brackets ``[...]`` are Python for "get item" in many different contexts.

# In[44]:


# test for the presence of a key
print('age' in d)
print('height' in e)


# In[45]:


# try to access a non-existant key
d['height']


# In[46]:


# add a new key
d['height'] = (5,11) # a tuple
d


# In[47]:


# keys don't have to be strings
d[99] = 'ninety nine'
d


# In[48]:


# iterate over keys
for k in d:
    print(k, d[k])


# In[49]:


# better way
### Python 2
### for key, val in d.iteritems()
for key, val in d.items():
    print(key, val)

