#!/usr/bin/env python
# coding: utf-8

# (frequency-and-range)=
# # Frequency and range

# Many of the material on this and following pages can be found in the [ApRES manual](https://github.com/ldeo-glaciology/phase-sensitive-radar-processing/blob/5cce6bd838cb70e290316195af9ceefe3d4a52ee/other%20documents/ApRES%20Manual%20V102.1.pdf), Brennan et al., ????, and Nicholls et al. 2015. 
# 
# ApRES emits 'chirps', which consist of continuous radio waves lasting 1 second. Due each chirp the frequency of the emmitted radio wave increased linearly with time from $f1$ to $f2$ where the bandwidth $B = f2-f1$. The signal is transmitted downwards into the ice sheet and is partly reflected back to the radar's receiving antenna where it is compared to the transmitted signal to determine the travel time of the signal and hence the range to sub-surface reflectors. Specifically, at every moment during a chirp the radar measures the difference between the frequency of the reveived signal and signal being tranmistted in that instant. Because the transmitted signal is always increasing in frequency and because the reveived signal was tranmitted a few milliseconds earlier than it is received, the recieved signal is always lower frequency than the transmitted signal. 
# 
# 
# 
# 

# ## TO do: add cartoon of chirp and delay in received signal

# ## To do: derive Equation 1 from Brennan et al. 

# This expression describes how the frequency difference between the transmitted signal and the received signal relates to the range to a reflector detected by ApRES. What we havent discussed is how this frequency difference is calculated. Next, we discuss how combining and summing the received and transmitted signals, then filtering the result, allows this to be computed using the concept of *beat frequency*
