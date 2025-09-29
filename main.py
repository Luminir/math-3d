import pygame as pygame
from camera import *
from camera_projection import *
from threed_main import *

class SoftwareRender:
    def __init__(self):
        # pygame.init() → starts up pygame, like turning on the power.
        # self.resolution → window size (w 1600 px, h 900 px).
        # self.screen → SET window size when pop up
        # stored half the width, half the height (not used yet)
        # fps: frame perr seconds (update screen 60 times every sec)
        # clock wathc → stopwatch to control how fast the loop runs.

        pygame.init()
        self.resolution = self.width, self.height = 500, 400
        self.screen = pygame.display.set_mode(self.resolution)

        self.H_WIDTH, self.H_HEIGHT = self.width // 2, self.height // 2

        self.fps = 60 # frame per second is 60 - i can understand this
        self.clock = pygame.time.Clock()
        self.create_object()

    def draw(self):
        # fill the screen with lightblue
        self.screen.fill(pygame.Color('lightblue'))
        self.object.draw()

    def run(self):
        # self.draw() → paints the screen lightblue
        #if an even is close (x) then close the app (check the close window button)
        # display.flip() to show the changes on window fps (flips to new changes)
        # only tick around 60 fps so it doesnt run too fast

        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip()
            self.clock.tick(self.fps)
    
    def create_object(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object3D(self)
        # rotating around the y axis
        self.object.translate([0.2, 0.4, 0.2])
        self.object.rotate_y(math.pi/6)

if __name__ == '__main__':
    app = SoftwareRender()
    app.run()
    