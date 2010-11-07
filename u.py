#! /usr/bin/python2
"""This is a module that returns the analytical velocity.
Once u_i(y) and cos(l_i*z) are know. The variables might be renamed 
this is just a guide. 
m&b refers to text.
"""

from math import fabs, cos, sin, cosh, sinh, hypot, pi
TOL_MIN = 1e-6
#TOL_MAX = 1e6

def velocity(h, a, y, z):
    """Return final velocity at some point in domain.
    From the fourier modes of y and z contributions.
    """
    i = 1
    u = 0.0
    
    #uiy = u_y(h, a, i, y)
    #uiz = u_z(a, z, i)

    while 1: 
        uiy = u_y(h, a, y, i)
        uiz = u_z(a, z, i)

        if fabs(uiy*uiz) <= TOL:
            break
        u += uiy*uiz
        print u, i
        i += 2
        
        
    return u

def u_z(a, z, i):
    """The z contribution to velocity from formulae in m&b
    Oneliner form is better. Lambda form is complicated to use?
    """
    temp = cos(0.5*i*pi*a*z)
    #p = "u(z) is ", temp, "\n"
    #print(p)
    return temp

def f(y, p1, p2):
    """intermediary function for u_y computation
    """
    temp = sinh(p1)*cosh(p2*y)-sinh(p2)*cosh(p1*y)
    print temp
    return temp

def u_y(h, a, y, i):
    """The y contribution of velocity, from formula.
    Most work goes in here.
    """
    l = 0.5*i*pi*a
    k = -2*a*sin(l/a)/l  
    pi1 = 0.5*(h - hypot(h, 2*l))
    pi2 = 0.5*(h + hypot(h, 2*l))
    
    return (k/l**2)*(1-(f(y, pi1, pi2)/f(1.0, pi1, pi2)))
