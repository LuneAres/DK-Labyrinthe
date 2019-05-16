import pygame, sys
from pygame.locals import *
from random import sample
from constantes import *

def test_fin(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

def test_touche(event,touche):
    if event.type == KEYDOWN and event.key == touche:
        return True
    else:
        return False

def load(image):
    return pygame.image.load(image)

def redimension(image,x,y):
    return pygame.transform.scale(image,(x,y))

def set_skins(qui):
    return {N: "images/" + persos[qui % len(persos)] + "/haut.png",
            S: "images/" + persos[qui % len(persos)] + "/bas.png",
            E: "images/" + persos[qui % len(persos)] + "/droite.png",
            W: "images/" + persos[qui % len(persos)] + "/gauche.png",}
