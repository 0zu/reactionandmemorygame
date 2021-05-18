# Import the needed modules
import grovepi
import time
from time import sleep
import random
import csv
import grove_rgb_lcd

#INPUT
button=8
grovepi.pinMode(button,"INPUT")     # Digital port D8 set to OUTPUT

# OUTPUTS
redLed=2
grovepi.pinMode(redLed,"OUTPUT")    # Digital port D2 set to OUTPUT

greenLed=3
grovepi.pinMode(greenLed,"OUTPUT")  # Digital port D3 set to OUTPUT

blueLed=4
grovepi.pinMode(blueLed,"OUTPUT")   # Digital port D4 set to OUTPUT

buzzer=5
grovepi.pinMode(buzzer,"OUTPUT")    # Digital port D5 set to OUTPUT

# Set green background on RGB LCD Display
grove_rgb_lcd.setRGB(0,255,0)

#DICTIONARY
charToLed={
    'r':redLed,
    'g':greenLed,
    'b':blueLed,
    'v':greenLed,   #Permet à l'utilisateur de rentrer soit v ou g pour le jeu de mémoire
}

#ENTREE AGE
print("Quel est votre âge?")
grove_rgb_lcd.setText_norefresh("Quel est votre âge?")  #Affichage sur LCD
try:
    age=int(input())    #Vérifie que l'utilisateur ait rentré un entier
    isAgeValid=True
except:
    isAgeValid=False

while (not isAgeValid) or age<10 or age>100:    #Demande à l'utilisateur de rentrer un age entre 10 et 100 si non valide
    print("Entrez un nombre entre 10 et 100")
    grove_rgb_lcd.setText_norefresh("Entrez un nombre entre 10 et 100")  #Affichage sur LCD
    try:
        age=int(input())
        isAgeValid=True
    except:
        isAgeValid=False

#ENTREE SEX
print("Quel est votre sexe? m/f/autre")
grove_rgb_lcd.setText_norefresh("Quel est votre sexe? m/f/autre")  #Affichage sur LCD

try:
    sex=str(input()).lower() #Vérifie que l'utilisateur ait rentré un sexe valide et convertit en minuscule
    isSexValid=True
except:
    isSexValid=False

while (not isSexValid) or sex not in ["m","f","autre"]: #Demande de rentrer un sexe valide
    print("Entrez m ou f ou autre")
    grove_rgb_lcd.setText_norefresh("Entrez m ou f ou autre")  #Affichage sur LCD
    try:
        sex=str(input()).lower()
        isSexValid=True
    except:
        isSexValid=False

#LIGHT GAME
reactionsLED=[]         #Initializing variable
for i in range(1,4):    #Le jeu se fait 3 fois
    print(f"{i}/3 : Appuyez une fois sur le bouton pour commencer")
    grove_rgb_lcd.setText_norefresh(f"{i}/3 : Appuyez une fois sur le bouton pour commencer")  #Affichage sur LCD
    while not grovepi.digitalRead(button):
        sleep(0.001) #Attend avant d'executer la suite
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton

    print("La lumière va s'allumer...")
    grove_rgb_lcd.setText_norefresh("La lumière va s'allumer...")  #Affichage sur LCD
    sleep(random.uniform(2.5,6.0))  #Délais avant allumage
    grovepi.digitalWrite(redLed,1)
    start = time.time() #Début de la mesure de temps
    while not grovepi.digitalRead(button):
        sleep(0.001)    #Délais pour ne pas surcharger de taches
    end = time.time()   #Fin de la mesure de temps
    reactionsLED.append(end-start)  #Ecriture des résultats dans la variable en seconde
    grovepi.digitalWrite(redLed,0)  #Déclenchement de la lumière
    print("Votre temps de réaction est de "+str(end-start)+" sec")
    grove_rgb_lcd.setText_norefresh("Votre temps de réaction est de "+str(end-start)+" sec")  #Affichage sur LCD
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton pour recommencer le jeu

#SOUND GAME
reactionsBuzzer=[]      #Initializing variable
for i in range(1,4):    #Le jeu se fait 3 fois
    print(f"{i}/3 : Appuyez une fois sur le bouton pour commencer")
    grove_rgb_lcd.setText_norefresh(f"{i}/3 : Appuyez une fois sur le bouton pour commencer")  #Affichage sur LCD
    while not grovepi.digitalRead(button):
        sleep(0.001) #Attend avant d'executer la suite
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton

    print("Le buzzer va émettre un son...")
    grove_rgb_lcd.setText_norefresh("Le buzzer va émettre un son...")  #Affichage sur LCD
    sleep(random.uniform(2.5,6.0))  #Délais avant allumage
    grovepi.digitalWrite(buzzer,1)
    start = time.time() #Début de la mesure du temps
    while not grovepi.digitalRead(button):    
        sleep(0.001)    #Délais pour ne pas surcharger de taches
    end = time.time()   #Fin de la mesure de temps
    reactionsBuzzer.append(end-start)   #Ecriture des résultats dans la variable
    grovepi.digitalWrite(buzzer,0)      #Déclenchement du son
    print("Votre temps de réaction est de "+str(end-start)+" sec")
    grove_rgb_lcd.setText_norefresh("Votre temps de réaction est de "+str(end-start)+" sec")  #Affichage sur LCD
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton pour recommencer le jeu

#MEMORY GAME
wrongAns=0  #Initializing variable
levels=[]   #Initializing variable
with open('memory_level.csv', 'r') as csvfile:  #Lecture du fichier de niveau
    csvfiles = csv.reader(csvfile)
    next(csvfiles)
    for line in csvfiles:
        levels.append(str(line[1]).lower()) #Conversion en mininuscule et enregistrement des niveaux dans la variable

for i in range(1,6): #Il y a 5 niveaux

    #Genre du joueur
    readyString = "prêt.e"
    if (sex == 'm'): readyString = "prêt" 
    elif (sex == 'f'): readyString = "prête" 

    print(f"Appuyez sur le bouton dès que vous êtes {readyString}")
    grove_rgb_lcd.setText_norefresh(f"Appuyez sur le bouton dès que vous êtes {readyString}")  #Affichage sur LCD
    while not grovepi.digitalRead(button):
        sleep(0.001) #Attend avant d'executer la suite
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton
    sequence=levels[i-1] #Récupération du niveau à jouer
    for color in sequence:  #Lecture de la séquence à allumer
        grovepi.digitalWrite(charToLed[color],1)    #Allumage à l'aide du dictionnaire
        sleep(2.2)
        grovepi.digitalWrite(charToLed[color],0)    #Déclenchement à l'aide du dicionnaire
        sleep(0.8)
    print(f"Entrez la séquence de lumières rgb, il y a {len(sequence)} lumières")
    grove_rgb_lcd.setText_norefresh(f"Entrez la séquence de lumières rgb, il y a {len(sequence)} lumières")  #Affichage sur LCD

    guess=str(input()).lower()  #Conversion en miniscule de la réponse de l'utilisateur

    guessIsValid=True
    for c in guess:
        if c not in charToLed.keys():
            guessIsValid=False
    while not guessIsValid or len(guess)!=len(sequence): #La longueur de la réponse utilisateur et la séquence doivent etre la meme et doit contenir soit r g b v
        print(f"Entrez une séquence valide rgb de {len(sequence)} caratères de long")
        grove_rgb_lcd.setText_norefresh(f"Entrez une séquence valide rgb de {len(sequence)} caratères de long")  #Affichage sur LCD
        guess=str(input()).lower() #Conversion en minuscule
        guessIsValid=True
        for c in guess:
            if c not in charToLed.keys():
                guessIsValid=False
    wrongAns+=sum(1 for i, char in enumerate(sequence) if charToLed[char] != charToLed[guess[i]])   #Additionner le nombre d'erreur à la fin de chaque niveau
print(f"Vous avez fait {wrongAns} erreur(s)/32")
grove_rgb_lcd.setText_norefresh(f"Vous avez fait {wrongAns} erreur(s)/32")  #Affichage sur LCD

#ECRITURE DES DONNEES DANS LE CSV
with open('g13_data.csv', 'a') as csvfile:
    csvfile.write(f'{age},{sex},{reactionsLED[0]},{reactionsLED[1]},{reactionsLED[2]},{reactionsBuzzer[0]},{reactionsBuzzer[1]},{reactionsBuzzer[2]},{wrongAns}\n')