import os, sys
import numpy
import pygame

def load_image(name):
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    fullname = os.path.join(main_dir, name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))

    return image

def pearson_coefficient(image1, image2):
    x = pygame.surfarray.pixels3d(image1)
    y = pygame.surfarray.pixels3d(image2)

    # Conversion to gray scale:
    x = numpy.dot(x, (0.30, 0.59, 0.11))
    y = numpy.dot(y, (0.30, 0.59, 0.11))

    # Calculate (xi - xm):
    xm, ym = numpy.mean(x), numpy.mean(y)
    diff_x = x - xm
    diff_y = y - xm

    # SUM[ (xi - xm) * (yi - ym) ]:
    nominator = diff_x * diff_y
    nominator = nominator.sum()

    # SQRT[ SUM[ (xi - xm) ** 2 ] ]:
    diff_x = diff_x ** 2
    diff_y = diff_y ** 2
    denominator_x = numpy.sqrt(diff_x.sum())
    denominator_y = numpy.sqrt(diff_y.sum())

    return nominator / (denominator_x * denominator_y)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: python pearson.py image1 image2"
    else:
        image1 = load_image(sys.argv[1])
        image2 = load_image(sys.argv[2])
        print "r =", pearson_coefficient(image1, image2)
