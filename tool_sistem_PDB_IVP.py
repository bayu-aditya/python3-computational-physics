# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:13:45 2018

@author: Bayu Aditya
"""
""" -------PILIH SALAH SATU--------- """
#from modul_euler import integrate
from modul_run_kut4 import integrate

import numpy as np
import matplotlib.pyplot as plt

import timeit
start = timeit.default_timer()

m = 50
k = 30
b = 10
f0 = 0
wext = 1

def F(x,y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = (f0*np.cos(wext*x) - b*y[1] - k*y[0])/m
    return F

x = 0.0                                         # Start of integration
xStop = 100.0                                  # End of integration
y = np.array([1., 3.])       # Initial values of {y}
h = 0.2                                         # Step size

X,Y = integrate(F,x,y,xStop,h)

""" Hanya Numerik """
plt.plot(X,Y[:,0],'--')

""" Numerik dan Analitik """
#fun = lambda x: np.exp(-x)
#plt.plot(X,Y[:,0],'o',X,fun(X))

plt.grid(True)
plt.xlabel('x'); plt.ylabel('y')
plt.legend(('Numerical','Exact'),loc=0)
plt.show()
#input("Press return to exit")

stop = timeit.default_timer()
execution_time = stop - start
print("Program ini berdurasi {:7.10f} detik".format(execution_time)) #It returns time in sec   