from fonctions import *
from constantes import *

class maze:
    def __init__(self):
        self.make()
        
    def make(self):
        random_ways = lambda: sample((N, S, E, W), 4)
        maze = [[0] * largeur for _ in range(hauteur)]
        walls = [(0, 0, d) for d in random_ways()]
        
        while walls:
            cx, cy, way = walls.pop()
            nx, ny = MOVE[way](cx, cy)
            if 0 <= ny < hauteur and 0 <= nx < largeur and maze[ny][nx] == 0:
                maze[cy][cx] |= way
                maze[ny][nx] |= OPPOSITE[way]
                walls += [(nx, ny, d) for d in random_ways()]
        
        maze2 = []
        for y, row in enumerate(maze):
            line1 = []
            line2 = []
            for x, cell in enumerate(row):
                
                line1.append(' ')
                if cell & E: line1.append(' ')
                else: line1.append('#')
                
                if cell & S: line2.append(' ')
                else: line2.append('#')
                line2.append('#')
            
            maze2.append(line1[:-1])
            maze2.append(line2[:-1])

        self.maze = maze2[:-1]

class perso:
    def __init__(self,skins):
        self.make(skins)
    
    def make(self,skins):
        skins2 = {}
        for direction,skin in skins.items():
            skins2[direction] = redimension(load(skin), cote_case,cote_case)
        
        self.skins = skins2
        
        self.x = 0
        self.y = 0
        self.skin = self.skins[S]
    
    def move(self,touche,maze):
        if touche in param.keys():
            nx,ny = MOVE[param[touche]](self.x,self.y)
            if 0 <= nx < largeur*2-1 and 0 <= ny < hauteur*2-1:
                if maze[ny][nx] != '#':
                    self.x = nx
                    self.y = ny
                    
                    self.skin = self.skins[param[touche]]
