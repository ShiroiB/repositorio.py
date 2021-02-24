import pygame
from pygame.locals import *
import os
from random import randrange


pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal ,'python' )
LARGURA = 640
ALTURA = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Caneca Game')

sprite_sheet = pygame.image.load(os.path.join(diretorio_principal, 'garrafa_termica.png')).convert_alpha()

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for i in range(3):
            img = sprite_sheet.subsurface((i*32,0), (30,30))#((x,y->posicao da imagem, precisa saber o tamanho do "quadrado"), tamanho))
            img = pygame.transform.scale(img, (100, 100))
            self.imagens_dinossauro.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (100, ALTURA-64)
        self.pulo = False
        self.pot=ALTURA-64-96/2
    def pular (self):
        self.pulo = True


    def update(self):
        if self.pulo == True:
           self.rect.y -= 20
           if self.rect.y <=200:
               self.pulo = False
        else:
            if self.rect.y < self.pot:
                self.rect.y +=20 
            else:
                self.rect.y = self.pot
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.index_lista)]


class N(pygame.sprite.Sprite):
     def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         self.image =sprite_sheet.subsurface((4*24,0), (30, 30))
         self.image = pygame.transform.scale(self.image, (100, 100))
         self.rect = self.image.get_rect()
         #self.rect.center = (100,100)
         self.rect.y = randrange(50,200,50)
         self.rect.x = LARGURA - randrange(30,300,90)

     def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA 
            self.rect.y = randrange(50,200,50)
        self.rect.x -= 10

class Sei(pygame.sprite.Sprite):
     def __init__(self, posx):
          pygame.sprite.Sprite.__init__(self)
          self.image =sprite_sheet.subsurface((5*26,0), (32,32))
          self.image = pygame.transform.scale(self.image, (200, 64))
          self.rect = self.image.get_rect()
          self.rect.y = ALTURA - 64
          self.rect.x = posx * 64

     def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA 
        self.rect.x -= 10
class Cacto(pygame.sprite.Sprite):
     def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         self.image =sprite_sheet.subsurface((6*32,0), (30,30))
         self.image = pygame.transform.scale(self.image, (50, 85))
         self.rect = self.image.get_rect()
         self.mask = pygame.mask.from_surface(self.image)
         self.rect.center = (LARGURA, ALTURA-64)
     def update(self):
          if self.rect.topright[0] < 0:
            self.rect.x = LARGURA 
          self.rect.x -= 10


todas_as_sprites = pygame.sprite.Group()
dino = Dino()

todas_as_sprites.add(dino)



for i in range(3):
    nuvem = N()
    todas_as_sprites.add(nuvem)


for i in range(640*2//64):
    terra = Sei(i)
    todas_as_sprites.add(terra)


cacto = Cacto()
todas_as_sprites.add(cacto)

grup = pygame.sprite.Group()
grup .add(cacto)


relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if dino.rect.y != dino.pot:
                    pass
                else:
                    dino.pular()
    


    colisoes = pygame.sprite.spritecollide(dino,grup,False, pygame.sprite.collide_mask)
    todas_as_sprites.draw(tela)
    if colisoes:
        pass
    else:
        todas_as_sprites.update()

    pygame.display.flip()
