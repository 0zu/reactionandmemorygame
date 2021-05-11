# Import the needed modules

#import grovepi
#import time
#from time import sleep
#import random
#import csv

#INPUT
#button=8
#grovepi.pinMode(button,"INPUT")# Digital port D8 set to OUTPUT

# OUTPUTS
#redLed=2
#greenLed=3
#blueLed=4
#buzzer=5
#grovepi.pinMode(redLed,"OUTPUT")# Digital port D2 set to OUTPUT
#grovepi.pinMode(greenLed,"OUTPUT")# Digital port D3 set to OUTPUT
#grovepi.pinMode(blueLed,"OUTPUT")# Digital port D4 set to OUTPUT
#grovepi.pinMode(buzzer,"OUTPUT")# Digital port D5 set to OUTPUT

#age=input("Quel est votre age?")
#sex=input("Quel est votre sexe? m/f/autre")

#Initializing variable
#time=0
#sleep(random.uniform(2.5,6.0))
#grovepi.digitalWrite(redLed,1)
#condition=True
#while condition:
#    button_status=grovepi.digitalRead(button)
#    time+=1
#    sleep(0.001)
#    if button_status==True:
#        condition=False
#        grovepi.digitalWrite(redLed,0)
#        print("Your reaction time is "+str(time)+"ms")
file = open('memory_level.txt')
levels = file.readlines()
level1 = levels[0]
level2 = levels[1]
level3 = levels[2]
level4 = levels[3]
level5 = levels[4]

print(level1)
print(level2)
print(level3)
print(level4)
print(level5)
print(len(level1))
print(len(level2))
print(len(level3))
print(len(level4))
print(len(level5))