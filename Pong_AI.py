import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
import pygame

RED=(255,0,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
GREY = (66, 64, 64)
L_GREY = (139, 143, 140)

size = (700,500)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
done = False

pygame.init()

class Wall(pygame.sprite.Sprite):
	def __init__(self,x,y,width,height):
		super().__init__()

		self.image = pygame.Surface([width,height])
		self.image.fill(L_GREY)
		self.image.set_colorkey(L_GREY)
		self.rect = self.image.get_rect()

		pygame.draw.rect(self.image,BLACK,[0,0,width,height])

		self.rect.x = x
		self.rect.y = y
		self.y_change = 0
		self.score = 0

	def update(self):
		self.rect.y += self.y_change

class Ball(pygame.sprite.Sprite):
	def __init__(self,x,y,width,height):
		super().__init__()

		self.image = pygame.Surface([width,height])
		self.image.fill(L_GREY)
		self.rect = self.image.get_rect()

		pygame.draw.ellipse(self.image,GREY,[0,0,width,height])

		self.rect.x = x
		self.rect.y = y
		self.x_speed = 0
		self.y_speed = 0


	def update(self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed

def game_over(winner):
	screen.fill(L_GREY)
	text3 = win_font.render(str(winner) + " WINS!!",True,BLACK,L_GREY)
	screen.blit(text3, textRect3)

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.flip()
		clock.tick(15)

def move_player2():
	if player1.rect.y + 35 > ball.rect.center[1]:
		player1.rect.y += -1
	elif player1.rect.y + 35 <  ball.rect.center[1]:
		player1.rect.y += 1
	if player1.rect.y > 430:
		player1.rect.y = 430
	if player1.rect.y < 0:
		player1.rect.y = 0

player1 = Wall(20,size[1]/2-35,10,70)
player2 = Wall(670,size[1]/2-35,10,70)
l_wall = Wall(0,0,5,500)
r_wall = Wall(695,0,5,500)
t_wall = Wall(0,0,700,5)
b_wall = Wall(0,495,700,5)

ball = Ball(15,15,20,20)

ball.x_speed = 1
ball.y_speed = 1

player_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player_list.add(player1,player2,l_wall,r_wall,t_wall,b_wall)
all_sprites.add(player2,player1,ball,l_wall,r_wall,t_wall,b_wall)

score_font = pygame.font.Font("freesansbold.ttf",15)
win_font = pygame.font.SysFont("Calibri.ttf",40)
text1 = score_font.render("SCORE",True,BLACK,L_GREY)
text2 = score_font.render(str(player1.score) + " | " + str(player2.score),True,BLACK,L_GREY)
text3 = win_font.render("PLAYER1 WINS!!",True,BLACK,L_GREY)

textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect1.center = (size[0]/2,20)
textRect2.center = (size[0]/2,40)
textRect3.center = (size[0]/2,size[1]/2)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player2.y_change = -1
			elif event.key == pygame.K_DOWN:
				player2.y_change = 1

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				player2.y_change = 0

	screen.fill(L_GREY)

	player_hit = pygame.sprite.spritecollide(ball,player_list,False)

	if player1 in player_hit:
		player1.score += 1
		ball.x_speed = 1
	elif player2 in player_hit:
		player2.score += 1
		ball.x_speed = -1
	elif l_wall in player_hit:
		pause=True
		game_over("PLAYER2")
		done = True
	elif r_wall in player_hit:
		pause=True
		game_over("PLAYER1")
		done = True
	elif t_wall in player_hit:
		ball.y_speed = 1
	elif b_wall in player_hit:
		ball.y_speed = -1


	if player2.rect.top < 5:
		player2.rect.top = 5
	elif player2.rect.bottom > 495:
		player2.rect.bottom = 495

	if ball.x_speed == -1:
		move_player2()

	ball.update()
	player_list.update()

	text2 = score_font.render(str(player1.score) + " | " + str(player2.score),True,BLACK,L_GREY)
	screen.blit(text1,textRect1)
	screen.blit(text2,textRect2)

	all_sprites.draw(screen)

	pygame.display.update()
	clock.tick(200)

pygame.quit()








