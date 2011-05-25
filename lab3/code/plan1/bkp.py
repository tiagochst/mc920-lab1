#!/usr/local/bin/python
from numpy import*
import sys
import getopt
import fileinput
import math
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

    x0=float(line[0])-2279
    x1=float(line[2])-2279
    y0=float(line[1])-1428
    y1=float(line[3])-1428

    draw.line((x0,y0,x1,y1),fill="white")

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

v90=[]
i=0
for line in fileinput.input(['v90Plan1.txt']):
    if(i%2==0):
        line = line.split()     
        v90.append(float(line[0])) # pega valocidade
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
for i in range(len(v90)):
	v90[i]= int(255*(v90[i]-vmin)/oldrange)



im4 = Image.new ( "L", (69,69), 0)

#Vou desenhar sobre a imagem
draw = ImageDraw.Draw ( im4 )

ax0 = ax1 = ay0 =ay1 = 0
i=0
for line in fileinput.input(['linePlan1.txt']):
    line = line.split()
    x0=int(line[0])-2270
    x1=int(line[2])-2270
    y0=int(line[1])-1421
    y1=int(line[3])-1421

    if(x0==x1):
        for aux2 in range (ax0,x0):
            for aux in range (y1,y0):
                print("AUX="+str(aux))
                ant=im4.getpixel((aux2,aux))
                new=(ant+v90[i])/2
                im4.putpixel((aux2,aux),int(new))
        ax0=x0
    #sobrepondo com a media?
    if(y1==y0):
        for aux2 in range (y0,ay0):
            for aux in range (x1,x0):
                ant=im4.getpixel((aux,aux2))
                new=(ant+v90[i])/2
                im4.putpixel((aux,aux2),int(new))
        ay0=y0

    #draw.line((x0,y0,x1,y1),fill=255)
    #print v90[i]
    i=i+1

im4.save ( "v90x.jpg" )

def readVel(v):
    i=0
    for line in fileinput.input(['v0Plan1.txt']):
        if(i%2==0):
            line = line.split()     
            v.append(float(line[0])) # pega valocidade
        i=i+1
    return v

def normVel(v):
    #Dados da Planilha 1
    vmax=2018.4899845917
    vmin=635.4123857996
    
    # Para normalizar de 0 a 255
    oldrange=vmax-vmin

    for i in range(len(v)):
	v[i]= int(255*(v[i]-vmin)/oldrange)
    return v


def drawTree(n,f):

    im4 = Image.new ( "L", (69,69), 0)
    ax0 = ay0  = 0
    i=0
    for line in fileinput.input(['linePlan1.txt']):
        line = line.split()
        x0=int(line[0])-2270
        x1=int(line[2])-2270
        y0=int(line[1])-1421
        y1=int(line[3])-1421

        if(x0==x1):
            for aux2 in range (ax0,x0):
                for aux in range (y1,y0):
                    ant=im4.getpixel((aux2,aux))
                    new=(ant+v90[i])/2
                    im4.putpixel((aux2,aux),int(new))
            ax0=x0
    #sobrepondo com a media?
        if(y1==y0):
            for aux2 in range (y0,ay0):
                for aux in range (x1,x0):
                    ant=im4.getpixel((aux,aux2))
                    new=(ant+v90[i])/2
                    im4.putpixel((aux,aux2),int(new))
            ay0=y0

            i=i+1

    im4.save ( "v90x.jpg" )



def main():


if __name__ == "__main__":
  main()
