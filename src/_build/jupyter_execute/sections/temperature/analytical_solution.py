#!/usr/bin/env python
# coding: utf-8

# # An analytical solution
# In this section we apply the general heat equation we derived in the previous section to a simplified scenario in which we have no advection and the temperature and the ice-sheet surface varies sinusoidally with time. Under these condictions an 'analytical' solution to the equation can be found, i.e. one which does not require any computational methods to derive. Analytical solutions are useful for building intuition for the physics and for testing numerical solutions.

# Our full heat equation, derived on the previous page is 
# 
# $$
# \frac{\partial T}{\partial t} = 
# -   u  \frac{\partial T}{\partial x}
# - v  \frac{\partial T}{\partial y}
# -  w  \frac{\partial T}{\partial z}  
# +  \frac{1}{c \rho}\left[\frac{\partial}{\partial x} \left( K \frac{\partial T}{\partial x}  \right)
#   +  \frac{\partial}{\partial y} \left( K \frac{\partial T}{\partial y}  \right)
#   +  \frac{\partial}{\partial z} \left( K \frac{\partial T}{\partial z}  \right)\right]
# $$(Heat_eq_full)
