#! /usr/bin/python2
"""This is a module that returns the analytical velocity field once u_i(y) and 
    cos(l_i*z) are know. The variables might be renamed this is just a guide. 
"""
from math import cos, sin, hypot, pi
# Some hacks.
#H = raw_input("Enter the Hartmann number: ")
#A = raw_input("Specify the aspect ratio : ")

def velocity(ha_, asp_r, z_co):
    """ Evaluate the velocity at a point for some given Ha and aspect ratio.
    From the given value of Ha, aspect ratio and z compute the velocity at 
    that point. H represents the Hartmann number, a parameter for this design.
    y is defined in mode_ui() so not repeated. 
    """
    
    d_z = 1/asp_r                             #following muller
    vel_u = 0.0                                 #init
    i = 1
    y_co = 0.0
    u_i = mode_ui(ha_, asp_r, i, y_co)

    while u_i >= 1.0e-6:
        u_i = mode_ui(ha_, i, y_co)
        l_i = 0.5*i*pi/d_z
        vel_u += u_i
    
    return vel_u*cos(l_i*z_co)
    
def mode_ui(ha_, asp_r, i, y_co):
    """Compute an individual mode of the velocity field y function. 
    The term that is the y component of the fourier series sum 
    solution.
    """
    d_z = 1/asp_r
    l_i = 0.5*i*pi/d_z
    k_i = 4*sin(0.5*i*pi)/(i*pi)

    if (ha_*d_z)/(i*pi) >= 10:
        return 
    p_i1 = 0.5*(ha_**2-hypot(ha_, 2*l_i))
    p_i2 = 0.5*(ha_**2+hypot(ha_, 2*l_i))
    
    
    return 
    
