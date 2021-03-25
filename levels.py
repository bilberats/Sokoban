import pygame as pg

def ecrfin(ecran,rectEcran):
    ecran.fill((255,255,255))
    police = pg.font.Font("ecrit.ttf",72)
    texte = police.render("Bravo !",True,(200, 0, 0))
    rectTexte = texte.get_rect()
    rectTexte.center = rectEcran.center
    ecran.blit(texte,rectTexte)
    pg.display.flip()


def bords(grille):
    for x in range(0,10):
        grille[x][0] = 1
    for x in range(0,20):
        grille[0][x] = 1
    for x in range(0,10):
        grille[x][19] = 1
    for x in range(0,20):
        grille[9][x] = 1

        
def reset(grille):
    for i in range(10):
        for x in range(20):
            grille[i][x] = 0
    return grille

def lvla(grille):
    grille = reset(grille)
    bords(grille)
    grille[8][13] = 1
    grille[3][12] = 1
    fin = [4,12]
    grille[fin[0]][fin[1]] = 2
    jcor = [1,1]
    
    re = [grille,fin,jcor]
    return re


def lvlb(grille):
    grille = reset(grille)

    bords(grille)
    grille[5][1] = 1
    for i in range(5):
        grille[i+1][4] = 1
    grille[7][3] = 1
    grille[6][7] = 1
    grille[3][8] = 1
    for i in range(4):
        grille[5][i+11] = 1
    grille[8][12] = 1
    for i in range(4):
        grille[i+4][14] = 1
    grille[1][15] = 1
    grille[1][18] = 1
    grille[2][18] = 1
    grille[4][18] = 1
    for i in range(3):
        grille[6][i+16] = 1
    
    
    fin = [5,18]
    grille[fin[0]][fin[1]] = 2
    jcor = [1,2]

    re = [grille,fin,jcor]
    return re
