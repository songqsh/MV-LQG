#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:55:31 2019

@author: songqsh
"""

#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
#from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Make data.
T = 1.
x = 0.
y = 1.
z = -2.

P = np.linspace(0,1,11)
Q = np.linspace(0,1,11)
P, Q = np.meshgrid(P, Q)
#R = np.where(P+Q<=1., (P*x + Q*y+(1-P-Q)*z)**2/(1+T), .) 
R = (P*x + Q*y+(1-P-Q)*z)**2/(1+T)

fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(P, Q, R, cmap=cm.coolwarm)

ax.set_xlabel('p')
ax.set_xlim(0, 1)
ax.set_ylabel('q')
ax.set_ylim(0, 1)
ax.set_zlabel('v')
#ax.set_zlim(-100, 100)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()