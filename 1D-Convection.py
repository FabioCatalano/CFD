# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:16:18 2024

@author: tarta
"""

import numpy as np
from matplotlib import pyplot as plt
import time, sys

x0 = 0 #initial coordinate
L_tot = 2 # length domain
nx = 41 # number of points in the domain
dx = L_tot/(nx - 1)
nt = 25 # number of timesteps
dt = 0.025 # time step
c = 1 # wave speed


#%% Set initial condition

# u = 2 if 0.5 <= x <= 1
# u = 1 everywhere else

L1 = 0.5
L2 = 1.0

if L2 <= L1:
    raise Exception("L2 has to be greater than L1")

u = np.ones(nx) # array of 1
u[int(L1/dx):int(L2/dx + 1)] = 2


#%% Plot initial condition

plt.plot(np.linspace(x0, x0 + L_tot, nx), u)


#%% Finite difference scheme

un = np.ones(nx) #init temp array

for n in range(nt):
    # u = u - c*dt/dx*np.diff(u)
    
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c*dt/dx*(un[i] - un[i - 1])


plt.plot(np.linspace(x0, x0 + L_tot, nx), u)



























