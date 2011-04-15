import pygame
from pygame.locals import *

class Capture(object):
    def __init__(self):
        self.size = (640,480)
        # Create a display surface:
        self.display = pygame.display.set_mode(self.size, 0)
        
        # Initialize the camera, if present:
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size, "RGB")
        self.cam.start()

        # Create a surface to capture to. For performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def get_cam(self):
	self.snapshot = self.cam.get_image(self.snapshot)
	return pygame.transform.flip(self.snapshot, True, False)

