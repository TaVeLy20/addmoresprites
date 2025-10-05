import pygame
import random
import math

pygame.init()
pygame.mixer.init()

scrwid, scrhei = 800, 600

pygame.display.set_caption("Level Upped!")
icon = pygame.image.load("enemy.png")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((scrwid, scrhei))
background = pygame.image.load("background.png")

enemiesimg = []
enemiesx = []
enemiesy = []
enenmycount = 7

enemyimg = pygame.image.load("enemy.png")
enemyimg = pygame.transform.scale(enemyimg, (70, 70))


for i in range(enenmycount):
    enemiesimg.append(enemyimg)
    enemiesx.append(random.randint(0, scrwid - 70))
    enemiesy.append(random.randint(0, scrhei - 70))

playerimg = pygame.image.load("player.png")
playerx = 400
playery = 300
playerxchange = 0

scorevalue = 0
font = pygame.font.SysFont("Comic Sans", 32)
textx = 10
texty = 10

overfont = pygame.font.SysFont("timesnewroman", 64)

playerimg = pygame.transform.scale(playerimg, (60, 70))
background = pygame.transform.scale(background, (800, 600))

enenmiesalive = enenmycount

playerspeed = 1

bgmusic = "backgroundmusic.mp3"

def gameovertext():
    overtext = overfont.render("YOU WIN!", True, (155, 0, 0))
    screen.blit(overtext, (200, 250))

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemiesimg[i], (x, y))

def iscollosion(enemyx, enemyy, playerx, playery):
    distance = math.sqrt((enemyx - playerx) ** 2 + (enemyy - playery) ** 2)
    return distance < 60

playing = True

pygame.mixer.music.load(bgmusic)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)

enemydiesound = pygame.mixer.Sound("die.mp3")

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    if enenmiesalive > 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: playerx -= playerspeed
        if keys[pygame.K_RIGHT]: playerx += playerspeed
        if keys[pygame.K_UP]: playery -= playerspeed
        if keys[pygame.K_DOWN]: playery += playerspeed
    else:
        pygame.mixer.music.stop()

    screen.blit(background, (0, 0))
    player(playerx, playery)

    for i in range(enenmycount):
        enemy(int(enemiesx[i]), enemiesy[i],i)

        if iscollosion(enemiesx[i], enemiesy[i], playerx, playery):
            enemiesx[i] = 100000
            enemiesy[i] = 100000
            enenmiesalive -= 1
            enemydiesound.play()

    if enenmiesalive == 0:
        gameovertext()

    top = font.render(str(enenmycount - enenmiesalive), True, (255, 255, 255))
    screen.blit(top, (400, 40))


    pygame.display.flip()

pygame.quit()