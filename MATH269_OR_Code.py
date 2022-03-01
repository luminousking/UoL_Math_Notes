# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:53:49 2022

@author: Luminous Isaac
"""
######################## Hadley-Whitin Algorithm ############################
from sympy import *
import math

def f(x):
    
    if 0<=x<=30:
        re = 1/30 ## change
    else:
        re = 0
        
    return re

def expectation():
    
    x = Symbol('x')
    
    Ex = integrate(x*1/30, (x, 0, 30)) ##change
    
    return Ex

def HWA(D, K, h, p, n):
    
    y_hat = math.sqrt((2 * D * (K + p * expectation())) / h)
    y_wave = (p * D) / h
    
    if y_wave < y_hat:
        return "Hadley-Whitin method will not converge."
    else:
        
        y = math.sqrt(2 * D * K / h)
        R = 30*(1 - y * h / (p * D)) ## change
        
        if n == 1:    
            return y, R
        else:
            for i in range(2, n+1):
                x = Symbol('x')
                S_R = integrate((x - R) / 30, (x, R, 30)) ##change
                y = math.sqrt((2 * D * (K + p * S_R)) / h)
                R = 30*(1 - y * h / (p * D)) ## change
                
    return y, R
    
    
HWA(17, 3, 1, 2, 4)



















































