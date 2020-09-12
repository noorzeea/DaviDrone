import time

def takeoff(speed, min, max):
    
    while (speed < max):
        speed += 100
        time.sleep(0.1)
        print (speed)
    return speed
    

def land(speed, max, min):
    while (speed > min):
        speed -= 100
        time.sleep(0.1)
        print (speed)
    return speed
