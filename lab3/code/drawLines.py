#!/usr/local/bin/python
from numpy import*
import sys
import getopt
import fileinput

import Image
import ImageDraw
import ImageFont

fontPath = "/usr/share/fonts/dejavu/DejaVuSerifCondensed-BoldItalic.ttf"
sans16 = ImageFont.truetype ( fontPath, 2 )

#Imagem em escala cinza
im = Image.new ( "L", (3000,3000), 0)
im2 = Image.new ( "L", (3000,3000), 0)
#im = Image.new ( "RGBA", (3000,3000), "#000")
#Vou desenhar sobre a imagem
draw = ImageDraw.Draw ( im )
draw2 = ImageDraw.Draw ( im2 )

# Draw X1,X2,X3,...,X20,Y1,Y2,...,Y19 Plan1
for line in fileinput.input(['linePlan1.txt']):
    line = line.split()     
    draw.line([(float(line[0]),float(line[1])),(float(line[2]),float(line[3]))],fill="white")
 #   draw.text ( (float(line[2]),float(line[3])), "x1")

for line in fileinput.input(['linePlan2.txt']):
    line = line.split()     
    draw2.line([(float(line[0]),float(line[1])),(float(line[2]),float(line[3]))],fill="white")

im=im.crop(im.getbbox())
im.save ( "1.jpg" )

im2=im2.crop(im2.getbbox())
im2.save ( "2.jpg" )
