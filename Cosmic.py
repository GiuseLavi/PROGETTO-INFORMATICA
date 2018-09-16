#Comando per caricare la libreria pygame
import pygame
import random
from pygame.locals import *

#Comando per attivare la libreria
pygame.init()

def World(finestra, main_x, main_y, block_size, block_velocity, colore_mondo, colore_mondo_chiaro, colore_mondo_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, presenza_castello, presenza_collezionabile, presenza_boss):
	
	finestra.fill(colore_mondo)
	stop = False

	# Liste di Coordinate
	coordinate = []
	alberi = []
	erba1 = []
	pixel = []
	pixel4 = []

	# Numero di Oggetti
	mostri = 0
	numero_di_erba = 15
	pixel1 = 20

	# Coordinate Player
	main_x_change = 0
	main_y_change = 0
	# Statistiche Player
	Player_Health = 100
	Player_Damage = 50
	Player_level = 1
	Player_exp = 0
	
	# Coordinate Enemy
	for i in range(numero_di_mostri):
		randX = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
		randY = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size
		mostro = []
		mostro.append(randX)
		mostro.append(randY)
		coordinate.append(mostro)
	# Statistiche Enemy
	Enemy_Health = 100
	Enemy_Damage = 30

	# Coordinate alberi
	for i in range(numero_di_alberi):
		randX = round(random.randrange(0,display_width-block_size)/block_size)*block_size
		randY = round(random.randrange(0,display_height-block_size)/block_size)*block_size
		albero = []
		albero.append(randX)
		albero.append(randY)
		alberi.append(albero)

	# Coordinate Erba
	for i in range(numero_di_erba):
		randX = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
		randY = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size
		erbaccia = []
		erbaccia.append(randX)
		erbaccia.append(randY)
		erba1.append(erbaccia)

	# Coordinate pixel colorati
	for i in range(pixel1):
		randX = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
		randY = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size
		pixel2 = []
		pixel2.append(randX)
		pixel2.append(randY)
		pixel.append(pixel2)

	for i in range(pixel1):
		randX = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
		randY = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size
		pixel3 = []
		pixel3.append(randX)
		pixel3.append(randY)
		pixel4.append(pixel3)

	# Coordinate Collezionabile
	if presenza_collezionabile == 'Sì':
		randX = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
		randY = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size
	elif presenza_collezionabile == 'No':
		randX = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
		randY = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size

	# Coordinate Castello
	if presenza_castello == 'Sì':
		randX1 = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
		randY1 = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size
	elif presenza_castello == 'No':
		randX1 = 0
		randY1 = 0

	# Coordinate Boss
	if presenza_boss == 'Sì':
		randX2 = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
		randY2 = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size
	elif presenza_boss == 'No':
		randX2 = 0
		randY2 = 0

	# Creazione Mondo di gioco
	while stop == False:

		# Gestione degli eventi
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()

			# Gestione del movimento
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

		# Gestione dei Bordi

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


		main_x += main_x_change
		main_y += main_y_change


		finestra.fill(colore_mondo)

		# Enemy
		crea_entità(block_size, nemico, coordinate)

		# Collezionabile
		if randX != 0 and randY != 0:
			finestra.blit(collezionabili, (randX, randY))

		# Castello
		if randX1 != 0 and randY1 != 0:
			finestra.blit(castello, (randX1, randY1))

		# Boss
		if colore_mondo == marrone and presenza_boss == 'Sì':
			finestra.blit(boss, (randX2, randY2))

		# Erbetta
		if colore_mondo == verde:
			crea_entità(erba_size, erba, erba1)
		elif colore_mondo == rosso:
			crea_entità(erba_size, erba_rossa, erba1)
		elif colore_mondo == blu:
			crea_entità(erba_size, erba_blu, erba1)
		elif colore_mondo == arancione:
			crea_entità(erba_size, erba_arancione, erba1)
		elif colore_mondo == bianco_opaco:
			crea_entità(erba_size, erba_bianca, erba1)
		elif colore_mondo == giallo:
			crea_entità(erba_size, erba_gialla, erba1)
		elif colore_mondo == viola_scuro:
			crea_entità(erba_size, erba_violascuro, erba1)
		elif colore_mondo == viola_chiaro:
			crea_entità(erba_size, erba_violachiaro, erba1)

		# Alberi
		if colore_mondo == verde:
			crea_entità(alberi_size, alberello, alberi)
		elif colore_mondo == rosso:
			crea_entità(alberi_size, alberello_rosso, alberi)
		elif colore_mondo == blu:
			crea_entità(alberi_size, alberello_blu, alberi)
		elif colore_mondo == arancione:
			crea_entità(alberi_size, alberello_arancione, alberi)
		elif colore_mondo == bianco_opaco:
			crea_entità(alberi_size, alberello_bianca, alberi)
		elif colore_mondo == giallo:
			crea_entità(alberi_size, alberello_gialla, alberi)
		elif colore_mondo == viola_scuro:
			crea_entità(alberi_size, alberello_violascuro, alberi)
		elif colore_mondo == viola_chiaro:
			crea_entità(alberi_size, alberello_violachiaro, alberi)
		elif colore_mondo == marrone:
			crea_entità(alberi_size, candelabro, alberi)

		# Pixel
		if colore_mondo != marrone:
			for XnY in pixel:
				pygame.draw.rect(finestra, colore_mondo_chiaro, (XnY[0], XnY[1], pixel_size, pixel_size))
			for XnY in pixel4:
				pygame.draw.rect(finestra, colore_mondo_scuro, (XnY[0], XnY[1], pixel_size, pixel_size))	

		# Player
		finestra.blit(img, (main_x, main_y))
		

		pygame.display.update() 
		clock.tick(FPS)

		# Controllo collisioni con nemici

		for i in coordinate:
			if main_x == i[0] and main_y == i[1]:
				print()
				print("Desideri iniziare il combattimento?")
				print()
				print("1) Sì")
				print("2) No")
				print()
				risposta = input("Inserire la scelta desiserata : ")
				if risposta == "1":
					combattimento(Player_Health, Player_Damage, Enemy_Health, Enemy_Damage, Player_level, Player_exp)
					if mostri < numero_di_mostri:
						mostri += 1
					del coordinate[mostri]
				if risposta == "2":
					main_x = i[0] + 20
					main_y = i[1] + 20

		# Controllo collisione con boss
			if colore_mondo == marrone:
				if main_x == randX2 and main_y == randY2:
					print()
					print("Desideri iniziare il combattimento con il Boss?")
					print()
					print("1) Sì")
					print("2) No")
					print()
					risposta = input("Inserire la scelta desiserata : ")
					if risposta == "1":
						combattimento(Player_Health, Player_Damage, Enemy_Health, Enemy_Damage, Player_level, Player_exp)
						randX2 = 0
						randY2 = 0
					if risposta == "2":
						main_x = randX2 + 20
						main_y = randY2 + 20	

		# Controllo collisione con collezionabile

		if main_x == randX and main_y == randY:
			print("Trovi qualcosa per terra, lo vuoi raccogliere?")
			print()
			print("1) Sì")
			print("2) No")
			print()
			r = input("Selezionare la scelta desiderata : ")
			if r == "1":
				print("Hai trovato", oggetti_collezionabile[random.randint(0, 3)])
				randX = 0
				randY = 0
			elif r == "2":
				main_x = randX + 20
				main_y = randY + 20

		# Controllo collisione con castello

		if main_x == randX1 and main_y == randY1:
			print("Desideri entrare nel castello?")
			print()
			print("1) Sì")
			print("2) No")
			print()
			r = input("Selezionare la scelta desiderata : ")
			if r == "1":
				colore_mondo = marrone
				World(finestra, main_x, main_y, block_size, block_velocity, marrone, marrone, marrone, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'Sì')
				randX2 = 0
				randY2 = 0
				stop = True
			elif r == "2":
				main_x = randX1 + 20
				main_y = randY1 + 20		


def messaggioPerLoSchermo(mes, colore, x, y):
	text = font.render(mes, True, colore)
	finestra.blit(text, [x, y])
	pygame.display.update()

def gameIntro():
	intro = True
	pixel = []
	pixel4 = []
	pixel1 = 20
	while intro == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					intro = False

		finestra.fill(nero)


		for i in range(pixel1):
			randX = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
			randY = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size
			pixel2 = []
			pixel2.append(randX)
			pixel2.append(randY)
			pixel.append(pixel2)

		for i in range(pixel1):
			randX = round(random.randrange(0,display_width-Enemy_size)/Enemy_size)*Enemy_size
			randY = round(random.randrange(0,display_height-Enemy_size)/Enemy_size)*Enemy_size
			pixel3 = []
			pixel3.append(randX)
			pixel3.append(randY)
			pixel4.append(pixel3)

		for XnY in pixel:
			pygame.draw.rect(finestra, bianco, (XnY[0], XnY[1], pixel_size, pixel_size))
		for XnY in pixel4:
			pygame.draw.rect(finestra, blu, (XnY[0], XnY[1], pixel_size, pixel_size))

		messaggioPerLoSchermo("Cosmic", giallo_ocra, 320, 50)
		messaggioPerLoSchermo("Missione Peyk", giallo_ocra, 260, 100)
		messaggioPerLoSchermo("Premi a per iniziare a giocare", giallo_ocra, 140, 200)
		pygame.display.update()
		clock.tick(FPS)

def crea_entità(block_size, img, coordinate):
	for XnY in coordinate:
		finestra.blit(img, (XnY[0], XnY[1]))

def Storia(frasi_storia, frasi, capitolo):
	x = 15
	y = 75
	intro = True
	prologo = 1
	capitoli = ["PROLOGO","CAPITOLO 1","CAPITOLO 2","CAPITOLO 3","CAPITOLO 4","CAPITOLO 5","CAPITOLO 6","CAPITOLO 7","CAPITOLO 8",]
	for i in range(frasi- 12,frasi):
		if prologo == 0:
			messaggioPerLoSchermo(capitoli[capitolo] , giallo_ocra, 330, 45)
		elif prologo == 1:
			messaggioPerLoSchermo( capitoli[0], giallo_ocra, 330, 15)
			prologo = 0
		messaggioPerLoSchermo(frasi_storia[i] , giallo_ocra, x, y)
		y += 25
		messaggioPerLoSchermo("Premere a per proseguire", giallo_ocra, 15, 385)

	while intro == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					intro = False


def combattimento(Player_Health, Player_Damage, Enemy_Health, Enemy_Damage, Player_level, Player_exp):

	turno = 1
	punti_abilita = 3


	while True:
		print()
		print("----INIZIO COMBATTIMENTO----")
		print()
		print("Turno :", turno)
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


# Variabili della finestra
display_width = 800
display_height = 400
finestra = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Cosmic")

# Variabili del clock
clock = pygame.time.Clock()
FPS = 30

# Frasi Storia
Capitolo_1 = ["Siediti, devo raccontarti una storia. Tanti anni or sono, nel 173 a.U., sul pianeta Peyk convivevano tre razze,i Cacciatori,","gli Stregoni e i Titani. Regnava la pace da sempre, non vi erano mai stati conflitti. Dopo molti anni, nel 32 a.U.,", "le risorse naturali del pianeta erano agli sgoccioli, serviva più spazio per tutti.","Di lì a poco cominciarono le corse agli armamenti","e con loro i primi conflitti. Vi erano grosse campagne militari. nell' anno 0 scoppia la guerra, un terribile","conflitto che comprendeva tutte e tre le razze. Non si trattava più di semplici rivolte, bensì di battaglie lunghe e sanguinose",
"Non si trattava più di semplici rivolte bensì di battaglie lunghe e sanguinose un giorno però un uomo prese le redini","dell'esercito l'uomo che riuscì a portare a termine questa lunga guerra fu proprio tuo padre Ata.","questa riappacificazione portò alla creazione di nuovi enti governativi tra cui l'O.R.U.","Ata era governatore dell’ O.R.U., Organizzazione delle Razze Unite,SEI  da ormai diversi anni, ma una nuova minaccia tormentava Peyk.","Gli Yolux, esseri appartenenti ad una razza proveniente da un altro pianeta, sbarcarono su Peyk.","Durante l'invasione Ata scomparve improvvisamente.", "A un anno dalla sua scomparsa salì al potere Zahid, vecchio amico di Ata.","Nel 13 d.U nascesti tu.","Gli Yolux, dopo 8 anni dalla loro comparsa, attuarono un colpo di stato, sgominando Zahid dal trono.",
"A questo punto rimane solo una cosa da fare, evacuare Peyk e andare il più lontano possibile per prepararsi alla battaglia.","Il luogo designato è il pianeta Uzak, pianeta un tempo abitato da Zahid.","Grazie alle tenologie portate da Peyk gli abitanti riuscirono a risanare i territori rendendoli coltivabili.","Detto questo ora ti consegno ciò che ti ha lasciato tuo padre.", "Caro figliolo, se stai leggendo questa lettera vuol dire che non sono riuscito a difendere il mio regno."," Sapevo per certo che qualcosa sarebbe successo, ma mai mi sarei immaginato così presto."," Devi stare attento figliolo, un’ enorme minaccia si sta abbattendo sul nostro pianeta e io non sarò li con te ad aiutarti.","ma ti ho affidato una delle mie armi più potenti, ti aiuterà a sconfiggere i nemici."," Fanne buon uso."," Buona fortuna figliolo, Ata.",
"Tuo padre voleva che avessi questo, ti accompagnerà nelle tue avventure: Ti consegno Rano, l'animaletto domestico di tuo padre."," È giunta l'ora di iniziare il tuo allenamento e sconfiggere il male.","SONO PASSATI QUATTRO ANNI DA QUANDO HAI INIZIATO IL TUO DURO ALLENAMENTO","Caro giocatore, in questo mondo troverai numerosi nemici ed è ora che ti spieghi come sopravvivere in questo luogo","TUTORIAL","In questo gioco ti troverai davanti numerosi nemici che dovrai sconfiggere.","Per sconfiggerli avrai a disposizione 5 mosse","1) Attacco con arma ravvicinata","2) Attacco con arma a lunga gittata","3) Attacco con magia esplosiva","4) Attacco con magia elettrizzante","5) Attacco con dardi velenosi","Inoltre potrai servirti della tua abilità che si ricaricherà ogni 3 turni per mettere subito fine allo scontro","per continuare il tuo cammino dovrai proseguire verso destra",
"Lungo il percorso potrai anche imbatterti in forzieri e andandoci sopra potrai ottenere oggetti rari","Sconfiggendo i nemici otterrai esperienza per salire di livello","E ora facciamo una prova",
"", "", "","", "", "","", "","","Parti da Uzak alla volta di Peyk","","","","","", "","","","","","",""]
Capitolo_2 = ["Nonostante tu abbia sconfitto i nemici che ti avevano teso un'imboscata nel porto,","continuando il percorso vieni circondato e costretto alla fuga.","Solo grazie al sacrificio dei tuoi compagni riuscirai a fuggire. ","Capisci, così, che prima di colpire il loro quartier generale dovrai agire nei pianeti circostanti per indebolirli.", "", "", "", "", "", "", "", "", "", ""]#fine capitolo 2
Capitolo_3 = ["Tornato ad Uzak per curarti dagli attacchi ricevuti in combattimento, riparti dopo pochi giorni alla volta del pianeta Ilk","Dopo essere sbarcato al porto di Ilk ed aver camminato per alcune ore ti ritrovi nella Città di Silfe","","","","","","","","","","","","","Decidi di attaccare la base con i tuoi uomini.","Sei riuscito ad espugnare la base nemica ed ad ottenere informazioni riguardanti la prima guerra di Usyan,","in particolare di un gruppo di persone che durante il conflitto non volevano entrare in guerra.","","","","","","","",""]#fine capitolo 3
Capitolo_4 = ["Dopo alcuni giorni di riposo e di rifornimento sul pianeta Ilk decidi di partire alla volta del pianeta Iki","Dopo essere sbarcato al porto di Iki prosegui fino ad arrivare alla Città di Uil, dove si trova la base nemica","Decidi allora di attaccare","","","","","","","","","","Sei riuscito ad espugnare la base nemica,","scoprendo anche che le persone che non volevano partecipare alla guerra vennero esiliati in un pianeta lontano","e che queste stesse persone tramavano vendetta nei confronti della popolazione","","","","","","","","",""]#fine capitolo 4
Capitolo_5 = ["Dopo aver scoperto la vera identità degli Yolux","decidi di partire e andare sul pianeta Uuk per scoprire nuove informazioni sugli Yolux.","Arrivato sul pianeta scopri di essere ricercato ma riesci comunque a cavartela e ad arrivare alla Città di Silon","","","","","","","","","","Sei riuscito a sconfiggere il capo della Città di Silon e hai scoperto","che gli Yolux in realtà possiedono dei geni modificati che hanno modificato la loro razza","di appartenenza trasformandoli e rendendoli più forti di un normale individuo","","","","","","","","",""]#fine capitolo 5
Capitolo_6 = ["Dopo alcuni giorni di riposo riparti verso il pianeta Dord","Dopo aver sconfitto i nemici che attendevano il tuo arrivo riesci a fuggire dalle guardie arrivando alla Città di Rodach","","","","","","","","","","","Mentre stavi combattendo con il capo Yolux del pianeta scopri che in realtà","ti stanno facendo perdere tempo mentre loro stanno attaccando il pianeta Uzak.","Dopo aver scoperto il piano degli Yolux ti sbrighi e torni al più presto sul pianeta Uzak","riuscendo a salvare la popolazione facendola, però, trasferire sul pianeta Ilk","","","","","","","","",""]#fine capitolo 6
Capitolo_7 = ["Dopo aver salvato gli abitanti del pianeta Uzak e averli trasferiti sul pianeta Ilk, sbarchi sul pianeta Bess","Sbarcato su Bess e occupatoti della sicurezza arrivi davanti alla base nemica e inizi l'attacco alla base nemica","","","","","","","","","","","Dopo aver sconfitto il capo Yolux di questo pianeta ti dirigi a sconfiggere il capo degli Yolux, che si trova sul pianeta Nazil","","","","","","","","","","",""]#fine capitolo 7
Capitolo_8 = ["Arrivato sul pianeta Nazil noti subito l'elevata sicurezza","Dopo aver sconfitto la sicurezza trovata al porto raggiungi al più presto la base nemica","","","","","","","","","","","Mentre combattevi contro il capo degli Yolux scopri che in realtà il capo degli Yolux è tuo padre, Ata.","Egli era stato rapito dagli Yolux durante la loro prima apparizione","e che li ha condotti alla conquista di Peyk e dei pianeti circostanti.","Dopo aver scoperto che tuo padre è ancora vivo provi a dissuaderlo dal continuare questo assurdo piano",",ma senza successo. Ti trovi perciò costretto a combattere tuo padre e a sconfiggerlo.","Dopo il combattimento finale contro tuo padre riconquisti definitivamente Nazil e anche Peyk","riuscendo a riportare la pace e diventando anche capo generale dell'O.R.U.","FINE","","grazie per aver giocato","Andrea Lavino & Giuseppe Di Vara",""]

# Colori
bianco = [255, 255, 255]
marrone = [128, 0, 0]
bianco_opaco = [192, 192, 192]
bianco_opaco_chiaro = [220, 220, 220]
bianco_opaco_scuro = [128, 128, 128]
nero = [0, 0, 0]
rosso = [255, 0, 0]
rosso_chiaro = [250, 128, 114]
rosso_scuro = [139, 0, 0]
verde = [50, 205, 50]
verde_chiaro = [0, 255, 0]
verde_scuro = [0, 100, 0]
blu = [0,0,255]
blu_chiaro = [173, 216, 230]
blu_scuro = [25, 25, 112]
giallo_ocra = [255, 215, 0]
giallo = [255, 255, 0]
giallo_chiaro = [240, 230, 140]
arancione = [255, 140, 0]
arancione_chiaro = [255, 165, 0]
arancione_scuro = [255, 69, 0]
viola_chiaro_chiaro = [216, 191, 216]
viola_chiaro = [238, 130, 238]
viola_chiaro_scuro = [218, 112, 214]
viola_scuro_scuro = [128, 0, 128]
viola_scuro = [148, 0, 211]
viola_scuro_chiaro = [186, 85, 211]



colori = [bianco, nero, rosso, verde, verde_chiaro, verde_scuro, blu, giallo_ocra]


font = pygame.font.SysFont(None, 50)

# Coordinate Player
main_x = 30
main_y = 30

# Grandezza dei vari blocchi
block_size = 20
alberi_size = 30
Enemy_size = 30
erba_size = 10
block_velocity = 10
frasi = 12
capitolo = 1

# Numero di Oggetti
oggetti_collezionabile = ['Pozione Curativa', 'Spada', 'Arco', 'Fionda']
numero_di_mostri = 5
numero_di_alberi = 5
pixel_size = 4

# Caricamento Sprite

alberello = pygame.image.load('albero.png')
alberello_blu = pygame.image.load('albero.blue.png')
alberello_violascuro = pygame.image.load('albero.darkpurple.png')
alberello_violachiaro = pygame.image.load('albero.lightpurple.png')
alberello_arancione = pygame.image.load('albero.orange.png')
alberello_rosso = pygame.image.load('albero.red.png')
alberello_bianco = pygame.image.load('albero.white.png')
alberello_giallo = pygame.image.load('albero.yellow.png')
erba_blu = pygame.image.load('erba.blue.png')
erba_violascuro = pygame.image.load('erba.darkpurple.png')
erba_violachiaro = pygame.image.load('erba.lightpurple.png')
erba_arancione = pygame.image.load('erba.orange.png')
erba_rossa = pygame.image.load('erba.red.png')
erba_bianca = pygame.image.load('erba.white.png')
erba_gialla = pygame.image.load('erba.yellow.png')
nemico = pygame.image.load('nemico.png')
collezionabili = pygame.image.load('collezionabile.png')
erba = pygame.image.load('erba.png')
icon = pygame.image.load('rano.png')
castello = pygame.image.load('castello.png')
candelabro = pygame.image.load('candelabro.png')
boss = pygame.image.load('boss.png')


pygame.display.set_icon(icon)
finestra.fill(bianco)

print()	
print("1) Stregone")
print("2) Cacciatore")
print("3) Titano")
print()
razza = input("Inserisci la razza alla quale vuoi appartenere : ")

# Caricamento Sprite Player

if razza == "1": 
	img = pygame.image.load('stregone.png')
elif razza == "2":
	img = pygame.image.load('cacciatore.png')
elif razza == "3":
	img = pygame.image.load('titano.png')

gameIntro()

font = pygame.font.SysFont(None, 20)
# Prologo

finestra.fill(nero)
Storia(Capitolo_1, frasi, capitolo)
frasi += 12
finestra.fill(nero)
Storia(Capitolo_1, frasi, capitolo)
finestra.fill(nero)
frasi += 12
Storia(Capitolo_1, frasi, capitolo)
finestra.fill(nero)
frasi += 12
Storia(Capitolo_1, frasi, capitolo)
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, verde, verde_chiaro, verde_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
frasi += 12
Storia(Capitolo_1, frasi, capitolo)
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, verde, verde_chiaro, verde_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)

frasi = 12 
capitolo = 2
Storia(Capitolo_2, frasi, capitolo)
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, blu, blu_chiaro, blu_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)

capitolo = 3
Storia(Capitolo_3, frasi, capitolo)
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, arancione, arancione_chiaro, arancione_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, arancione, arancione_chiaro, arancione_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
numero_di_mostri = 10
World(finestra, main_x, main_y, block_size, block_velocity, arancione, arancione_chiaro, arancione_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'Sì', 'Sì', 'Sì')

finestra.fill(nero)
capitolo = 4
frasi = 12
numero_di_mostri = 5
Storia(Capitolo_4, frasi, capitolo)
frasi += 12
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, rosso, rosso_chiaro, rosso_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, rosso, rosso_chiaro, rosso_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
numero_di_mostri = 10
World(finestra, main_x, main_y, block_size, block_velocity, rosso, rosso_chiaro, rosso_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'Sì', 'Sì', 'Sì')
finestra.fill(nero)
Storia(Capitolo_4, frasi, capitolo)
finestra.fill(nero)

capitolo = 5
frasi = 12
numero_di_mostri = 5
Storia(Capitolo_5, frasi, capitolo)
frasi += 12
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, viola_chiaro, viola_chiaro_chiaro, viola_chiaro_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, viola_chiaro, viola_chiaro_chiaro, viola_chiaro_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
numero_di_mostri = 10
World(finestra, main_x, main_y, block_size, block_velocity, viola_chiaro, viola_chiaro_chiaro, viola_chiaro_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'Sì', 'Sì', 'Sì')
finestra.fill(nero)
Storia(Capitolo_5, frasi, capitolo)
finestra.fill(nero)

capitolo = 6
frasi = 12
numero_di_mostri = 5
Storia(Capitolo_6, frasi, capitolo)
frasi += 12
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, viola_scuro, viola_scuro_chiaro, viola_scuro_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, viola_scuro, viola_scuro_chiaro, viola_scuro_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
numero_di_mostri = 10
World(finestra, main_x, main_y, block_size, block_velocity, viola_scuro, viola_scuro_chiaro, viola_scuro_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'Sì', 'Sì', 'Sì')
finestra.fill(nero)
Storia(Capitolo_5, frasi, capitolo)
finestra.fill(nero)

capitolo = 7
frasi = 12
numero_di_mostri = 5
Storia(Capitolo_7, frasi, capitolo)
frasi += 12
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, giallo, giallo_chiaro, giallo_ocra, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, giallo, giallo_chiaro, giallo_ocra, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
numero_di_mostri = 10
World(finestra, main_x, main_y, block_size, block_velocity, giallo, giallo_chiaro, giallo_ocra, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'Sì', 'Sì', 'Sì')
finestra.fill(nero)
Storia(Capitolo_7, frasi, capitolo)
finestra.fill(nero)

capitolo = 8
frasi = 12
numero_di_mostri = 5
Storia(Capitolo_8, frasi, capitolo)
frasi += 12
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, bianco_opaco, bianco_opaco_chiaro, bianco_opaco_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
World(finestra, main_x, main_y, block_size, block_velocity, bianco_opaco, bianco_opaco_chiaro, bianco_opaco_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'No', 'Sì', 'No')
finestra.fill(nero)
numero_di_mostri = 10
World(finestra, main_x, main_y, block_size, block_velocity, bianco_opaco, bianco_opaco_chiaro, bianco_opaco_scuro, numero_di_mostri, numero_di_alberi, oggetti_collezionabile, 'Sì', 'Sì', 'Sì')
finestra.fill(nero)
Storia(Capitolo_8, frasi, capitolo)
finestra.fill(nero)






# Chiusura Programma
pygame.quit()