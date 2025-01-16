import pygame 
import random 
from random import randint
from sys import exit
screen=pygame.display.set_mode((800,450))

#function to monitor the score of the player
def ninja_score():
	ninja_point=pygame.time.get_ticks()//1000-score
	ninjap_surface=test_font.render(f'{ninja_point}',False,(64,60,60))
	ninja_p_rect=ninjap_surface.get_rect(center=(400,80))
	screen.blit(ninjap_surface,ninja_p_rect)
	return ninja_point

def obs_movent(obastical_rect):
	if obastical_rect:
		for i in obastical_rect:
			i.x-=4
			if i.bottom==375:
				screen.blit(snail,i)
			else:screen.blit(dragon,i)
		  
		obastical_rect=[x for x  in obastical_rect if x.x>-100]
		return obastical_rect
	else:return []

def collisions(player,obastical_list):
	for i in obastical_list:
		if i.collidepoint(player.center):
			return False
	else:
		return True

pygame.init()
clock=pygame.time.Clock()
game_on=True
score=0
score_value=0

test_font=pygame.font.Font(None,50)
sky=pygame.image.load("surace land.jpg")
ninja=pygame.image.load("ninja-removebg-preview (2).png").convert_alpha()
ninja_rec=ninja.get_rect(bottomleft=(70,370))

#obasticles

snail=pygame.image.load("snail-removebg-preview (1).png")

dragon=pygame.image.load("Dragon-red_-_Fantasy_Flying_Dragon__HD_Png_Download___Transparent_Png_Image_-_PNGitem-removebg-preview.png")
obastical_rect=[]


ninja_gravity=0
#intro of game while the game is in game off mode
ninja_stand=pygame.image.load("ninja_intro-removebg-preview.png").convert_alpha()
ninja_stand=pygame.transform.rotozoom(ninja_stand,0,2)
ninja_stand_rect=ninja_stand.get_rect(center=(400,225))
test_font1=pygame.font.Font(None,30)
text_font=test_font1.render("this game is on the beast mode ,play if you dare to change the world 'all alone'",None,(89,80,90))
text_font_rect=text_font.get_rect(bottomleft=(10,100))
game_name=test_font.render('Ninja_runner',None,(110,180,100))
game_rt=game_name.get_rect(center=(400,40))

#timer
obasticale_timer=pygame.USEREVENT + 1
pygame.time.set_timer(obasticale_timer,1500)
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
		if game_on:
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_SPACE :
					ninja_gravity=-20
		else:
			if event.type==pygame.KEYDOWN and  event.key==pygame.K_SPACE:
				
				score=pygame.time.get_ticks()//1000
				game_on=True
		if event.type==obasticale_timer and game_on:
			if randint(0,2):
				obastical_rect.append(snail.get_rect(bottomright=(randint(900,1200),375)))
			else:
				obastical_rect.append(dragon.get_rect(bottomright=(randint(900,1200),105)))
			
    #snail movement monitoring 
	if game_on:    
		screen.blit(sky,(0,00))
		ninja_score()
		obastical_rect=obs_movent(obastical_rect)

# ninja components
		ninja_gravity+=1
		ninja_rec.y +=ninja_gravity
		if ninja_rec.bottom>=370:ninja_rec.bottom=370
		ninja_rec.right+=2
		if ninja_rec.x>800:ninja_rec.x=-10
		screen.blit(ninja,ninja_rec)

		#after effect representation
		score_value=ninja_score()
		scr=test_font.render(f'SCORE: {score_value}',None,(50,90,112))
		score_vr=scr.get_rect(center=(200,200))

		game_on=collisions(ninja_rec,obastical_rect)
	
		#dragon area
		"""dragon_rect.right -=2
		if dragon_rect.x<-70:dragon_rect.x=790
		if dragon_rect.collidepoint(ninja_rec.center):
			game_on=False"""
       
		#snail rect parts
		"""snail_rect.right-=1
		if snail_rect.x<-30:snail_rect.x=790
		if snail_rect.collidepoint(ninja_rec.center):
			game_on=False"""
        
	else:
		screen.fill((94,129,162)) 
		screen.blit(ninja_stand,ninja_stand_rect)
		screen.blit(game_name,game_rt)
		obastical_rect.clear()
		if score_value==0:
				screen.blit(text_font,text_font_rect)
		else:
			screen.blit(scr,score_vr)



	pygame.display.update()
	clock.tick(60)
