# Import the needed modules

#import grovepi
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
    sleep(uniform(2.5, 6))
    grovepi.digitalWrite(redLed,1)

    while condition:
        button_status=grovepi.digitalRead(button)
        time+=1
        sleep(0.001)
        if button_status==True:
            condition=False
            grovepi.digitalWrite(redLed,0)
            print("Your reaction time is "+str(time)+"ms")
            #enregistrer résultat+ écrire dans csv

#SOUND REACTION
input("Vous allez commencez le test de réaction au son, appuyer sur ENTER pour commencer")
for i in range(1,3):
    time=0
    condition=True
    print("Le son va s'allumer, préparez vous à appuyer sur le bouton!")
    sleep(1.5)
    sleep(uniform(2.5, 6))
    grovepi.digitalWrite(redLed,1)

    while condition:
        button_status=grovepi.digitalRead(button)
        time+=1
        sleep(0.001)
        if button_status==True:
            condition=False
            grovepi.digitalWrite(buzzer,0)
            print("Your reaction time is "+str(time)+"ms")
            #enregistrer résultat+ écrire dans csv

