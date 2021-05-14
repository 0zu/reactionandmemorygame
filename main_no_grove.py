# Import the needed modules

import time
from time import sleep
import random
import csv

with open('memory_level.csv', 'r', encoding='utf-8-sig') as csvfile:
    levels = csv.reader(csvfile, delimiter=';')
    next(levels)
    for line in levels:
        print(line[1])

#JEU
age=input("Quel est votre age?")
sex=input("Quel est votre sexe? m/f/autre")

#LIGHT REACTION
input("Vous allez commencez le test de réaction à la lumière, appuyer sur ENTER pour commencer")
for i in range(1,3):
    time=0
    condition=True
    print("Le rouge va s'allumer, préparez vous à appuyer sur le bouton!")
    sleep(1.5)
    sleep(random.uniform(2.5, 6.0))
    redLight=True

    while condition:
        time+=1
        sleep(0.001)
        print("Red light is ON")
        if input("Ecrivez STOP"):
            condition=False
            redLight=False
            print("Your reaction time is "+str(time)+"ms")
            #enregistrer résultat+ écrire dans csv

##SOUND REACTION
#input("Vous allez commencez le test de réaction au son, appuyer sur ENTER pour commencer")
#for i in range(1,3):
#    time=0
#    condition=True
#    print("Le son va s'allumer, préparez vous à appuyer sur le bouton!")
#    sleep(1.5)
#    sleep(uniform(2.5, 6))
#    grovepi.digitalWrite(redLed,1)

#    while condition:
#        button_status=grovepi.digitalRead(button)
#        time+=1
#        sleep(0.001)
#        if button_status==True:
#            condition=False
#            grovepi.digitalWrite(buzzer,0)
#            print("Your reaction time is "+str(time)+"ms")
#            #enregistrer résultat+ écrire dans csv
##MEMORY GAME
#print("Vous allez commencer le jeu de mémoire, appuyer sur ENTER dès que vous êtes prêt")
#level="rggbg"
#nbrOfLight=str(len(level))
#print("Il y a eu "+nbrOfLight+" lumières qui se sont allumés")
#user_guess=input("Entrez dans le shell ce que vous avez vu")

##Compare level and userinput
#level="rrgbg"
#user="rgrbr"
#print(level)
#print(user)
#splitedlevel=list(level)
#print(splitedlevel)
#spliteduser=list(user)
#print(spliteduser)
