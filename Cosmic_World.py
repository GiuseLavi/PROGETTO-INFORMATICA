import os
import pygame
import random
from Cosmic_Entity import Entity
from pygame.locals import *

pygame.init()

class World:

	def __init__(self, finestra, numero_di_mostri, colore_mondo, colore_mondo_chiaro, colore_mondo_scuro):

		self.finestra = finestra
		self.numero_di_mostri = numero_di_mostri
		self.colore_mondo = colore_mondo
		self.colore_mondo_chiaro = colore_mondo_chiaro
		self.colore_mondo_scuro = colore_mondo_scuro



	def draw(self,presenza_castello, presenza_boss, sprite):

		display_width = 800
		display_height = 400
		clock = pygame.time.Clock()
		FPS = 30

		# Controllo colore alberi

		if self.colore_mondo == [50, 205, 50]:
			alberello = pygame.image.load('albero.png')
		elif self.colore_mondo == [0,0,255]:
			alberello = pygame.image.load('albero.blue.png')
		elif self.colore_mondo == [148, 0, 211]:
			alberello = pygame.image.load('albero.darkpurple.png')
		elif self.colore_mondo == [238, 130, 238]:
			alberello = pygame.image.load('albero.lightpurple.png')
		elif self.colore_mondo == [255, 140, 0]:
			alberello = pygame.image.load('albero.orange.png')
		elif self.colore_mondo == [255, 0, 0]:
			alberello = pygame.image.load('albero.red.png')
		elif self.colore_mondo == [192, 192, 192]:
			alberello = pygame.image.load('albero.white.png')
		elif self.colore_mondo == [255, 255, 0]:
			alberello_giallo = pygame.image.load('albero.yellow.png')
		elif self.colore_mondo == [128, 0, 0]:
			crea_entità(alberi_size, candelabro, alberi)

		# Controllo colore erba

		if self.colore_mondo == [50, 205, 50]:
			erba = pygame.image.load('erba.png')
		elif self.colore_mondo == [0,0,255]:
			erba_ = pygame.image.load('erba.blue.png')
		elif self.colore_mondo == [148, 0, 211]:
			erba = pygame.image.load('erba.darkpurple.png')
		elif self.colore_mondo == [238, 130, 238]:
			erba = pygame.image.load('erba.lightpurple.png')
		elif self.colore_mondo == [255, 140, 0]:
			erba = pygame.image.load('erba.orange.png')
		elif self.colore_mondo == [255, 0, 0]:
			erba = pygame.image.load('erba.red.png')
		elif self.colore_mondo == [192, 192, 192]:
			erba = pygame.image.load('erba.white.png')
		elif self.colore_mondo == [255, 255, 0]:
			erba = pygame.image.load('erba.yellow.png')
		elif self.colore_mondo == [128, 0, 0]:
			candelabro = pygame.image.load('candelabro.png')

		
		nemico = pygame.image.load('nemico.png')
		collezionabili = pygame.image.load('collezionabile.png')
		castello = pygame.image.load('castello.png')
		boss = pygame.image.load('boss.png')
		menu = pygame.image.load('Menù.png')
		

		main_x = 30
		main_y = 30


		player = Entity(main_x, main_y, self.finestra, 20 , sprite)
		oggetto_collezionabile = Entity(-220, -220, self.finestra, 20, collezionabili)
		albero = Entity(-120, -120, self.finestra, 20, alberello)
		erba = Entity(-110, -110, self.finestra, 20, erba)
		mostri = Entity(-100, -100, self.finestra, 20, nemico)

		if presenza_boss == 'Sì':
			boss = Entity(-130, -130, self.finestra, 20, boss)
			boss.coordinate_Entità(1, boss)
		if presenza_castello == 'Sì':
			castello = Entity(-140, -140, self.finestra, 20, castello)
			castello.coordinate_Entità(1, castello)



		stop = False

		# Liste di Coordinate

		coordinate = []
		boss = []
		castello = []
		alberi = []
		erba1 = []
		pixel = []
		pixel4 = []

		'''
		for i in range(pixel1):
			randX = round(random.randrange(0,display_width-block_size)/block_size)*block_size
			randY = round(random.randrange(0,display_height-block_size)/block_size)*block_size
			pixel2 = []
			pixel2.append(randX)
			pixel2.append(randY)
			pixel.append(pixel2)

		for i in range(pixel1):
			randX = round(random.randrange(0,display_width-block_size)/block_size)*block_size
			randY = round(random.randrange(0,display_height-block_size)/block_size)*block_size
			pixel3 = []
			pixel3.append(randX)
			pixel3.append(randY)
			pixel4.append(pixel3)
		'''
		# Numero di Oggetti

		numero_di_erba = 15
		numero_di_alberi = 5 
		pixel1 = 20
		
		self.finestra.fill(self.colore_mondo)


		main_x_change = 0
		main_y_change = 0
		block_velocity = 10
		block_size = 20
		pixel_size = 4

		mostri.coordinate_Entità(self.numero_di_mostri, coordinate)
		albero.coordinate_Entità(numero_di_alberi, alberi)
		erba.coordinate_Entità(numero_di_erba, erba1)
		randX = round(random.randrange(0,display_width-block_size)/block_size)*block_size
		randY = round(random.randrange(0,display_width-block_size)/block_size)*block_size

		for i in range(pixel1):
			randX_1 = round(random.randrange(0,display_width-block_size)/block_size)*block_size
			randY_1 = round(random.randrange(0,display_height-block_size)/block_size)*block_size
			pixel2 = []
			pixel2.append(randX_1)
			pixel2.append(randY_1)
			pixel.append(pixel2)

		for i in range(pixel1):
			randX_1 = round(random.randrange(0,display_width-block_size)/block_size)*block_size
			randY_1 = round(random.randrange(0,display_height-block_size)/block_size)*block_size
			pixel3 = []
			pixel3.append(randX_1)
			pixel3.append(randY_1)
			pixel4.append(pixel3)

		# Creazione Mondo di gioco
		while stop == False:

			# Gestione degli eventi
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()

				# Gestione del movimento
				'''
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						player.movimento(main_x, main_y, 'L')

					elif event.key == pygame.K_RIGHT:
						player.movimento(main_x, main_y, 'R')

					elif event.key == pygame.K_UP:
						player.movimento(main_x, main_y, 'U')

					elif event.key == pygame.K_DOWN:
						player.movimento(main_x, main_y, 'D')

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						player.movimento(main_x, main_y, 'a')
				'''
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						main_x_change = -block_velocity
						main_y_change = 0

					elif event.key == pygame.K_RIGHT:
						main_x_change = block_velocity
						main_y_change = 0

					elif event.key == pygame.K_UP:
						main_y_change = -block_velocity
						main_x_change = 0

					elif event.key == pygame.K_DOWN :
						main_y_change = block_velocity
						main_x_change = 0

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						main_x_change = 0
						main_y_change = 0


			if main_x <= 0 or main_x >= display_width or main_y <= 0 or main_y >= display_height:
				if main_x >= display_width and presenza_castello == 'No':
					print("Desideri continuare il percorso?")
					print()
					print("1) Sì")
					print("2) No")
					print()
					r = input("Selezionare la scelta desiderata : ")
					if r == "1":
						stop = True
					if r == "2":
						main_x_change = -block_velocity
						main_y_change = 0	

				elif main_x >= display_width and presenza_castello == 'Sì':
					main_x_change = -block_velocity
					main_y_change = 0	


			# Cambio di direzione

				elif main_x <= 0:
					main_x_change = block_velocity
					main_y_change = 0
				elif main_y <= 0:
					main_y_change = block_velocity
					main_x_change = 0
				elif main_y >= display_height:
					main_y_change = -block_velocity
					main_x_change = 0

			if self.colore_mondo != [128, 0, 0]:
				for XnY in pixel:
					pygame.draw.rect(self.finestra, self.colore_mondo_chiaro, (XnY[0], XnY[1], pixel_size, pixel_size))
				for XnY in pixel4:
					pygame.draw.rect(self.finestra, self.colore_mondo_scuro, (XnY[0], XnY[1], pixel_size, pixel_size))	


			player.crea_entità(20, [[main_x, main_y]])
			pygame.display.update()
			self.finestra.fill(self.colore_mondo)
			oggetto_collezionabile.crea_entità(20, [[randX, randY]])
			mostri.crea_entità(20, coordinate)
			albero.crea_entità(20, alberi)
			erba.crea_entità(20, erba1)
			clock.tick(FPS)

			player.collisioni(coordinate, 'N',main_x, main_y)
			player.collisioni([[randX, randY]], 'C', main_x, main_y)
			if presenza_castello == 'Sì':
				player.collisioni(castello, 'c', main_x, main_y)
			if presenza_boss == 'Sì':
				player.collisioni(boss, 'B', main_x, main_y)

			main_x += main_x_change
			main_y += main_y_change