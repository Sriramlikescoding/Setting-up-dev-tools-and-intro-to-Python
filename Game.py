import math
import random
import pygame

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT= 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 10
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27
#Initialize Pygame
pygame.init()
#create_the_screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#Background
bacckground = pygame.image.load("background.png")
#Caption and Icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#Player
playerImg = pygame.image.load('ufo.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0
#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64)) #64 size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

#Bullet
bulletImg = pygame.image.load("bullet.png")
BULLET_X = 0
BULLET_Y = PLAYER_START_Y

BULLET_X_CHANGE = 0
BULLET_Y_CHANGE = BULLET_SPEED_Y
BULLET_STATE = "ready"

#Creating Score
SCORE_VALUE = 0
font = pygame.font.Font("freesansbold.ttf", 32)
TEXT_X = 10
TEXT_Y = 10

#Game over Text

game_over_font = pygame.font.Font("freesansbold.ttf", 64)

def showScore(X, Y):
    score = font.render("Score: " + str(SCORE_VALUE), True, (255,255,255))
    screen.blit(score, (X,Y))

def GameOverText():
    game_over_text = game_over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over_text, (200,250))

def Player(X, Y):
    screen.blit(playerImg, (X, Y))

def Enemy(X, Y, I):
    screen.blit(enemyImg[I], (X,Y))

def Fire_bullets(X,Y):
    global BULLET_STATE 
    BULLET_STATE = "fire"
    screen.blit(bulletImg, (X+16, Y+10))

#Check Collision between enemy and bullet
def isCollision(ENEMY_X, ENEMY_Y, BULLET_X, BULLET_Y):
    distance = math.sqrt((ENEMY_X-BULLET_X)**2+(ENEMY_Y - BULLET_Y)**2)
    return distance < COLLISION_DISTANCE

#Game Loop

running = True

while running:
    screen.fill((0,0,0))
    screen.blit(bacckground, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and BULLET_STATE == "ready":
                BULLET_X = playerX
                Fire_bullets(BULLET_X,BULLET_Y)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    playerX = playerX + playerX_change
    playerX = max(0,min(playerX, SCREEN_WIDTH-64))

    for i in range(num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            GameOverText()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH-64:
            enemyX_change[i]*=-1
            enemyY[i] += enemyY_change[i]
        if isCollision(enemyX[i], enemyY[i], BULLET_X, BULLET_Y):
            BULLET_Y = PLAYER_START_Y
            BULLET_STATE = 'ready'
            SCORE_VALUE += 1
            enemyX[i] = random.randint(0,SCREEN_WIDTH-64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        Enemy(enemyX[i], enemyY[i], i)

    #Bullet Movement
    if BULLET_Y <= 0:
        BULLET_Y = PLAYER_START_Y
        BULLET_STATE = 'ready'
    elif(BULLET_STATE == 'fire'):
        Fire_bullets(BULLET_X,BULLET_Y)
        BULLET_Y -= BULLET_Y_CHANGE
    Player(playerX,playerY)
    showScore(TEXT_X,TEXT_Y)
    pygame.display.update()
        

            