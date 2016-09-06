import pygame
import random

ANCHO = 1200
ALTO = 800

#Colores
BLANCO = (255,255,255)
NEGRO = (0,0,0)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL=(0,0,255)
origen=[200,200]

def Puntos(n):#dibuja puntos en la pantalla
    l=[]
    for i in range(n):
        x=random.randrange(200)
        y=random.randrange(200)
        l.append([x,y])
    return l

def traspuntos(n,p,origen):
        t=[]
        for i in range(n):
            xi=p[i][0]+origen[0]
            yi=p[i][1]+origen[1]
            t.append([xi,yi])
        return t


if __name__=="__main__":
    pygame.init()#inicializar
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    pptos = Puntos(5)
    for p in pptos:
        pantalla.set_at(p,AZUL)
        pygame.draw.circle(pantalla,VERDE,p,10,1)#dibuja una circunsferencia cuyo entero sea cada punto


    pantalla.set_at(origen,BLANCO)
    pygame.draw.circle(pantalla,BLANCO,origen,10,1)


    pptras = traspuntos(5,pptos,origen)
    for t in pptras:
        pantalla.set_at(t,ROJO)
        pygame.draw.circle(pantalla,ROJO,t,10,1)


pygame.display.flip()

fin=False

while not fin:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            fin=true
