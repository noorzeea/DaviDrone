import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import pigpio #importing GPIO library for pulses
from ESC import arm, stop, min_value, gomax_value

from commands import *


os.system ("sudo killall pigpiod") #Launching GPIO library
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error

mot1=5  #motor 1 --> GPIO05 
mot2=6  #motor 2 --> GPIO06 
mot3=13 #motor 3 --> GPIO13 
mot4=19 #motor 4 --> GPIO19 

pi = pigpio.pi()
arm() 
speed = min_value

print("Motors armed. Ready to take off!")

command = "ignoreme"
while (command != "minchia"):
    command = input()
    if (command == "go"):
        print ("I'm going! See you soon my Lord :)")
        speed = takeoff(speed, min_value, max_value)
        print ("Tkoff: " + str(speed))
    elif (command == "land"):
        print ("Ayoooooo! Guess who's back... back again... etc...")
        speed = land(speed, max_value, min_value)
        print ("Land: " + str(speed))
    elif (command == "stop"):
        stop()
        print("Jesus Fucking Christ... Huston, I think we have a problem here...")
    else:
        print ("What?")