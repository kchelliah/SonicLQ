# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 20:27:39 2014

@author: kc
"""

#import scipy

import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import pylab as pl
from matplotlib.pyplot import autumn
from matplotlib.afm import AFM
# from mpl_toolkits.axes_grid1 import make_axes_locatable
import scipy.ndimage



Nx = 45;
Ny = 21;
Xres = 0.5 * 2.54;
FILE = "/Users/kchelliah/Data/HighDR/R3/pH203X0N45";

# Set up a regular grid of interpolation points
X, Y = np.linspace(-(Nx-1)*Xres/2, (Nx-1)*Xres/2, Nx), np.linspace(-(Ny-1)*Xres/2, (Ny-1)*Xres/2, Ny)
X, Y = np.meshgrid(X, Y);

Z1 = np.loadtxt(FILE+".txt");
Z2 = np.reshape(Z1, (Nx, Ny));
Z = Z2.T;
Z = 20.0 * np.log10 (Z/0.00002);

X = scipy.ndimage.zoom(X, 6)
Y = scipy.ndimage.zoom(Y, 6)
Z = scipy.ndimage.zoom(Z, 6)




# Interpolate
# Zs = scipy.interpolate.griddata((Xs, Ys), Z, (X, Y), method='cubic')
levels = MaxNLocator(nbins=15).tick_values(Z.min(), Z.max())
cmap = plt.get_cmap('afmhot')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

im = plt.pcolormesh(X, Y, Z, cmap=cmap, norm=norm)
#plt.colorbar()
# set the limits of the plot to the limits of the data
plt.axis([X.min(), X.max(), Y.min(), Y.max()])

ax = plt.gca().set_aspect('equal', adjustable='box')

plt.xlabel('X (cm)')
plt.ylabel('Y (cm)')

plt.draw()
cb = plt.colorbar(im,fraction=0.0225, pad=0.04)
# cb.set_label('dB')
cb.ax.set_title('dB')


plt.savefig(FILE+".eps", bbox_inches="tight", format='eps', dpi=300)

plt.show()
