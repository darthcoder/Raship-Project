#! /usr/bin/python2
"""This is a module that returns the analytical velocity field once u_i(y) and 
    cos(l_i*z) are know. The variables might be renamed this is just a guide. 
    m&b refers to text.
"""

from math import cos, sin, hypot, pi
TOL = 1e-6

def velocity(ha, asp, y_co, z_co):
    """Sums the fourier modes and obtains the velocity analytical solution
    From the fourier modes of y and z contributions.
    """
    i = 1
    u = 0.0
    
    uiy = u_y(ha, asp, i, y_co)
    uiz = u_z(asp, z_co, i)

    while uiy*uiz >= TOL: 
        uiy = u_y(ha, asp, y_co, i)
        uiz = u_z(asp, z_co, i)

        u += uiy*uiz
        i += 2
        
    return u

def u_z(a, z, i):
    """The z contribution to velocity from formulae in m&b
    Oneliner form is better. Lambda form is complicated to use?
    """
    return cos(0.5*a*i*pi*z)

def u_y(h, a, y, i):
    """The y contribution of velocity
    Most work goes in here.
    """

# The solution has a tendency to blowup as we are using hyperbolic 
# functions. This is to prevent that from occuring

    if h/(a*i*pi) >= 10.0:
        return 0.0

    return y
    


    
