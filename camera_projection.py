import math
import numpy as np

class Projection:
    def __init__(self, render):
        NEAR_VIEW = render.camera.near_plane
        FAR_VIEW = render.camera.far_plane
        RIGHT_VIEW = math.tan(render.camera.h_fov / 2)
        LEFT_VIEW = -RIGHT_VIEW
        TOP_VIEW = math.tan(render.camera.v_fov / 2)
        BOTTOM_VIEW = - TOP_VIEW

        m00 = 2/ (RIGHT_VIEW - LEFT_VIEW)
        m11 = 2 / (TOP_VIEW - BOTTOM_VIEW)
        m22 = (FAR_VIEW * NEAR_VIEW) / (FAR_VIEW - NEAR_VIEW)
        m32 = -2 * NEAR_VIEW * FAR_VIEW / (FAR_VIEW - NEAR_VIEW)
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        HW, HH = render.H_WIDTH, render.H_HEIGHT
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])

        