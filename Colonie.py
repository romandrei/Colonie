import pygame, random
pygame.init()

frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("Colonie")

ceas = pygame.time.Clock()

pixel = 15

class colonieA(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((pixel, pixel))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.reproducere = 0
        self.reproducere_max = random.randrange(15, 60)
        self.varsta = 0
        self.moarte = random.randrange(50, 100)
        self.soarta = random.randrange(1, 5)
    def update(self):
        self.reproducere += 1
        self.varsta += 1
        if self.reproducere > self.reproducere_max:
            colA = colonieA(self.rect.x, self.rect.y)
            toate.add(colA)
            colonA.add(colA)
            self.reproducere = 0
        elif self.varsta > self.moarte:
            self.kill()
        elif self.soarta == 1 and self.rect. x < 800:
            self.rect.x += pixel
            self.soarta = random.randrange(1, 5)
        elif self.soarta == 2 and self.rect.x > 0:
            self.rect.x -= pixel
            self.soarta = random.randrange(1, 5)
        elif self.soarta == 3 and self.rect.y < 800:
            self.rect.y += pixel
            self.soarta = random.randrange(1, 5)
        elif self.soarta == 4 and self.rect.y > 0:
            self.rect.y -= pixel
            self.soarta = random.randrange(1, 5)
        

class colonieB(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((pixel, pixel))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.reproducere = 0
        self.reproducere_max = random.randrange(15, 60)
        self.varsta = 0
        self.moarte = random.randrange(50, 100)
        self.soarta = random.randrange(1, 5)
    def update(self):
        self.reproducere += 1
        self.varsta += 1
        if self.reproducere > self.reproducere_max:
            colB = colonieB(self.rect.x, self.rect.y)
            toate.add(colB)
            colonB.add(colB)
            self.reproducere = 0
        elif self.varsta > self.moarte:
            self.kill()
        elif self.soarta == 1 and self.rect. x < 800:
            self.rect.x += pixel
            self.soarta = random.randrange(1, 5)
        elif self.soarta == 2 and self.rect.x > 0:
            self.rect.x -= pixel
            self.soarta = random.randrange(1, 5)
        elif self.soarta == 3and self.rect.y < 800:
            self.rect.y += pixel
            self.soarta = random.randrange(1, 5)
        elif self.soarta == 4 and self.rect.y > 0:
            self.rect.y -= pixel
            self.soarta = random.randrange(1, 5)

toate = pygame.sprite.Group()
colonA = pygame.sprite.Group()
colonB = pygame.sprite.Group()
colA = colonieA(200, 200)
toate.add(colA)
colonA.add(colA)
colB = colonieB(600, 600)
toate.add(colB)
colonB.add(colB)

rulare = True
while rulare:
    ceas.tick(30)
    frstr.fill((0, 255, 0))
    taste = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or taste[pygame.K_ESCAPE]:
            rulare = False
        elif taste[pygame.K_F4]:
            frstr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        elif taste[pygame.K_F3]:
            frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

    lovit = pygame.sprite.groupcollide(colonA, colonB, True, True)

    toate.update()
    toate.draw(frstr)
    pygame.display.flip()

pygame.quit()
