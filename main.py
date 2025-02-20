import pygame # type: ignore
pygame.init()
pygame.display.set_caption("Space_Invaders!")
Game_Screen = pygame.display.set_mode((800,800))
Tick_Speed = pygame.time.Clock()
Playing_Game = True
#------------------------------------------------------------------### Classes ###
class Player:
    def __init__(self):
        self.X_Pos = 400
        self.Y_Pos = 750
        self.X_Vol = 0
        self.MoveLeft = False
        self.MoveRight = False
    def Input(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.MoveLeft = True
            elif event.key == pygame.K_RIGHT:
                self.MoveRight = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.MoveLeft = False
            elif event.key == pygame.K_RIGHT:
                self.MoveRight = False
    def Physics(self):
        if self.MoveLeft:
            self.X_Vol = -3
        elif self.MoveRight:
            self.X_Vol = 3
        else:
            self.X_Vol = 0
        self.X_Pos += self.X_Vol
    def Draw(self):
        pygame.draw.rect(Game_Screen, (200, 200, 100), (self.X_Pos, 750, 60, 20))
        pygame.draw.rect(Game_Screen, (200, 200, 100), (self.X_Pos+6, 745, 48, 25))
        pygame.draw.rect(Game_Screen, (200, 200, 100), (self.X_Pos+24, 740, 12, 30))
        pygame.draw.rect(Game_Screen, (200, 200, 100), (self.X_Pos+27, 735, 6, 35))
#--------------------------------------------------------------------#
player = Player()
#--------------------------------------------------------------------#
while Playing_Game:
    Tick_Speed.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing_Game = False
        player.Input()
    player.Physics()
#--------------------------------------------------------------------### Render Section ###
    Game_Screen.fill((0, 0, 0))
    player.Draw()
    pygame.display.flip()

pygame.quit
