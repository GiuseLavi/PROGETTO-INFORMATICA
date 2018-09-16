#Comando per caricare la libreria pygame
import os
import pygame
import random
from Cosmic_World import World
import Cosmic_Entity
from pygame.locals import *

#Comando per attivare la libreria
pygame.init()
pygame.mixer.init()


def messaggioPerLoSchermo(mes, colore, x, y):
	text = font.render(mes, True, colore)
	finestra.blit(text, [x, y])
	pygame.display.update()

# Menu di gioco 
'''
def menu():
	menu = True
	while menu == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.
'''

# Intro Gioco 

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


# Storia

def Storia(frasi_storia, frasi, frasi_da_togliere, prologo, capitolo):
	x = 15
	y = 75
	intro = True
	capitoli = ["PROLOGO","CAPITOLO 1","CAPITOLO 2","CAPITOLO 3","CAPITOLO 4","CAPITOLO 5","CAPITOLO 6","CAPITOLO 7","CAPITOLO 8",]
	for i in range(frasi - frasi_da_togliere, frasi):
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
"Parti da Uzak alla volta di Peyk"]
Capitolo_2 = ["Nonostante tu abbia sconfitto i nemici che ti avevano teso un'imboscata nel porto,","continuando il percorso vieni circondato e costretto alla fuga.","Solo grazie al sacrificio dei tuoi compagni riuscirai a fuggire. ","Capisci, così, che prima di colpire il loro quartier generale dovrai agire nei pianeti circostanti per indebolirli."]#fine capitolo 2
Capitolo_3 = ["Tornato ad Uzak per curarti dagli attacchi ricevuti in combattimento, riparti dopo pochi giorni alla volta del pianeta Ilk","Dopo essere sbarcato al porto di Ilk ed aver camminato per alcune ore ti ritrovi nella Città di Silfe","Decidi di attaccare la base con i tuoi uomini.","Sei riuscito ad espugnare la base nemica ed ad ottenere informazioni riguardanti la prima guerra di Usyan,","in particolare di un gruppo di persone che durante il conflitto non volevano entrare in guerra."]#fine capitolo 3
Capitolo_4 = ["Dopo alcuni giorni di riposo e di rifornimento sul pianeta Ilk decidi di partire alla volta del pianeta Iki","Dopo essere sbarcato al porto di Iki prosegui fino ad arrivare alla Città di Uil, dove si trova la base nemica","Decidi allora di attaccare","Sei riuscito ad espugnare la base nemica,","scoprendo anche che le persone che non volevano partecipare alla guerra vennero esiliati in un pianeta lontano","e che queste stesse persone tramavano vendetta nei confronti della popolazione"]#fine capitolo 4
Capitolo_5 = ["Dopo aver scoperto la vera identità degli Yolux","decidi di partire e andare sul pianeta Uuk per scoprire nuove informazioni sugli Yolux.","Arrivato sul pianeta scopri di essere ricercato ma riesci comunque a cavartela e ad arrivare alla Città di Silon","Sei riuscito a sconfiggere il capo della Città di Silon e hai scoperto","che gli Yolux in realtà possiedono dei geni modificati che hanno modificato la loro razza","di appartenenza trasformandoli e rendendoli più forti di un normale individuo"]#fine capitolo 5
Capitolo_6 = ["Dopo alcuni giorni di riposo riparti verso il pianeta Dord","Dopo aver sconfitto i nemici che attendevano il tuo arrivo riesci a fuggire dalle guardie arrivando alla Città di Rodach","Mentre stavi combattendo con il capo Yolux del pianeta scopri che in realtà","ti stanno facendo perdere tempo mentre loro stanno attaccando il pianeta Uzak.","Dopo aver scoperto il piano degli Yolux ti sbrighi e torni al più presto sul pianeta Uzak","riuscendo a salvare la popolazione facendola, però, trasferire sul pianeta Ilk"]#fine capitolo 6
Capitolo_7 = ["Dopo aver salvato gli abitanti del pianeta Uzak e averli trasferiti sul pianeta Ilk, sbarchi sul pianeta Bess","Sbarcato su Bess e occupatoti della sicurezza arrivi davanti alla base nemica e inizi l'attacco alla base nemica","Dopo aver sconfitto il capo Yolux di questo pianeta ti dirigi a sconfiggere il capo degli Yolux, che si trova sul pianeta Nazil"]#fine capitolo 7
Capitolo_8 = ["Arrivato sul pianeta Nazil noti subito l'elevata sicurezza","Dopo aver sconfitto la sicurezza trovata al porto raggiungi al più presto la base nemica","Mentre combattevi contro il capo degli Yolux scopri che in realtà il capo degli Yolux è tuo padre, Ata.","Egli era stato rapito dagli Yolux durante la loro prima apparizione","e che li ha condotti alla conquista di Peyk e dei pianeti circostanti.","Dopo aver scoperto che tuo padre è ancora vivo provi a dissuaderlo dal continuare questo assurdo piano",",ma senza successo. Ti trovi perciò costretto a combattere tuo padre e a sconfiggerlo.","Dopo il combattimento finale contro tuo padre riconquisti definitivamente Nazil e anche Peyk","riuscendo a riportare la pace e diventando anche capo generale dell'O.R.U.","FINE","","grazie per aver giocato","Andrea Lavino & Giuseppe Di Vara",""]

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

# Musica

listofsongs = []


colori = [bianco, nero, rosso, verde, verde_chiaro, verde_scuro, blu, giallo_ocra]


font = pygame.font.SysFont(None, 50)

# Coordinate Player
main_x = 30
main_y = 30

# Grandezza dei vari blocchi

Enemy_size = 20
block_size = 20
pixel_size = 4
frasi = 12
frasi_da_togliere = 12
capitolo = 1
prologo = 1

# Numero di Oggetti

numero_di_mostri = 5

# Caricamento Sprite

icon = pygame.image.load('rano.png')

candelabro = pygame.image.load('candelabro.png')
boss = pygame.image.load('boss.png')
menu = pygame.image.load('Menù.png')


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

# Prologo e Capitolo 1
'''
directory = 'C:/Users/asus/Desktop/cartelle utili/informatica/Colonne Sonore'

for files in os.listdir(directory):
	if files.endswith(".mp3"):
		listofsongs.append(files)

pygame.mixer.music.load(listofsongs[0])
pygame.mixer.music.play()
'''

pianeta1 = World(finestra, numero_di_mostri, verde, verde_chiaro, verde_scuro)
pianeta2 = World(finestra, numero_di_mostri, blu, blu_chiaro, blu_scuro)
pianeta3 = World(finestra, numero_di_mostri, arancione, arancione_chiaro, arancione_scuro)
pianeta4 = World(finestra, numero_di_mostri, rosso, rosso_chiaro, rosso_scuro)
pianeta5 = World(finestra, numero_di_mostri, viola_chiaro, viola_chiaro_chiaro, viola_chiaro_scuro)
pianeta6 = World(finestra, numero_di_mostri, viola_scuro, viola_chiaro_scuro, viola_scuro_scuro)
pianeta7 = World(finestra, numero_di_mostri, giallo, giallo_chiaro, giallo_ocra)
pianeta8 = World(finestra, numero_di_mostri, bianco_opaco, bianco_opaco_chiaro, bianco_opaco_scuro)


finestra.fill(nero)
Storia(Capitolo_1, frasi, frasi_da_togliere, prologo, capitolo)
frasi += 12
finestra.fill(nero)
Storia(Capitolo_1, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)
frasi += 12
Storia(Capitolo_1, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)
frasi += 6
frasi_da_togliere = 6
Storia(Capitolo_1, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)
pianeta1.draw('No', 'No', img)
finestra.fill(nero)
frasi += 1
frasi_da_togliere = 1
Storia(Capitolo_1, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)
pianeta1.draw('No', 'No', img)
finestra.fill(nero)

# Capitolo 2

prologo = 0
frasi = 4
frasi_da_togliere = 4
capitolo = 2
Storia(Capitolo_2, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)
pianeta2.draw('No', 'No', img)
finestra.fill(nero)

# Capitolo 3

capitolo = 3
frasi = 2
frasi_da_togliere = 2
Storia(Capitolo_3, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)
pianeta3.draw('No', 'No', img)
finestra.fill(nero)
pianeta3.draw('No', 'No', img)
finestra.fill(nero)
numero_di_mostri = 10
pianeta3.draw('Sì', 'Sì', img)
finestra.fill(nero)
frasi += 3
frasi_da_togliere = 3
Storia(Capitolo_3, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)

# Capitolo 4

capitolo = 4
frasi = 3
frasi_da_togliere = 3
numero_di_mostri = 5
Storia(Capitolo_4, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)
pianeta4.draw('No', 'No', img)
finestra.fill(nero)
pianeta4.draw('No', 'No', img)
finestra.fill(nero)
numero_di_mostri = 10
pianeta4.draw('Sì', 'Sì', img)
finestra.fill(nero)
frasi += 3
Storia(Capitolo_4, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)

# Capitolo 5

capitolo = 5
frasi = 3
numero_di_mostri = 5
Storia(Capitolo_5, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)
pianeta5.draw('No', 'No', img)
finestra.fill(nero)
pianeta5.draw('No', 'No', img)
finestra.fill(nero)
numero_di_mostri = 10
pianeta5.draw('Sì', 'Sì', img)
frasi += 3
frasi_da_togliere = 3
finestra.fill(nero)
Storia(Capitolo_5, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)

# Capitolo 6

capitolo = 6
frasi = 2
frasi_da_togliere = 2
numero_di_mostri = 5
Storia(Capitolo_6, frasi, frasi_da_togliere, prologo, capitolo)
frasi += 4
frasi_da_togliere = 4
finestra.fill(nero)
pianeta6.draw('No', 'No', img)
finestra.fill(nero)
pianeta6.draw('No', 'No', img)
finestra.fill(nero)
numero_di_mostri = 10
pianeta6.draw('Sì', 'Sì', img)
finestra.fill(nero)
Storia(Capitolo_6, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)

# Capitolo 7

capitolo = 7
frasi = 2
frasi_da_togliere = 2
numero_di_mostri = 5
Storia(Capitolo_7, frasi, frasi_da_togliere, prologo, capitolo)
frasi += 1
frasi_da_togliere = 1
finestra.fill(nero)
pianeta7.draw('No', 'No', img)
finestra.fill(nero)
pianeta7.draw('No', 'No', img)
finestra.fill(nero)
numero_di_mostri = 10
pianeta7.draw('Sì', 'Sì', img)
finestra.fill(nero)
Storia(Capitolo_7, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)

# Capitolo 8

capitolo = 8
frasi = 2
frasi_da_togliere = 2
numero_di_mostri = 5
Storia(Capitolo_8, frasi, frasi_da_togliere, prologo, capitolo)
frasi += 12
frasi_da_togliere = 12
finestra.fill(nero)
pianeta8.draw('No', 'No', img)
finestra.fill(nero)
pianeta8.draw('No', 'No', img)
finestra.fill(nero)
numero_di_mostri = 10
pianeta8.draw('Sì', 'Sì', img)
finestra.fill(nero)
Storia(Capitolo_8, frasi, frasi_da_togliere, prologo, capitolo)
finestra.fill(nero)






# Chiusura Programma
pygame.quit()