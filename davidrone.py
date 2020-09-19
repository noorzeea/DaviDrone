import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
import pigpio #importing GPIO library for pulses



os.system ("sudo killall pigpiod") #Launching GPIO library
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error

mot1=5  #motor 1 --> GPIO05 
mot2=6  #motor 2 --> GPIO06 
mot3=13 #motor 3 --> GPIO13 
mot4=19 #motor 4 --> GPIO19 

min_value = 500
max_value = 2500

speed = min_value


def takeoff(speed):
    while (speed < max):
        speed += 100
        pi.set_servo_pulsewidth(mot1, speed) 
        pi.set_servo_pulsewidth(mot2, speed) 
        pi.set_servo_pulsewidth(mot3, speed) 
        pi.set_servo_pulsewidth(mot4, speed) 
        time.sleep(0.1)
        print (speed)
    return speed
    

def land(speed): 
    while (speed > min):
        speed -= 100
        pi.set_servo_pulsewidth(mot1, speed) 
        pi.set_servo_pulsewidth(mot2, speed) 
        pi.set_servo_pulsewidth(mot3, speed) 
        pi.set_servo_pulsewidth(mot4, speed) 
        time.sleep(0.1)
        print (speed)
    return speed



def arm(): #This is the arming procedure of an ESC 

    pi.set_servo_pulsewidth(mot1, 0) 
    pi.set_servo_pulsewidth(mot2, 0) 
    pi.set_servo_pulsewidth(mot3, 0) 
    pi.set_servo_pulsewidth(mot4, 0) 
    time.sleep(1)

    pi.set_servo_pulsewidth(mot1, max_value) 
    pi.set_servo_pulsewidth(mot2, max_value) 
    pi.set_servo_pulsewidth(mot3, max_value) 
    pi.set_servo_pulsewidth(mot4, max_value) 
    time.sleep(1)

    pi.set_servo_pulsewidth(mot1, min_value) 
    pi.set_servo_pulsewidth(mot2, min_value) 
    pi.set_servo_pulsewidth(mot3, min_value) 
    pi.set_servo_pulsewidth(mot4, min_value) 
    time.sleep(1)
        
        
def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(mot1, 0) 
    pi.set_servo_pulsewidth(mot2, 0) 
    pi.set_servo_pulsewidth(mot3, 0) 
    pi.set_servo_pulsewidth(mot4, 0) 
    pi.stop()



pi = pigpio.pi()
arm() 

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
        speed = takeoff(speed)
        print ("Taking off @ " + str(speed))
    elif (command == "land"):
        print ("Ayoooooo! Guess who's back... back again... etc...\n")
        speed = land(speed)
        print ("Landing @ " + str(speed))
    elif (command == "stop"):
        stop()
        print("Jesus Fucking Christ... Huston, I think we have a problem here...\n")
    else:
        print ("What?\n")