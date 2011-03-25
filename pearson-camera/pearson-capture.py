import pygame
import pygame.camera
import capture
import numpy
from pygame.locals import *

# Initialize screen:
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('MC920')

# Initialize camera:
pygame.camera.init()
webcam = capture.Capture()

# Event loop:
calibration = True
clock = pygame.time.Clock()
while True:
    clock.tick(60)

    # Handle events:
    pygame.event.pump()
    keystate = pygame.key.get_pressed()
    if keystate[K_ESCAPE] or pygame.event.peek(QUIT):
        break
    if calibration and keystate[K_UP]:
        calibration = 0

        # Store base image:
        x = pygame.surfarray.array3d(cam)
        x = numpy.dot(x, (0.30, 0.59, 0.11))
        xm = numpy.mean(x)
        diff_x = x - xm
        diff_x2 = diff_x ** 2
        denominator_x = numpy.sqrt(diff_x2.sum())

    # Capture images:
    if calibration:
        cam = webcam.get_cam()
    else:
        # Get new image:
        cam = webcam.get_cam()
        y = pygame.surfarray.array3d(cam)
        y = numpy.dot(y, (0.30, 0.59, 0.11))
        ym = numpy.mean(y)
        
        # Calculate r:
        diff_y = y - ym
        nominator = diff_x * diff_y
        nominator = nominator.sum()
        diff_y = diff_y ** 2
        denominator_y = numpy.sqrt(diff_y.sum())
        r = nominator / (denominator_x * denominator_y)
        print r

    # Draw everything:
    screen.blit(cam, (0,0))
    pygame.display.flip()
