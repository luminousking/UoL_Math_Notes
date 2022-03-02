# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:53:49 2022

@author: Luminous Isaac
"""
######################## Linear Programming Plt #############################
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
#from pylab import figure, text, scatter, show
 
# Construct lines
x = np.linspace(0.0,50,100)
y1 = 3.0*x - 33
y2 = (-1/15)*x + 15
y3 = (14/5)*x - 28
 
# Make plot
plt.plot(x, y1, label=r'$y1 = 3.0*x - 33$')
plt.plot(x, y2, label=r'$y2 = (-1/15)*x + 15$')
plt.plot(x, y3, label=r'$y3 = (14/5)*x - 28$')
 
plt.xlim((0.0, 50.000))
plt.ylim((0.0, 50.000))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
 
# Fill feasible region
y5 = np.minimum(y1, y3)                                                                                                                                                                                                             
#y6 = np.maximum(y1, y3)
plt.fill_between(x, y5, y2, where=y5>y2, color='grey', alpha=0.5)
 
plt.grid(True, linestyle='-.')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
 
#plt.savefig('ordering_constraints.eps',dpi=600,bbox_inches='tight')
plt.show()

######################## Hadley-Whitin Algorithm ############################
from sympy import *
import math

def expectation():
    x = Symbol('x')
    Ex = integrate(x*1/32, (x, 0, 32)) ##change
    return Ex

def HWA(D, K, h, p, n):
    y_hat = math.sqrt((2 * D * (K + p * expectation())) / h)
    y_wave = (p * D) / h
    if y_wave < y_hat:
        return "Hadley-Whitin method will not converge."
    else:
        y = math.sqrt(2 * D * K / h)
        R = 32*(1 - y * h / (p * D)) ## change
        if n == 1:    
            return y, R
        else:
            for i in range(2, n+1):
                x = Symbol('x')
                S_R = integrate((x - R) / 32, (x, R, 32)) ##change
                y = math.sqrt((2 * D * (K + p * S_R)) / h)
                R = 32*(1 - y * h / (p * D)) ## change
    return y_hat, y_wave, y, R

HWA(30, 4, 0.48, 1.11, 3)




















































