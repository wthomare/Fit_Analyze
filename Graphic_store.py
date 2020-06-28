# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

class Graphic_store(object):
    
    def __init__(self, parameters, logger):
        self.parameters = parameters
        self.logger = logger
        
    def asRadians(self, degrees):
        return degrees * np.pi / 180
    
    def getXYpos(self, relativeNullPoint, p):
        """ Calculates X and Y distances in meters.
        """
        deltaLatitude = p['latitude'] - relativeNullPoint['latitude']
        deltaLongitude = p['longitude'] - relativeNullPoint['longitude']
        latitudeCircumference = 40075160 * np.cos(self.asRadians(relativeNullPoint['latitude']))
        resultX = deltaLongitude * latitudeCircumference / 360
        resultY = deltaLatitude * 40008000 / 360
        return resultX, resultY
    
    def draw_3d(self, name, latitude, longitude, z):

        initial = {'latitude':latitude[0], 'longitude':longitude[0]}
        x, y = [], []
        
        for i in range(min(len(latitude), len(longitude))):
            xi, yi = self.getXYpos(initial, {'latitude':latitude[i], 'longitude':longitude[i]})
            x.append(xi)
            y.append(yi)
        
        x = np.array(x)
        y = np.array(y)            

        mpl.rcParams['legend.fontsize'] = 8
        
        fig = plt.figure()
        ax = fig.gca(projection='3d')
    
        ax.plot(x, y, z, label='3d curve')
        ax.legend()
        
        plt.savefig(fname=name + '_3d' + '.jpeg', dpi =2096)
        
    def draw_2D_enriched(self, name, latitude, longitude, data):
        
        initial = {'latitude':latitude[0], 'longitude':longitude[0]}
        x, y = [], []
        
        for i in range(min(len(latitude), len(longitude))):
            xi, yi = self.getXYpos(initial, {'latitude':latitude[i], 'longitude':longitude[i]})
            x.append(xi)
            y.append(yi)
        
        x = np.array(x)
        y = np.array(y)        

        norm = (data-data.min())/(data.max()-data.min())*255
        
        segments = [[(x[i],y[i]), (x[i+1], y[i+1])] for i in range(len(x)-1)]
        colors = [plt.cm.viridis(int(y)) for y in norm]
    
        norm_colorbar = plt.Normalize(norm.min(), norm.max())
        lc = LineCollection(segments, colors=colors, norm = norm_colorbar)
        fig, ax = plt.subplots()
        line = ax.add_collection(lc)
        fig.colorbar(line, ax=ax)
        ax.add_collection(lc)
        
        ax.autoscale()
        ax.margins(0.1)
        plt.savefig(fname=name[:-4] + '_altitude'+ '.jpeg', dpi =2096)
    
    def draw_contour(self, filename):
        df = pd.read_csv(filename)
        initial = {'latitude':df['position_lat'].iloc[0], 'longitude':df['position_long'].iloc[0]}
        
        latitude = np.array(df['position_lat'])
        longitude = np.array(df['position_long'])
        z = np.array(df['altitude'])
        z_delta = z + 0.1
        
        Z = np.transpose(np.array([z,z_delta]))
        
        x, y = [], []
        
        for i in range(min(len(latitude), len(longitude))):
            xi, yi = self.getXYpos(initial, {'latitude':latitude[i], 'longitude':longitude[i]})
            x.append(xi)
            y.append(yi)
            
        X = np.array([x for u in range(len(x))])
        Y = np.array([y for u in range(len(y))])
        
        print('X shape %s' %str(X.shape))
        print('Y shape %s' %str(Y.shape))
        print('Z shape %s' %str(Z.shape))
    
        mpl.rcParams['legend.fontsize'] = 8
        
        fig = plt.figure()
        ax = fig.gca(projection='3d')   
    
        
        cset = ax.contour(X, Y, Z, cmap=cm.coolwarm)
        ax.clabel(cset, fontsize=9, inline=1)
    
        ax.plot(X, Y, Z, label='parametric curve')
        ax.legend()
        
        plt.savefig(fname=filename[:-4] + '.jpeg', dpi =4096)