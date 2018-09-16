import pygame
import os
import random
import Cosmic_Entity
from pygame.locals import *

pygame.init()

class Entity:

	def __init__(self, main_x, main_y, finestra, block_size, sprite):

		self.main_x = main_x
		self.main_y = main_y
		self.sprite = sprite
		self.block_size = block_size	
		self.finestra = finestra

	def crea_entità(self, block_size, coordinate):
		for XnY in coordinate:
			self.finestra.blit(self.sprite, (XnY[0], XnY[1]))
			
	def coordinate_Entità(self, numero_di_entità, lista1):

		display_width = 800
		display_height = 400

		for i in range(numero_di_entità):
			self.main_x = round(random.randrange(0,display_width-self.block_size)/self.block_size)*self.block_size
			self.main_y = round(random.randrange(0,display_height-self.block_size)/self.block_size)*self.block_size
			lista2 = []
			randX = self.main_x
			randY = self.main_y
			lista2.append(randX)
			lista2.append(randY)
			lista1.append(lista2)

	def collisioni(self, coordinate, entita, main_x, main_y):

		Entità = Entity(self.main_x, self.main_y, self.finestra, self.block_size, self.sprite)

		for i in coordinate:
			if main_x == i[0] and main_y == i[1]:
				if entita == 'N':
					print()
					print("Desideri iniziare il combattimento?")
					print()
					print("1) Sì")
					print("2) No")
					print()
				elif entita == 'B':
					print()
					print("Desideri iniziare il combattimento con il Boss?")
					print()
					print("1) Sì")
					print("2) No")
					print()
				elif entita == 'C':
					print("Trovi qualcosa per terra, lo vuoi raccogliere?")
					print()
					print("1) Sì")
					print("2) No")
					print()
				elif entita == 'c':
					print("Desideri entrare nel castello?")
					print()
					print("1) Sì")
					print("2) No")
					print()
				risposta = input("Inserire la scelta desiserata : ")
				if risposta == "1" and (entita == 'N' or entita == 'B'):
					Entità.combattimento()
					i[0] = -100
					i[1] = -100
				if risposta == "1" and entita == 'C':
					oggetti_collezionabile = ['Pozione Curativa', 'Spada', 'Arco', 'Fionda']
					print("Hai trovato", oggetti_collezionabile[random.randint(0, 3)])
					randX = 0
					randY = 0
				if risposta == "1" and entita == 'c':
					pass
				if risposta == "2":
					main_x = i[0] + 20
					main_y = i[1] + 20


	def movimento(self, main_x, main_y, direction):

		main_x_change = 0
		main_y_change = 0
		block_velocity = 20
		display_width = 800
		display_height = 400


		if direction == 'L':
			main_x_change = -block_velocity
			main_y_change = 0
		elif direction == 'R':
			main_x_change = block_velocity
			main_y_change = 0
		elif direction == 'U':
			main_y_change = -block_velocity
			main_x_change = 0
		elif direction == 'D':
			main_y_change = block_velocity
			main_x_change = 0
		elif direction != 'L' and direction != 'R' and direction != 'U' and direction != 'D':
			main_x_change = 0
			main_y_change = 0



		if main_x >= display_width:
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

		elif main_x >= display_width:
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

		main_x += main_x_change
		main_y += main_y_change
		

	def combattimento(self):

		turno = 1
		punti_abilita = 3
		Player_Health = 1000
		Player_Damage = random.randrange(0,50)*10 

		Enemy_Health = 1000
		Enemy_Damage = random.randrange(0,30)*10
		Player_level = random.randrange(0,15)
		Player_exp = 0



		while True:
			print()
			print("----INIZIO COMBATTIMENTO----")
			print()
			print("Turno :", turno)
			turno += 1
			print()
			print("1) Mosse")
			if punti_abilita <= 0:
				print("2) Abilità")
			else:
				print("La tua abilità non si è ancora ricaricata dovrai aspettare ancora", punti_abilita, "turni")
			print()
			r = input("Inserire la scelta desiderata : ")

			if r == "1":
				mosse = ["Seul","Tyr","Isi","Eoma","Tys"]

				for i in range(len(mosse)):
					print(str(i+1)+")"+" "+mosse[i])
				print()
				input("Seleziona la mossa che si intende scegliere : ")
				print()
				Enemy_Health -= Player_Damage
				print("Hai inflitto al nemico", Player_Damage, "danni")
				Player_Health -= Enemy_Damage
				print("Il nemico ti ha inflitto", Enemy_Damage, "danni")

				if Enemy_Health <= 0:
					print()
					print("Congratulazioni hai sconfitto il nemico")
					Player_exp += Player_level*100
					print("Hai guadagnato", Player_level*100, "punti esperienza")
					print()
					if Player_exp >= Player_level*1000:
						print("Sei salito di livello")
						Player_level += 1
						print("Livello attuale :", Player_level)
					break

			elif r == "2":
				print("Usi la tua abilità è abbatti istantaneamente il nemico")
				Player_exp += Player_level*100
				print("Hai guadagnato", Player_level*100, "punti esperienza")
				print()
				if Player_exp >= Player_level*1000:
					print("Sei salito di livello")
					Player_level += 1
					print("Livello attuale :", Player_level)
				break
			punti_abilita -= 1

