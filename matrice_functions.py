import math
import numpy as np

# this r the math matrices for equations
# the next_position = current_position * formula_matrices

# formula to move the 3d object
def dich_chuyen(toa_do):

# formula to roate the 3d object around x axis
    x, y, z = toa_do
    return np.array([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [x,y,z,1]
    ])

def rotate_x(a):
    return np.array([
        [1,0,0,0],
        [0, math.cos(a), -math.sin(a), 0],
        [0, math.sin(a), math.cos(a), 0],
        [0,0,0,1]
    ])

def rotate_y(a):
    return np.array([
        [math.cos(a), 0, math.sin(a), 0],
        [0,1,0,0],
        [-math.sin(a), 0, math.cos(a), 0],
        [0,0,0,1]
    ])

def rotate_z(a):
    return np.array([
        [math.cos(a), -math.sin(a), 0,0],
        [math.sin(a), math.cos(a), 0 ,0],
        [0,0,1,0],
        [0,0,0,1]
    ])

def scale(n):
    return np.array([
        [n,0,0,0],
        [0,n,0,0],
        [0,0,n,0],
        [0,0,0,1]
    ])
