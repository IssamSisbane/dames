import pygame
from pygame.locals import *
from tkinter import *
import os

def interface():
    fenetre=Tk() #definit la fenêtre principale
    fenetre.geometry("160x100") #definit la taille de la fenêtre
    txt1=Label(fenetre, text='Bienvenue\n Lancer une partie de Dames?')
    txt1.pack()
    Bouton = Button(fenetre, text ='Oui !', command =fenetre.destroy)
    Bouton.pack()
    fenetre.mainloop()

def casecliquée(point):
    case=[0,0]
    case[0]=int((point[0]-5)/50)
    case[1]=int((point[1]-8)/50)
    return case

def detectionfin(plateau):
    fin=0
    for i in range(10):
        for j in range(10):
            if plateau[i][j]!=0:
                fin=1
    return fin

def deplactsimple(colonnedepart,lignedepart,colonnearrivee,lignearrivee,sens,plateau):
    if lignedepart==lignearrivee-sens and colonnearrivee==colonnedepart and plateau[colonnearrivee][lignearrivee]==0:
        return 1
    else:
        return 0


def depactprisepion(colonnedepart,lignedepart,colonnearrivee,lignearrivee,plateau,pion,sens):
    depvalide=0
    if lignedepart==lignearrivee and colonnearrivee-colonnedepart==-2 and plateau[colonnedepart-1][lignearrivee]!=0 and plateau[colonnedepart-1][lignearrivee]!=pion:
            depvalide=1
    if lignedepart-lignearrivee==-2 and colonnearrivee==colonnedepart and plateau[colonnedepart][lignearrivee-1]!=0 and plateau[colonnedepart][lignearrivee-1]!=pion:
            depvalide=1
    if lignedepart==lignearrivee and colonnearrivee-colonnedepart==2 and plateau[colonnedepart+1][lignearrivee]!=0 and plateau[colonnedepart+1][lignearrivee]!=pion:
            depvalide=1
    if lignedepart-lignearrivee==+2 and colonnearrivee==colonnedepart and plateau[colonnedepart][lignearrivee+1]!=0 and plateau[colonnedepart][lignearrivee+1]!=pion:
            depvalide=1
    return(depvalide)

def depactprisepiondiag(colonnedepart,lignedepart,colonnearrivee,lignearrivee,plateau,pion,sens):
    depvalide=0
    if lignedepart-lignearrivee==-2 and colonnearrivee-colonnedepart==-2 and plateau[colonnedepart-1][lignearrivee-1]!=0 and plateau[colonnedepart-1][lignearrivee-1]!=pion:
            depvalide=1
    if lignedepart-lignearrivee==+2 and colonnearrivee-colonnedepart==-2 and plateau[colonnedepart-1][lignearrivee+1]!=0 and plateau[colonnedepart-1][lignearrivee+1]!=pion:
            depvalide=1
    if lignedepart-lignearrivee==+2 and colonnearrivee-colonnedepart==+2 and plateau[colonnedepart+1][lignearrivee+1]!=0 and plateau[colonnedepart+1][lignearrivee+1]!=pion:
            depvalide=1
    if lignedepart-lignearrivee==-2 and colonnearrivee-colonnedepart==+2 and plateau[colonnedepart+1][lignearrivee-1]!=0 and plateau[colonnedepart+2][lignearrivee-1]!=pion:
            depvalide=1
    return(depvalide)

pygame.init()
#Création du plateau de jeu
plateau=[[0 for i in range(10)]for j in range(10)]
#On met les pions blancs dans le tableau
for i in range(2):
    for j in range(5):
        plateau[2*j][2*i]=1
        plateau[2*j+1][2*i+1]=1
#On met les pions noirs dans le tableau
for i in range(2):
    for j in range(5):
        plateau[2*j][9-2*i]=2
        plateau[2*j+1][8-2*i]=2
print(plateau)


#Ouverture de la fenÃƒÂªtre Pygame
fenetre = pygame.display.set_mode((500, 600),RESIZABLE)

#Chargement et collage du fond
fond = pygame.image.load(os.path.dirname( __file__ )+"\\damier.gif")
fenetre.blit(fond, (0,0))
bandeau=pygame.image.load(os.path.dirname( __file__ )+"\\bandeau.gif")
fenetre.blit(bandeau,(0,500))

#Placement des pions dans le damier
pion_blanc=pygame.image.load(os.path.dirname( __file__ )+"\\pionblanc.gif")
pion_blanc.set_colorkey((255,255,255))

dame_noire=pygame.image.load(os.path.dirname( __file__ )+"\\damenoir.gif")
dame_noire.set_colorkey((255,255,255))

dame_blanc=pygame.image.load(os.path.dirname( __file__ )+"\\dameblanc.gif")
dame_blanc.set_colorkey((255,255,255))

pion_noir=pygame.image.load(os.path.dirname( __file__ )+"\\pionnoir.gif")
pion_noir.set_colorkey((255,255,255))
for j in range(10):
    for i in range(10):
        if plateau[j][i]==1:
            fenetre.blit(pion_blanc,(j*50+5,i*50+8))
        elif plateau[j][i]==2:
            fenetre.blit(pion_noir,(j*50+5,i*50+8))



pygame.display.flip() #rafraichit la fenêtre

interface()
#BOUCLE INFINIE
continuer = 1
joueur=1
while continuer==1:
    casedepart=[0,0]
    joueur=(joueur+1)%2
    if joueur==0:
        pion=1
        sens=1
        pionjoueur=pion_blanc
    else:
        pion=2
        sens=-1
        pionjoueur=pion_noir
    print(joueur,pion)
    fenetre.blit(fond,(0,0))
    fenetre.blit(bandeau,(0,500))
    fenetre.blit(pionjoueur,(200,520))
    for i in range(10):
        for j in range(10):
            if plateau[i][j]==1:
                fenetre.blit(pion_blanc,(i*50+5,j*50+8))
            elif plateau[i][j]==2:
                fenetre.blit(pion_noir,(i*50+5,j*50+8))
    pygame.display.flip()
    pion_choisi=0
    while pion_choisi==0:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and event.pos[1]<500:
                    colonne=casecliquée(event.pos)[0]
                    ligne=casecliquée(event.pos)[1]
                    if plateau[colonne][ligne]==pion:
                        pion_choisi=1
                        colonnecasedepart=colonne
                        lignecasedepart=ligne
                        print("pionchoisi",colonnecasedepart,lignecasedepart)
                        print(sens)
                        if event.button==3:
                                print("desélection")
                                pion_choisi=0


    pion_déplace=0
    while pion_déplace==0:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 :
                    colonne=casecliquée(event.pos)[0]
                    ligne=casecliquée(event.pos)[1]
                    print(colonne,ligne)
                    if deplactsimple(colonnecasedepart,lignecasedepart,colonne,ligne,sens,plateau)==1:
                        pion_déplace=1
                        plateau[colonnecasedepart][lignecasedepart]=0
                        plateau[colonne][ligne]=pion
                        print("piondeplace",colonne,ligne)
                    elif depactprisepion(colonnecasedepart,lignecasedepart,colonne,ligne,plateau,pion==1,joueur)==1:
                        pion_déplace=1
                        plateau[colonnecasedepart][lignecasedepart]=0
                        plateau[colonne][ligne]=pion
                        if colonnecasedepart==colonne and lignecasedepart>ligne :
                            plateau[colonne][ligne+1]=0
                        if colonnecasedepart==colonne and lignecasedepart<ligne :
                            plateau[colonne][ligne-1]=0
                        if colonnecasedepart>colonne and lignecasedepart==ligne :
                            plateau[colonne+1][ligne]=0
                        if colonnecasedepart<colonne and lignecasedepart==ligne :
                            plateau[colonne-1][ligne]=0
                    elif depactprisepiondiag(colonnecasedepart,lignecasedepart,colonne,ligne,plateau,pion==1,joueur)==1:
                        pion_déplace=1
                        plateau[colonnecasedepart][lignecasedepart]=0
                        plateau[colonne][ligne]=pion
                        if colonnecasedepart>colonne and lignecasedepart>ligne :
                            plateau[colonne+1][ligne+1]=0
                            plateau[colonne+2][ligne+2]=0
                        if colonnecasedepart>colonne and lignecasedepart<ligne :
                            plateau[colonne+1][ligne-1]=0
                            plateau[colonne+2][ligne-2]=0
                        if colonnecasedepart<colonne and lignecasedepart>ligne :
                            plateau[colonne-1][ligne+1]=0
                            plateau[colonne-2][ligne+2]=0
                        if colonnecasedepart<colonne and lignecasedepart<ligne :
                            plateau[colonne-1][ligne-1]=0
                            plateau[colonne-2][ligne-2]=0


                        print("piondeplace",colonne,ligne)

                    else:
                        print("pas bon")

                    plateau[colonne][ligne]=pion
                    if sens==1 and ligne==9 :
                            pion=dame_blanc
                            fenetre.blit(dame_blanc , ((event.pos)[0],(event.pos)[1]))
                    if sens==-1 and ligne==0:
                            pion=dame_noir
                            fenetre.blit(dame_noir , ((event.pos)[0],(event.pos)[1]))
            if event.type == pygame.QUIT:
                continuer = 0
                pion=dame_noire

pygame.quit()