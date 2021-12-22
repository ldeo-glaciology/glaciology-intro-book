#!/usr/bin/env python
# coding: utf-8

# # Processing examples
# 
# This notebook contains examples of doing some processing. 
# 
# 
# 

# It can include equations etc.
# 
# $
# \phi_d(t) = \phi_t(t) - \phi_r(t)
# $

# In[25]:


import numpy as np
import math
import matplotlib.pyplot as plt


# Define physical constants

# In[31]:


epsilon = 2.1;    # the dielectric permittivity of the cable

c= 3e8;

B = 200e6
T = 1; 
pi = math.pi
K = 2*pi*B/T

t = np.linspace(0.0, 1.0, num=100)

omega_c = 2*pi*300

## range and two-way travel time
R = 10 # m
tau =  2*R/(c/1.8)

phi_d = omega_c * tau + K*tau*(t - T/2) - K*tau**2 /2

f_d = 4*pi*B*R*np.sqrt(epsilon)/c/T
print(f_d)


# The phase $\phi$ is a linear function of time $t$.
# 

# In[29]:


plt.plot(t,phi_d);
plt.ylabel('phi [rad]')
plt.xlabel('t [s]')
plt.show()

