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


#%% Finite difference scheme non-opt

start_time = time.time()

un = np.ones(nx) #init temp array

for n in range(nt):    
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c*dt/dx*(un[i] - un[i - 1])


print("--- %s seconds ---" % (time.time() - start_time))

plt.plot(np.linspace(x0, x0 + L_tot, nx), u)

#%% Finite diff opt

start_time = time.time()


for n in range(nt):
    u = u - np.concatenate((np.array([0]), c*dt/dx*np.diff(u)))
    # subtract 0 from the first and c*dt/dx *diff from the others
    

print("--- %s seconds ---" % (time.time() - start_time))

plt.plot(np.linspace(x0, x0 + L_tot, nx), u)























