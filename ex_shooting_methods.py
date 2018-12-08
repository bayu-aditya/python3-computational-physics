## example8_1
import numpy as np
from run_kut4 import integrate
#from ridder import ridder
from bayu_optimalisasi import bisectioninc
from printSoln import printSoln
import matplotlib.pyplot as plt

def initCond(u): # Init. values of [y,y’]; use ’u’ if unknown
    return np.array([0.0, u])

def r(u): # Boundary condition residual--see Eq. (8.3)
    X,Y = integrate(F,xStart,initCond(u),xStop,h)
    y = Y[len(Y) - 1]
    r = y[0] - 1.0
    return r

def F(x,y): # First-order differential equations
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -3.0*y[0]*y[1]
    #F[1] = 2.*y[1]/7. + y[0]/7. - x/7.
    return F

xStart = 0.0 # Start of integration
xStop = 2.0 # End of integration
u1 = 1.0 # 1st trial value of unknown init. cond.
u2 = 2.0 # 2nd trial value of unknown init. cond.
h = 0.1 # Step size
freq = 2 # Printout frequency
#u = ridder(r,u1,u2) # Compute the correct initial condition
u = bisectioninc(r,u1,u2)
X,Y = integrate(F,xStart,initCond(u),xStop,h)
printSoln(X,Y,freq)
plt.plot(X,Y)
plt.show()