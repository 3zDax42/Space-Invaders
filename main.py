import pygame # type: ignore
pygame.init()
pygame.display.set_caption("Space_Invaders!")
Game_Screen = pygame.display.set_mode((800,800))
Tick_Speed = pygame.time.Clock()
Time = 0
Playing_Game = True
enemy1 = pygame.image.load('Invader One.png').convert_alpha()
enemy2 = pygame.image.load('Invader Two.png').convert_alpha()
enemy3 = pygame.image.load('Invader Three.png').convert_alpha()
#------------------------------------------------------------------### Classes ###
class Alien:
    def __init__(self, X_Pos, Y_Pos):
        self.X_Pos = X_Pos
        self.Y_Pos = Y_Pos
        self.Living = True
        self.Direction = 1
        self.Frame_num = 0
        self.Width = 0
        self.Height = 0
    def Move(self, Time):
        if Time % 800 == 0:
            self.Y_Pos += 100
            self.Direction *= -1
            return 0
        if Time % 100==0:
            self.X_Pos += 50
        return Time
    def Draw(self):
        pass
class Large_Alien(Alien):
    def Draw(self, Time):
        self.Width = 38
        self.Height = 38
        Game_Screen.blit(enemy1, (self.X_Pos, self.Y_Pos), (self.Width*self.Frame_num, self.Height, self.Width, self.Height))
        if Time % 100 == 0:
            self.Frame_num += 1
class Mid_Alien(Alien):
    def Draw(self, Time):
        self.Width = 38
        self.Height = 30
        Game_Screen.blit(enemy2, (self.X_Pos, self.Y_Pos), (self.Width*self.Frame_num, self.Height, self.Width, self.Height))
        if Time % 100 == 0:
            self.Frame_num += 1
class Small_Alien(Alien):
    def Draw(self, Time):
        self.Width = 24
        self.Height = 24
        Game_Screen.blit(enemy2, (self.X_Pos, self.Y_Pos), (self.Width*self.Frame_num, self.Height, self.Width, self.Height))
        if Time % 100 == 0:
            self.Frame_num += 1
Armada = []
for i in range (2):
    Armada.append(Large_Alien(50, i*50+50))
class Bullet:
    def __init__(self, X_Pos, Y_Pos):
        self.X_Pos = X_Pos+28
        self.Y_Pos = Y_Pos-15
        self.Living = False
    def Move(self, X_Pos, Y_Pos):
        if self.Living == True:
            self.Y_Pos -= 5
            #print("Bullet True")
        if self.Y_Pos < 0:
            self.Living = False
        if self.Living == False:
            self.X_Pos = X_Pos+28
            self.Y_Pos = Y_Pos-15
    def Draw(self):
        pygame.draw.rect(Game_Screen, (250,250,250), (self.X_Pos, self.Y_Pos, 3, 10))

class Player:
    def __init__(self):
        self.X_Pos = 400
        self.Y_Pos = 750
        self.X_Vol = 0
        self.MoveLeft = False
        self.MoveRight = False
        self.Shoot = False
    def Input(self, Key1, Key2, Key3):
        if event.type == pygame.KEYDOWN:
            if event.key == Key1:
                self.MoveLeft = True
            elif event.key == Key2:
                self.MoveRight = True
            elif event.key == Key3:
                self.Shoot = True
        elif event.type == pygame.KEYUP:
            if event.key == Key1:
                self.MoveLeft = False
            elif event.key == Key2:
                self.MoveRight = False
            elif event.key == Key3:
                self.Shoot = False
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
bullet = Bullet(player.X_Pos, player.Y_Pos)
#--------------------------------------------------------------------################-------------------------------------------------------#
while Playing_Game:
    Tick_Speed.tick(60)
    Time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing_Game = False
        player.Input(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)
    for i in range (len(Armada)):
        Time = Armada[i].Move(Time)
    player.Physics()
    if player.Shoot == True:
        bullet.Living = True
    bullet.Move(player.X_Pos, player.Y_Pos)
#--------------------------------------------------------------------### Render Section ###
    Game_Screen.fill((0, 0, 0))
    if bullet.Living == True:
        bullet.Draw()
    for i in range (len(Armada)):
        Armada[i].Draw(Time)
    player.Draw()
    pygame.display.flip()

pygame.quit
