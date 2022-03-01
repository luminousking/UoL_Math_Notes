# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:53:49 2022

@author: Luminous Isaac
"""
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




















































