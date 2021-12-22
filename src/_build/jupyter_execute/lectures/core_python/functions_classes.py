#!/usr/bin/env python
# coding: utf-8

# # Python Functions and Classes
# 
# For longer and more complex tasks, it is important to organize your code into reuseable elements.
# For example, if you find yourself cutting and pasting the same or similar lines of code over and over,
# you probably need to define a _function_ to encapsulate that code and make it reusable.
# An important principle in programming in **DRY**: "don't repeat yourself".
# Repetition is tedious and opens you up to errors. Strive for elegance and simplicity in your programs.

# In[ ]:





# ## Functions
# 
# Functions are a central part of advanced python programming. Functions take some inputs ("arguments") and do something in response.
# Usually functions return something, but not always.

# In[1]:


# define a function
def say_hello():
    """Return the word hello."""
    return 'Hello'


# In[2]:


# functions are also objects
type(say_hello)


# In[3]:


# this doesnt call
get_ipython().run_line_magic('pinfo', 'say_hello')


# In[4]:


# this does
say_hello()


# In[5]:


# assign the result to something
res = say_hello()
res


# In[6]:


# take some arguments
def say_hello_to(name):
    """Return a greeting to `name`"""
    return 'Hello ' + name


# In[7]:


# intended usage
say_hello_to('World')


# In[8]:


say_hello_to(10)


# In[9]:


# redefine the function
def say_hello_to(name):
    """Return a greeting to `name`"""
    return 'Hello ' + str(name)


# In[10]:


say_hello_to(10)


# In[11]:


# take an optional keyword argument
def say_hello_or_hola(name, spanish=False):
    """Say hello in multiple languages."""
    if spanish:
        greeting = 'Hola '
    else:
        greeting = 'Hello '
    return greeting + name


# In[12]:


print(say_hello_or_hola('Ryan'))
print(say_hello_or_hola('Juan', spanish=True))


# In[13]:


# flexible number of arguments
def say_hello_to_everyone(*args):
    return ['hello ' + str(a) for a in args]


# In[14]:


say_hello_to_everyone('Ryan', 'Juan', 'Xiaomeng')


# ### Pure vs. Impure Functions
# 
# Functions that don't modify their arguments or produce any other side-effects are called [_pure_](https://en.wikipedia.org/wiki/Pure_function). 
# 
# Functions that modify their arguments or cause other actions to occur are called _impure_.
# 
# Below is an impure function.

# In[15]:


def remove_last_from_list(input_list):
    input_list.pop()


# In[16]:


names = ['Ryan', 'Juan', 'Xiaomeng']
remove_last_from_list(names)
print(names)
remove_last_from_list(names)
print(names)


# We can do something similar with a pure function.
# 
# In general, pure functions are safer and more reliable.

# In[17]:


def remove_last_from_list_pure(input_list):
    new_list = input_list.copy()
    new_list.pop()
    return new_list


# In[18]:


names = ['Ryan', 'Juan', 'Xiaomeng']
new_names = remove_last_from_list_pure(names)
print(names)
print(new_names)


# We could spend the rest of the day talking about functions, but we have to move on.

# ### Namespaces
# 
# In python, a [namespace](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces) is a mapping between variable names and python object. You can think of it like a dictionary.
# 
# The namespace can change depending on where you are in your program. Functions can "see" the variables in the parent namespace, but they can also redefine them in a private scope.

# In[19]:


name = 'Ryan'

def print_name():
    print(name)

def print_name_v2():
    name = 'Kerry'
    print(name)
    
print_name()
print_name_v2()
print(name)


# ### A more complex function: Fibonacci Sequence
# 
# The Fibonacci sequence is the 1,1,2,3,5,8..., the sum of each number with the preceding one. Write a function to compute the Fibonacci sequence of length n. (Hint, use some list methods.)

# In[20]:


def fib(n):
    l = [1,1]
    for i in range(n-2):
        l.append(l[-1] + l[-2])
    return l


# In[21]:


fib(10)


# ## Classes
# 
# We have worked with many different types of python objects so far: strings, lists, dictionaries, etc. These objects have different attributes and respond in different ways to the built-in functions (`len`, etc.)
# 
# _How can we make our own, custom objects?_ Answer: by defining classes.
# 
# ### A class to represent a hurricane

# In[22]:


class Hurricane:
    
    def __init__(self, name):
        self.name = name


# In[23]:


h = Hurricane('florence')
h


# Our class only has a single attribute so far:

# In[24]:


h.name


# Let's add more, along with some input validation:

# In[25]:


class Hurricane:
    
    def __init__(self, name, category, lon):
        self.name = name.upper()
        self.category = int(category)
        
        if lon > 180 or lon < -180:
            raise ValueError(f'Invalid lon {lon}')
        self.lon = lon
        


# In[26]:


h = Hurricane('florence', 4, -46)
h


# In[27]:


h.name


# In[28]:


h = Hurricane('ryan', 5, 300)


# Now let's add a custom method:

# In[29]:


class Hurricane:
    
    def __init__(self, name, category, lon):
        self.name = name.upper()
        self.category = int(category)
        
        if lon > 180 or lon < -180:
            raise ValueError(f'Invalid lon {lon}')
        self.lon = lon
    
    def is_dangerous(self):
        return self.category > 1


# In[30]:


f = Hurricane('florence', 4, -46)
f.is_dangerous()


# ### Magic / dunder methods
# 
# We can implement special methods that begin with double-underscores (i.e. "dunder" methods), which allow us to customize the behavior of our classes. ([Read more here](https://www.python-course.eu/python3_magic_methods.php)). We have already learned one: `__init__`. Let's implement the `__repr__` method to make our class display something pretty.

# In[31]:


class Hurricane:
    
    def __init__(self, name, category, lon):
        self.name = name.upper()
        self.category = int(category)
        
        if lon > 180 or lon < -180:
            raise ValueError(f'Invalid lon {lon}')
        self.lon = lon
        
    def __repr__(self):
        return f"<Hurricane {self.name} (cat {self.category})>"
    
    def is_dangerous(self):
        return self.category > 1


# In[32]:


f = Hurricane('florence', 4, -46)
f


# In[ ]:




