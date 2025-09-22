import pygame as pg
import numpy as np
import math
from matrice_functions import *

# Set camera angle to view the 3D object
class Camera:
    def __init__(self, render, vi_tri):
        self.render = render
        self.vi_tri = np.array([*vi_tri, 1.0])

        # - forward: the direction the camera is looking (along the Z-axis).
        # - up: which way is "up" for the camera (Y-axis).
        # - right: which way is "right" (X-axis).
        # - These help define the camera's orientation in 3D space
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])

        # - This is how wide the camera can see horizontally. π/3 radians ≈ 60 degrees.
        self.h_fov = math.pi / 3
        # - It's calculated based on the horizontal FOV and the screen's aspect ratio (height ÷ width).
        self.v_fov = self.h_fov * (render.height / render.width)

        # - near_plane: the closest distance the camera can see (0.1 units).
        # - far_plane: the farthest distance it can see (100 units).
        # - Anything outside this range won't be rendered.
        self.near_plane = 0.1
        self.far_plane = 100

    def dich_chuyen_matrix(self):
        x, y, z, w = self.vi_tri
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def xoay_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0,  0,  0,  1]
        ])

    # @ stand for matrix mutiplication
    def camera_matrix(self):
        return self.dich_chuyen_matrix() @ self.xoay_matrix()