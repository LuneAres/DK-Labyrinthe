from classes import *

pygame.init()
pygame.font.init()
FPSCLOCK=pygame.time.Clock()

menu = redimension(load(menu), fenX,fenY)
fond = redimension(load(fond), fenX,fenY)
mur = redimension(load(mur), cote_case,cote_case)
depart = redimension(load(depart), cote_case,cote_case)
arrivee = redimension(load(arrivee), cote_case,cote_case)

fen = pygame.display.set_mode((fenX, fenY))
pygame.display.set_caption(titre)

qui = 0
skins = set_skins(qui)

pygame.key.set_repeat(75, 75)

maze = maze()
perso = perso(skins)
i_menu = True
while True:
    
    if i_menu:
        fen.blit(menu, (0,0))
        fen.blit(redimension(perso.skin, cote_case*2,cote_case*2), (fenX/2-cote_case,fenY/2-cote_case))
    else:
        fen.blit(fond, (0,0))
        
        for y,ligne in enumerate(maze.maze):
            for x,case in enumerate(ligne):
                if case == '#':
                    fen.blit(mur, (x*cote_case,y*cote_case))
                    
        fen.blit(depart, (0,0))
        fen.blit(arrivee, (fenX-cote_case,fenY-cote_case))
        fen.blit(perso.skin, (perso.x*cote_case,perso.y*cote_case))
    
    for event in pygame.event.get():
        test_fin(event)
        
        if test_touche(event,K_SPACE):
            perso.make(skins)
            maze.make()
            i_menu = False
        
        if test_touche(event,K_ESCAPE):
            perso.make(skins)

        if event.type == KEYDOWN:
            if i_menu:
                if test_touche(event,K_RIGHT):
                    qui +=1
                elif test_touche(event,K_LEFT):
                    qui -=1
                skins = set_skins(qui)
                perso.make(skins)
            else:
                perso.move(event.key,maze.maze)
    
    if perso.x == largeur*2-2 and perso.y == hauteur*2-2:
        i_menu = True
    
    pygame.display.flip()
