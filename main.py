# Import the needed modules
import grovepi
import time
from time import sleep
import random
import csv

#INPUT
button=8
grovepi.pinMode(button,"INPUT")# Digital port D8 set to OUTPUT


# OUTPUTS
redLed=2
greenLed=3
blueLed=4
buzzer=5
grovepi.pinMode(redLed,"OUTPUT")# Digital port D2 set to OUTPUT
grovepi.pinMode(greenLed,"OUTPUT")# Digital port D3 set to OUTPUT
grovepi.pinMode(blueLed,"OUTPUT")# Digital port D4 set to OUTPUT
grovepi.pinMode(buzzer,"OUTPUT")# Digital port D5 set to OUTPUT

#DICTIONARY
charToLed={
    'r':redLed,
    'g':greenLed,
    'b':blueLed,
    'v':greenLed,
}

print("Quel est votre âge")

try:
    age=int(input())
    isAgeValid=True
except:
    isAgeValid=False

while (not isAgeValid) or age<10 or age>100:
    print("Entrez un nombre entre 10 et 100")
    try:
        age=int(input())
        isAgeValid=True
    except:
        isAgeValid=False

print("Quel est votre sexe? m/f/autre")

try:
    sex=str(input()).lower()
    isSexValid=True
except:
    isSexValid=False

while (not isSexValid) or sex not in ["m","f","autre"]:
    print("Entrez m ou f ou autre")
    try:
        sex=str(input()).lower()
        isSexValid=True
    except:
        isSexValid=False

#LIGHT GAME
reactionsLED=[]
for i in range(1,4):
    print(f"{i}/3 : Appuyez une fois sur le bouton pour commencer")

    while not grovepi.digitalRead(button):
        sleep(0.001) #Attend avant d'executer la suite
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton
    print("La lumière va s'allumer...")
    sleep(random.uniform(2.5,6.0))
    grovepi.digitalWrite(redLed,1)
    start = time.time()
    #print(end - start)    
    condition=True
    while not grovepi.digitalRead(button):
        
        sleep(0.001)
    end = time.time()
    reactionsLED.append(end-start)
    condition=False
    grovepi.digitalWrite(redLed,0)
    print("Votre temps de réaction est de "+str(end-start)+" sec")
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton

#SOUND GAME
#Initializing variable
reactionsBuzzer=[]
for i in range(1,4):
    print(f"{i}/3 : Appuyez une fois sur le bouton pour commencer")

    while not grovepi.digitalRead(button):
        sleep(0.001) #Attend avant d'executer la suite
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton
    print("Le buzzer va émettre un son...")
    sleep(random.uniform(2.5,6.0))
    grovepi.digitalWrite(buzzer,1)
    start = time.time()
    #print(end - start)    
    condition=True
    while not grovepi.digitalRead(button):
        
        sleep(0.001)
    end = time.time()
    reactionsBuzzer.append(end-start)
    condition=False
    grovepi.digitalWrite(buzzer,0)
    print("Votre temps de réaction est de "+str(end-start)+" sec")
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton


#MEMORY GAME
wrongAns=0
levels=[]
with open('memory_level.csv', 'r') as csvfile:
    csvfiles = csv.reader(csvfile)
    next(csvfiles)
    for line in csvfiles:
        levels.append(str(line[1]).lower())

for i in range(1,6):
    pretString = "prêt.e"
    if (sex == 'm'): pretString = "prêt" 
    elif (sex == 'f'): pretString = "prête" 

    print(f"Appuyez sur le bouton dès que vous êtes {pretString}")
    while not grovepi.digitalRead(button):
        sleep(0.001) #Attend avant d'executer la suite
    while grovepi.digitalRead(button):
        sleep(0.001) #Vérifie que l'utilisateur ait laché le bouton
    sequence=levels[i-1]
    for color in sequence:
        grovepi.digitalWrite(charToLed[color],1)
        sleep(1.5)
        grovepi.digitalWrite(charToLed[color],0)
        sleep(0.2)
    print(f"Entrez la séquence de lumières rgb, il y a {len(sequence)} lumières")


    guess=str(input()).lower()

    guessIsValid=True
    for c in guess:
        if c not in charToLed.keys():
            guessIsValid=False
    while not guessIsValid or len(guess)!=len(sequence):
        print(f"Entrez une séquence valide rgb de {len(sequence)} caratères de long")
        guess=str(input()).lower()
        guessIsValid=True
        for c in guess:
            if c not in charToLed.keys():
                guessIsValid=False
    wrongAns+=sum(1 for i, char in enumerate(sequence) if charToLed[char] != charToLed[guess[i]])
print(f"Vous avez fait {wrongAns} erreur(s)")

with open('g13_data.csv', 'a') as csvfile:
    csvfile.write(f'{age},{sex},{reactionsLED[0]},{reactionsLED[1]},{reactionsLED[2]},{reactionsBuzzer[0]},{reactionsBuzzer[1]},{reactionsBuzzer[2]},{wrongAns}\n')