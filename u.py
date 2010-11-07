#! /usr/bin/python2
"""This is a module that returns the analytical velocity.
Once u_i(y) and cos(l_i*z) are know. The variables might be renamed 
this is just a guide. 
m&b refers to text.
"""

from math import fabs, cos, sin, cosh, sinh, hypot, pi
TOL = 1e-6

def velocity(ha, asp, y_co, z_co):
    """Return final velocity at some point in domain.
    From the fourier modes of y and z contributions.
    """
    i = 1
    u = 0.0
    
    uiy = u_y(ha, asp, i, y_co)
    uiz = u_z(asp, z_co, i)

    while 1: 
        uiy = u_y(ha, asp, y_co, i)
        uiz = u_z(asp, z_co, i)

        if fabs(uiy*uiz) <= TOL:
            break
        u += uiy*uiz
        i += 2
        
        
    return u

def u_z(a, z, i):
    """The z contribution to velocity from formulae in m&b
    Oneliner form is better. Lambda form is complicated to use?
    """
    return cos(0.5*i*pi*a*z)

def f(y, p1, p2):
    """intermediary function for u_y computation
    """
    return sinh(p1)*cosh(p2*y)-sinh(p2)*cosh(p1*y)

def u_y(h, a, y, i):
    """The y contribution of velocity, from formula.
    Most work goes in here.
    """
    l = 0.5*i*pi*a
    k = -2*a*sin(l/a)/l  
    pi1 = 0.5*(h - hypot(h, 2*l))
    pi2 = 0.5*(h + hypot(h, 2*l))
    
    return (k/l**2)*(1-(f(y, pi1, pi2)/f(1.0, pi1, pi2)))
