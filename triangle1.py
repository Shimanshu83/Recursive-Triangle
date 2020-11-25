import pygame 
import math 
import time

def factTriangle(tuple1,tuple2,tuple3):
    if (tuple3[0]-tuple1[0] ) <=10 :
        return 1
    else:
        x1 = tuple1[0] 
        y1 = tuple1[1]
        x2 = tuple2[0]
        y2 = tuple2[1]
        x3 = tuple3[0]
        y3 = tuple3[1]
        point1 = (x1,y1)
        point2 = (x2,y2)
        point3 = (x3,y3)
        point12 = ((x1+x2)/2,(y1+y2)/2)
        point23 = ((x3+x2)/2,(y3+y2)/2)
        point13 = ((x1+x3)/2,(y1+y3)/2)
        
        pygame.display.update()
        
        time.sleep(0.1)
        factTriangle(point12,point2,point23)
        factTriangle(point1,point12,point13)
        factTriangle(point13,point23,point3)
        pygame.draw.polygon(screen, (250,34,23), [point12,point2,point23], 1)
        pygame.draw.polygon(screen, (250,34,23), [point1,point12,point13], 1)
        pygame.draw.polygon(screen, (250,34,23), [point13,point23,point3], 1)

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("traingle")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((51,0,123))
    x = 60
    pointlist_3 = [(160, 540), (400, 60), (640, 540)]
    pygame.draw.polygon(screen, (250,34,23), pointlist_3, 2)
    factTriangle((160, 540), (400, 60), (640, 540))
    




#om swami vivekananda mai ki si ka baap toa nhi hu na jai bhawani samjha ki nhi 