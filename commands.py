import time



def takeoff(pi, speed, min, max, mot1, mot2, mot3, mot4):
    
    while (speed < max):
        speed += 100
        pi.set_servo_pulsewidth(mot1, speed) 
        pi.set_servo_pulsewidth(mot2, speed) 
        pi.set_servo_pulsewidth(mot3, speed) 
        pi.set_servo_pulsewidth(mot4, speed) 
        time.sleep(0.1)
        print (speed)
    return speed
    

def land(pi, speed, max, min, mot1, mot2, mot3, mot4):
    while (speed > min):
        speed -= 100
        pi.set_servo_pulsewidth(mot1, speed) 
        pi.set_servo_pulsewidth(mot2, speed) 
        pi.set_servo_pulsewidth(mot3, speed) 
        pi.set_servo_pulsewidth(mot4, speed) 
        time.sleep(0.1)
        print (speed)
    return speed
