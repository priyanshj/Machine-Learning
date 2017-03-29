# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 22:49:57 2017

@author: priyansh
"""

from math import sqrt

plot1 = [1,3]
plot2 = [2,5]

euclidean_distance = sqrt((plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2)

print(euclidean_distance)