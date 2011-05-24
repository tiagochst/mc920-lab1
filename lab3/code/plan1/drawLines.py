#!/usr/local/bin/python
from numpy import*
import sys
import getopt
import fileinput

import Image
import ImageDraw

#Imagem em escala cinza
im = Image.new ( "L", (70,70), 0)
#im2 = Image.new ( "L", (70,70), 0)

#Vou desenhar sobre a imagem
draw = ImageDraw.Draw ( im )
#draw2 = ImageDraw.Draw ( im2 )

# Draw X1,X2,X3,...,X20,Y1,Y2,...,Y19 Plan1
for line in fileinput.input(['linePlan1.txt']):
    line = line.split()     

    draw.line([(float(line[0])-2279,float(line[1])-1428),(float(line[2])-2279,float(line[3])-1428)],fill="white")

#for line in fileinput.input(['linePlan2.txt']):
#    line = line.split()     
#    draw2.line([(float(line[0]),float(line[1])),(float(line[2]),float(line[3]))],fill="white")

#im=im.crop(im.getbbox())
im.save ( "1.jpg" )
#im=im.resize((1000,1000))
#im.save ( "1res.jpg" )

#im2=im2.crop(im2.getbbox())
#im2.save ( "2.jpg" )
#im2=im2.resize((500,500))
#im2.save ( "2res.jpg" )

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



# TODO:
# Corrigir mapeamento de x e y
# Normalizar velocidades e imprimir em duas imagem e juntar
# como normalizar
# como juntar duas imagens?

#Planilha 1
vmax=2018.4899845917
vmin=635.4123857996

# Para normalizar de 0 a 255
oldrange=2018.4899845917-635.4123857996

for i in range(len(v0)):
	v0[i]= int(255*(v0[i]-vmin)/oldrange)
for i in range(len(v5)):
	v5[i]= int(255*(v5[i]-vmin)/oldrange)



im4 = Image.new ( "L", (3000,3000), 0)

#Vou desenhar sobre a imagem
draw = ImageDraw.Draw ( im4 )

i=0
for line in fileinput.input(['linePlan1.txt']):
    line = line.split()
    x0=float(line[0])
    x1=float(line[2])
    y0=float(line[1])
    y1=float(line[3])

    draw.line((x0,y0,x1,y1),fill=v5[i])
    print v5[i]
    i=i+1

im4=im4.crop(im4.getbbox())
im4.save ( "v5x.jpg" )

