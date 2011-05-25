#!/usr/local/bin/python
from numpy import*
import sys
import getopt
import fileinput
import math
import Image,ImageDraw


def readVel(v,name):
    i=0
    for line in fileinput.input([name+'Plan1.txt']):
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


def drawTree(v,name):

    im = Image.new ( "L", (69,69), 0)
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
                    ant=im.getpixel((aux2,aux))
                    new=(ant+v[i])/2
                    im.putpixel((aux2,aux),int(new))
            ax0=x0
    #sobrepondo com a media?
        else:
            for aux2 in range (y0,ay0):
                for aux in range (x1,x0):
                    ant=im.getpixel((aux,aux2))
                    new=(ant+v[i])/2
                    im.putpixel((aux,aux2),int(new))
            ay0=y0

        i=i+1

    im.save ( name +".png" )

def main():
    v = []
    v = readVel(v,"v0");
    v = normVel(v);   
    drawTree(v,"v0");

    v1 = []
    v1 = readVel(v1,"v55");
    v1 = normVel(v1);   
    drawTree(v1,"v55");

    v2 = []
    v2 = readVel(v2,"v90");
    v2 = normVel(v2);   
    drawTree(v2,"v90");



if __name__ == "__main__":
  main()
