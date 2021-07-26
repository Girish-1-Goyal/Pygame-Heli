import pygame
import os
import time
import math

pygame.init()

win = pygame.display.set_mode((1000,570))
pygame.display.set_caption('Helicopter shooting')

bg = pygame.image.load('bg.png')

wtrimg = pygame.image.load('w2.jpg')

hcimg = pygame.image.load('helicopter.png')
x1 = 500
y1 = 20
x_change = -2
y_change = 0

btimg = pygame.image.load('boat.png')
x2 = 850
y2 = 370
xb_change = 6

msimg = pygame.image.load('missile.png')
x3 = 500
y3 = 70
msy_change = 8
ms_state = "ready"

score_value = 0
font = pygame.font.SysFont('times new roman',32,'italic')
x4 = 500
y4 = 500

def score(x,y):
	msg = font.render("Score:-" + str(score_value) ,True,(255,255,0))
	win.blit(msg,(x,y))

def hc(x,y):
	win.blit(hcimg,(x,y))

def boat(x,y):
	win.blit(btimg,(x,y))

def msi(x,y):
	global ms_state
	win.blit(msimg,(x,y))
	ms_state = "fire"

def iscollision(x2,y2,x3,y3):
	d = math.sqrt((math.pow(x3-x2,2)) + (math.pow(y3-y2,2)))
	if d < 50:
		return True
	else:
		return False


run = True
while run:
	win.blit(bg,(0,0))
	win.blit(wtrimg,(0,430))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		x_change -= 3	
	if keys[pygame.K_RIGHT]:
		x_change += 1
	if keys[pygame.K_v]:
		x1 = 500
	if keys[pygame.K_SPACE]:
		if ms_state is "ready":
			x3 = x1
			msi(x3,y3)
       
	hc(x1,y1)
	x1 += x_change
	if x1 <= 0:
		x1 = 930
	elif x1 >= 930:
		x1 = 0

	x2 -= xb_change
	if x2 <= 0:
		x2 = 900
	elif x2 >= 900:
		x2 = 0
	boat(x2,y2)

	if y3 >= 560:
		y3 = 59
		ms_state = "ready"
	if ms_state is "fire":
		msi(x3,y3)
		y3 += msy_change

	collision = iscollision(x2,x3,y2,y3)
	if collision:
		y3 = 70
		ms_state = "ready"
		score_value +=1
		
	score(x4,y4)
	pygame.display.update()
pygame.quit()