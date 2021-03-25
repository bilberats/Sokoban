import pygame as pg
from levels import*
pg.init()



                    
class Joueur():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def mouvement(self,grille):
        for x in pg.event.get():
            if x.type == pg.KEYDOWN:
                if x.key == pg.K_LEFT:
                    while grille[self.y][self.x] != 1:
                        self.x -= 1
                    self.x += 1
                    
                if x.key == pg.K_RIGHT:
                    while grille[self.y][self.x] != 1:
                        self.x += 1
                    
                    self.x -= 1
                       
                if x.key == pg.K_DOWN:
                    while grille[self.y][self.x] != 1:
                        self.y += 1
                    self.y -= 1
                    
                if x.key == pg.K_UP:
                    while grille[self.y][self.x] != 1:
                        self.y -= 1
                    self.y += 1



def danslevl(ecran,joueur,grille):
    while grille [fin[0]][fin[1]] == 2:
        temps.tick(60)
        grille[joueur.y][joueur.x] = 0
        joueur.mouvement(grille)
        grille[joueur.y][joueur.x] = 3
        ecran.fill((0,0,0))
        
        for y in range(10):
            for x in range(20):
                if grille[y][x] == 1:
                    pg.draw.rect(ecran,(81, 81, 81),(x*64,y*64,64,64))
                elif grille[y][x] == 2:
                    pg.draw.rect(ecran,(0, 145, 0),(x*64,y*64,64,64))
                else:
                    pg.draw.rect(ecran,(255,255,255),(joueur.x*64,joueur.y*64,64,64))
        pg.display.flip()
        

if __name__ == "__main__":
    grille=[]
    for i in range(0,10):
        grille = grille + [[0]*20]
        
    temps = pg.time.Clock()
    ecran = pg.display.set_mode((20*64,10*64))
    rectEcran = ecran.get_rect()
    
    jcor = lvla(grille)[2]
    joueur = Joueur(jcor[0],jcor[1])
    grille = lvla(grille)[0]
    fin = lvla(grille)[1]
    
    danslevl(ecran,joueur,grille)#level while
    
    
    jcor = lvlb(grille)[2]
    joueur = Joueur(jcor[0],jcor[1])
    grille = lvlb(grille)[0]
    fin = lvlb(grille)[1]

    danslevl(ecran,joueur,grille)#level while

    ecrfin(ecran,rectEcran)
        



