from pygame.locals import *

hauteur = 10
largeur = 10
cote_case = 30

fenX = largeur * cote_case * 2 - cote_case
fenY = hauteur * cote_case * 2 - cote_case

FPS=30

titre = 'DK Labyrinthe'

menu = "images/menu.jpg"
fond = "images/fond.jpg"
mur = "images/mur.png"
depart = "images/depart.png"
arrivee = "images/arrivee.png"

N, S, E, W = 1, 2, 4, 8
OPPOSITE = {N: S, S: N, E: W, W: E}

MOVE = {N: lambda x, y: (x, y-1),
        S: lambda x, y: (x, y+1),
        E: lambda x, y: (x+1, y),
        W: lambda x, y: (x-1, y)}

persos = ["dk", "pacman"]

param = {K_UP: N,
         K_DOWN: S,
         K_RIGHT: E,
         K_LEFT: W}
