import pygame as pygame
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

        self.height_width, self.height_height = self.width // 2, self.height // 2
        self.fps = 60 # frame per second is 60 - i can understand this
        self.clock = pygame.time.Clock()

    def draw(self):
        # fill the screen with lightblue

        self.screen.fill(pygame.Color('lightblue'))

    def run(self):
        # self.draw() → paints the screen lightblue
        #if an even is close (x) then close the app (check the close window button)
        # display.flip() to show the changes on window fps (flips to new changes)
        # only tick around 60 fps so it doesnt run too fast

        while True:
            self.draw()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip()
            self.clock.tick(self.fps)
    
if __name__ == '__main__':
    app = SoftwareRender()
    app.run()
    