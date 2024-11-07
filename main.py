import pygame
pygame.init()

screen = pygame.display.set_mode((864,700))
bg = pygame.image.load("lesson 7/images/bg.png")
grass = pygame.image.load("lesson 7/images/ground.png")
flappy1 = pygame.image.load("lesson 7/images/flappy1.png")
flappy2 = pygame.image.load("lesson 7/images/flappy2.png")
flappy3 = pygame.image.load("lesson 7/images/flappy3.png")

flying = False
game_over = False
grass_x = 0

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [flappy1,flappy2,flappy3]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
        self.velocity = 0
        self.click = False
    def update(self):
        if flying == True:
            self.velocity += 0.1
            if self.velocity > 5:
                self.velocity = 5
            if self.rect.bottom < 660:
                self.rect.y += self.velocity
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.velocity = -3
            if pygame.mouse.get_pressed()[1] == 0:
                self.click = False 
            self.counter += 1
            if self.counter >= 5:
                self.counter = 0
                self.index += 1
                if self.index >= 3:
                    self.index = 0
            self.image = self.images[self.index]

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("lesson 7/images/tube.png")
        self.rect = self.image.get_rect()
        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = x,y-75
        if pos == -1:
            self.rect.topleft = x,y+75
    def update(self):
        self.rect.x -= 5
        if self.rect.x <0:
            self.kill()
flappy = Bird(100,300)
Flappy1 = pygame.sprite.Group()
Pipes = pygame.sprite.Group()
Flappy1.add(flappy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    screen.fill("black")
    screen.blit(bg,(0,0))
    screen.blit(grass,(grass_x,600))
    if game_over == False and flying == True:
        grass_x -= 0.3
        if abs(grass_x) >30:
            grass_x = 0
    Flappy1.draw(screen)
    Flappy1.update()
    pygame.display.update()