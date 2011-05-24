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
im=im.resize((1000,1000))
im.save ( "1res.jpg" )

im2=im2.crop(im2.getbbox())
im2.save ( "2.jpg" )
im2=im2.resize((500,500))
im2.save ( "2res.jpg" )

# pegando as valocidades para linha da malha
v0=[]
i=0
for line in fileinput.input(['v0Plan1.txt']):
    if(i%2==0):
        line = line.split()     
        v0.append(float(line[0])) # pega valocidade
    i=i+1

v5=[]
i=0
for line in fileinput.input(['v5Plan1.txt']):
    if(i%2==0):
        line = line.split()     
        v5.append(float(line[0])) # pega valocidade
    i=i+1


v10=[]
i=0
for line in fileinput.input(['v10Plan1.txt']):
    if(i%2==0):
        line = line.split()     
        v10.append(float(line[0])) # pega valocidade
    i=i+1

for i in range(len(v0)):
    print v0[i]-v10[i]



im3 = Image.new ( "RGB", (3000,3000), 0)

#Vou desenhar sobre a imagem
draw = ImageDraw.Draw ( im3 )


# raio = (v0/v1)(sqrt(delta x^2 + delta y^2)-sqrt(delta x^2 + delta y^2))/ pi-2
# Draw X1,X2,X3,...,X20,Y1,Y2,...,Y19 Plan1
i=0
for line in fileinput.input(['linePlan1.txt']):
    line = line.split()
    x0=float(line[0])
    x1=float(line[2])
    y0=float(line[1])
    y1=float(line[3])
    dist = sqrt((math.pow(x0-x1,2))+(math.pow(y0-y1,2)))
    centerx=(x0+x1)/2
    centery=(y0+y1)/2

    # limiar que indica buraco
    if(v5[i]<1600):
        radius = ((v0[i]/v5[i])*(dist)-dist)/(math.pi-2)     
    else:
        radius =0
 #Linha com buraco do tamanho do raio

    # Caso 1: x nao altera raio no y 
    if(x0==x1):
        if(y0<y1):
            draw.line((x0,y0,x1,centery-radius),fill="green")
            draw.line((x0,centery+radius,x1,y1),fill="blue")
        else:
            draw.line((x0,y1,x1,centery-radius),fill="green")
            draw.line((x0,centery+radius,x1,y0),fill="blue")
    else:
        # caso em que x altara e y eh o mesmo
        if(x0<x1):
            draw.line((x0,y0,centerx-radius,y1),fill="pink")
            draw.line((centerx+radius,y0,x1,y1),fill="purple")
        else:
            draw.line((x1,y0,centerx-radius,y1),fill="pink")
            draw.line((centerx+radius,y0,x0,y1),fill="purple") 
    print i
    i=i+1
 #   draw.text ( (float(line[2]),float(line[3])), "x1")

im3=im3.crop(im3.getbbox())
im3=im3.resize((500,500))
im3.save ( "v5.jpg" )



im4 = Image.new ( "RGB", (3000,3000), 0)

#Vou desenhar sobre a imagem
draw = ImageDraw.Draw ( im4 )


# raio = (v0/v1)(sqrt(delta x^2 + delta y^2)-sqrt(delta x^2 + delta y^2))/ pi-2
# Draw X1,X2,X3,...,X20,Y1,Y2,...,Y19 Plan1
i=0
for line in fileinput.input(['linePlan1.txt']):
    line = line.split()
    x0=float(line[0])
    x1=float(line[2])
    y0=float(line[1])
    y1=float(line[3])
    dist = sqrt((math.pow(x0-x1,2))+(math.pow(y0-y1,2)))
    centerx=(x0+x1)/2
    centery=(y0+y1)/2

    # limiar que indica buraco
    if(v10[i]<1500):
        radius = ((v0[i]/v10[i])*(dist)-dist)/(math.pi-2)     
    else:
        radius =0

 #Linha com buraco do tamanho do raio

    # Caso 1: x nao altera raio no y 
    if(x0==x1):
        if(y0<y1):
            draw.line((x0,y0,x1,centery-radius),fill="green")
            draw.line((x0,centery+radius,x1,y1),fill="blue")
        else:
            draw.line((x0,y1,x1,centery-radius),fill="green")
            draw.line((x0,centery+radius,x1,y0),fill="blue")
    else:
        # caso em que x altara e y eh o mesmo
        if(x0<x1):
            draw.line((x0,y0,centerx-radius,y1),fill="pink")
            draw.line((centerx+radius,y0,x1,y1),fill="purple")
        else:
            draw.line((x1,y0,centerx-radius,y1),fill="pink")
            draw.line((centerx+radius,y0,x0,y1),fill="purple") 
    print i
    i=i+1
 #   draw.text ( (float(line[2]),float(line[3])), "x1")

im4=im4.crop(im4.getbbox())
im4=im4.resize((500,500))
im4.save ( "v10.jpg" )
