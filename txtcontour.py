# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 20:27:39 2014

@author: kc
"""

#import scipy

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib.pyplot import autumn
# from matplotlib.afm import AFM

Nx = 45;
Ny = 21;
Xres = 0.5;
FILE = "/Users/kchelliah/Data/HighDR/R3/pH203X0N45";

# Set up a regular grid of interpolation points
X, Y = np.linspace(-(Nx-1)*Xres/2, (Nx-1)*Xres/2, Nx), np.linspace(-(Ny-1)*Xres/2, (Ny-1)*Xres/2, Ny)
X, Y = np.meshgrid(X, Y);

Z1 = np.loadtxt(FILE+".txt");
Z2 = np.reshape(Z1, (Nx, Ny));
Z = Z2.T;
Z = 20.0 * np.log10 (Z/0.00002);

# Interpolate
#Zs = scipy.interpolate.griddata((Xs, Ys), Z, (X, Y), method='cubic')

im = plt.pcolormesh(X, Y, Z)
#plt.colorbar()
# set the limits of the plot to the limits of the data
plt.axis([X.min(), X.max(), Y.min(), Y.max()])

plt.gca().set_aspect('equal', adjustable='box')
plt.draw()

# from mpl_toolkits.axes_grid1 import make_axes_locatable
# divider = make_axes_locatable(plt.gca())
# cax = divider.append_axes("right", "5%", pad="3%")
# plt.colorbar(im, cax=cax)
# plt.tight_layout()

#plt.imshow(Z, vmin=Z.min(), vmax=Z.max(), origin='lower',
#           extent=[X.min(), X.max(), Y.min(), Y.max()])
##plt.scatter(X, Y, c=Z)
#plt.colorbar()
 plt.show()


#% Zmin = min(min(Z));
#% Zmax = max(max(Z));
#% CutOff = Zmax - DynRange;
#
#% FILE1 = strcat(FILE,'.pdf');
#XX = linspace(min(X(:)),max(X(:)),1000) ;
#YY = linspace(min(Y(:)),max(Y(:)),1000) ;
#[XX, YY] = meshgrid( XX, YY) ;
#Zs = interp2(X, Y, Z, XX, YY) ;
#
#% Zs(Zs<CutOff) = NaN ; % get rid of data for Zs<cutoff
# Zs = flipdim(Zs,1);
#
#
#contourf(XX,YY,Zs'',100); colormap(hot); shading flat; hold on; rectangle('Position',[-3.0,-0.25,6.0,0.5]); alpha(1.0);

#axis equal;
#   ylim([-((Ny-1)*Xres/2) ((Ny-1)*Xres/2)]);
#   xlim([-((Nx-1)*Xres/2) ((Nx-1)*Xres/2)]);
#% xlabel('X (in)','FontSize',16), ylabel('Y (in)','FontSize',16);
#h = colorbar; % label = get(h,'yticklabel') ; newLabel = str2num(label)./1; set(h,'yticklabel',sprintf('%0.1f|',newLabel) );
#xlabel(h,'dB','FontSize',18);
#set(gca,'FontSize',20);
#set(gcf, 'PaperUnits', 'inches', 'PaperPosition', [0 0 1300 900]/150);
#print ('-dpdf', '-r150', strcat(FILE,'.pdf'));
#% close(gcf);