import pygame
from random import randint
from pygame.locals import *


pygame.init()

largura = 640
altura = 480
x = int(largura/2)
y = int(altura/2)


x1 = randint (10, 300)
y1 = randint(10, 300)
dor = 0

fonte = pygame.font.SysFont('arial', 40, True, True)
listac=[]

compri=3
velo = 10
xr = velo
yr = 0

morreu = False



tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('cobra vegana')
temp = pygame.time.Clock()

def cobri(listac):
    for XeY in listac:
        ree_o = pygame.draw.rect(tela,(25,100,30), (XeY[0],XeY[1], 20,20))

def rei():
    global dor, compri,x,y,lista,listac,x1,x2,morreu
    dor = 0
    compri = 3
    x = int(largura/2)
    y = int(altura/2)
    lista=[]
    listac=[]
    x1 = randint (10, 300)
    y1 = randint(10, 300)
    morreu = False


while True:
    temp.tick(20)
    tela.fill((20,25,6))
    men = f'maca coletada: {dor} '
    tex = fonte.render(men, True, (255,255,255))
    te=tex.get_rect() 
    te.center = (400,40) 
    tela.blit(tex, te )
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if xr == velo:
                    pass
                else:
                    xr =  - velo
                    yr = 0
            if event.key == K_d:
                if xr == -velo:
                    pass
                else:
                    xr = velo
                    yr = 0
            if event.key == K_w:
                if yr == velo:
                    pass
                else:
                    yr = - velo
                    xr= 0
            if event.key == K_s:
                if yr == -velo:
                    pass
                else:
                    yr =  velo
                    xr = 0
    x = x + xr
    y = y + yr
    ree_o = pygame.draw.rect(tela,(25,100,30), (x,y, 20,20))
    tee_l = pygame.draw.rect(tela,(255,0,0), (x1,y1, 20,20))

    
    if ree_o.colliderect( tee_l ):
        x1 = randint (40, 600)
        y1 = randint(50, 430)
        dor = dor + 1 
        compri= compri + 1
        
    lista=[]
    lista.append(x)
    lista.append(y)
    listac.append(lista)
    if listac.count(lista) > 1:
        font = pygame.font.SysFont('arial', 30,True,True)
        mej='game over, aperte R para continuar'
        textt=font.render(mej,True,(255,255,255))
        text=textt.get_rect()
        morreu = True

    cobri(listac)

    if len(listac) > compri:
        del listac[0]

    while morreu:
        tela.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    rei()
        text.center = (largura/2, altura/2) 
        tela.blit(textt, text)
        pygame.display.update()
    
    if x > largura:
        x = 0
    if x < 0:
        x = largura
    if y > altura:
        y = 0
    if y < 0:
        y=altura

    #tela.blit(tex, (450,40))
    pygame.display.update()
