import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import pigpio #importing GPIO library for pulses
from ESC import arm, stop, min_value, max_value

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

print("Motors armed. Ready to take off!\n")

command = "start"
while (command != "shut"):
    #starting the motors
    pi.set_servo_pulsewidth(mot1, speed) 
    pi.set_servo_pulsewidth(mot2, speed) 
    pi.set_servo_pulsewidth(mot3, speed) 
    pi.set_servo_pulsewidth(mot4, speed) 

    #managing commands
    command = input("Those are the commands: \nType 'takeoff' to take off;\nType 'land' to land;\nType 'stop' if you end up on a tree\nType 'shut' to close the program\n")
    if (command == "takeoff"):
        print ("I'm going! See you soon my Lord :)\n")
        speed = takeoff(pi, speed, min_value, max_value, mot1, mot2, mot3, mot4)
        print ("Taking off @ " + str(speed))
    elif (command == "land"):
        print ("Ayoooooo! Guess who's back... back again... etc...\n")
        speed = land(pi, speed, max_value, min_value, mot1, mot2, mot3, mot4)
        print ("Landing @ " + str(speed))
    elif (command == "stop"):
        stop()
        print("Jesus Fucking Christ... Huston, I think we have a problem here...\n")
    else:
        print ("What?\n")