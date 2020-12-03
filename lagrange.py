from math import pi

G = 6.67408e-11 # m^3 / (kg * s^2)
m1 = 5.972e24 # kg, mass of earth
m2 = 0.07346e24 # kg, mass of moon
l = 384400000 #m, distance from earth to moon
x1 = m2 * l / (m1 + m2)
x2 = m1 * l / (m1 + m2)
velocity = (G * (m1 + m2)/ l) ** 0.5
period = 2 * pi * l / velocity
theta_dot = 2*pi / period

def x_eqn(xs):
    return -G*m1/((xs + x1) * abs(xs +x1)) - G * m2 / ((xs - x2)*abs(xs-x2)) + \
            theta_dot**2 * xs

from numpy import arange

xvals = arange(-2*l, 2*l, 1000)

yvals = x_eqn(xvals)

import matplotlib.pyplot as plt

from scipy.optimize import root_scalar

L3 = root_scalar(x_eqn, bracket=[-4e8, -2e8])
print(L3.root+x1)

L1 = root_scalar(x_eqn, bracket=[2e8, 3.5e8])
print(L1.root+x1)

L2 = root_scalar(x_eqn, bracket=[3.9e8, 5e8])
print(L2.root+x1)

plt.plot(xvals, yvals)
plt.grid()
plt.ylim(-0.01, 0.01)
plt.show()
