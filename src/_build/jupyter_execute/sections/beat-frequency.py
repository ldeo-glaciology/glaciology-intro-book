#!/usr/bin/env python
# coding: utf-8

# # Beat frequency

# (under construction)

# The Autonomous radio-echo sounder (ApRES) uses the concept of *beat frequency* to compute the difference in the frequency between a transmitted signal and a received signal. From this frequency, the range to each englacial reflector can be calculated (see [here](apres-intro)).

# Beat freqencies occur when two waves with different frequencies are superimposed, producing a third wave that is the sum of the two original waves. Because the two waves are differnt frequencies, they gradually shift out of and into phase with one another  as time goes by. When they are in phase they interfere destructively and when they are out of phase they interfere destructively. So, as they shift in and out of phase the resulting wave increases and descreases in amplitude. This occurs at a particular frequency: the beat frequency. 
# 
# Below we explore this theoretically and numerically.
# 
# ## Numerical superposition of waves
# Let's start by getting a feel for what we expect to see by suprimposing some waves numerically. `

# We will define two waves $s_1$ and $s_2$ by 
# 
# $
# s_1 = A_1 \sin \left(\omega_1 t\right)
# $
# 
# and
# 
# $
# s_2 = A_2 \sin \left(\omega_2 t\right).
# $
# 
# Their amplitudes are $A_1$ and $A_2$, and their *angular frequencies* are $\omega_1$ and $\omega_2$.  
# 

# ```{note}
# Angular frequencies $\omega$ tell us how fast the phase of a wave increaes with time. The units of  $\omega$ are radians per second. Angular frequency is related to *frequency* $f$ by $\omega = 2\pi f$.
# 
# See the [page](phase-frequency-label) on phase and frequency for more details
# ```

# In[ ]:





# Let's plot both waves

# In[75]:


import numpy as np
import matplotlib.pyplot as plt

pi = np.pi                                # define pi
t = np.linspace(0.0, 40*pi, num=1000)     # define a time vector 

# define the first wave
omega_1 = 2
A_1 = 1
s1 = A_1*np.sin(omega_1*t)

# define the second wave
omega_2 = 1.8
A_2 = 1
s2 = A_2*np.sin(omega_2*t)


# In[94]:


plt.figure(figsize=(15, 5))
plt.plot(t,s1,t,s2);
plt.ylabel('our two waves')
plt.xlabel('time, $t$ [s]')
plt.legend(['$s_1$','$s_2$'],loc='lower left')
plt.show()


# In[86]:


plt.figure(figsize=(18, 5))
plt.plot(t,s1+s2);
plt.ylabel('$s_2$')
plt.xlabel('$t$ [s]')
plt.autoscale(enable=True, axis='x', tight=True)
plt.show()


# ## Analytical superposition of waves
# 
# 
# 
# Assuming for now that the amplitudes of the waves are the same ($A_1 = A_2$) and using a *sum-to-product trignometric identity*, the sum of the two waves is 
# $$
# s_3 = s_1 + s_2 = 2A\sin\left( \pi \left(f_1+f_2 \right) t \right) \cos\left( \pi \left(f_1-f_2 \right) t \right)
# $$

# In[ ]:




