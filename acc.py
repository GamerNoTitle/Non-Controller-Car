#!/usr/bin/python
import wiringpi
import time

def checkdist():
    wiringpi.digitalWrite(28, 0)
    time.sleep(0.000015)
    wiringpi.digitalWrite(28, 1)
    t0=time.time()
    while not wiringpi.digitalRead(29):
        t=time.time()
        if (t-t0)>0.1:
            break
    t1=time.time()
    while wiringpi.digitalRead(29):
        t=time.time()
        if (t-t0)>0.1:
            break
    t2=time.time()
    return (t2-t1)*34000/2

# motion function
def forward(speed):
    if speed > 100:
        speed = 100
    elif speed < 0:
        speed = 0

    wiringpi.softPwmWrite(1,0)
    wiringpi.softPwmWrite(4,speed)
    wiringpi.softPwmWrite(5,0)
    wiringpi.softPwmWrite(6,speed)

# init io
wiringpi.wiringPiSetup()
wiringpi.pinMode(28,1) # trigger
wiringpi.pinMode(29,0) # echo

# left motor
wiringpi.pinMode(1,1)
wiringpi.softPwmCreate(1,0,100)
wiringpi.softPwmWrite(1,0)

wiringpi.pinMode(4,1)
wiringpi.softPwmCreate(4,0,100)
wiringpi.softPwmWrite(4,0)

# right motor
wiringpi.pinMode(5,1)
wiringpi.softPwmCreate(5,0,100)
wiringpi.softPwmWrite(5,0)

wiringpi.pinMode(6,1)
wiringpi.softPwmCreate(6,0,100)
wiringpi.softPwmWrite(6,0)

# stop
forward(0)

print("Adaptive cruise control")

"""
try:
    while True:
        speed = 0
        distance = round(checkdist(),1) #cm
        print(distance)
        if distance > 50:
            # move forward at full speed
            speed = 100
            print("Haha~~~")
        elif distance > 10:
            # pid control
            speed = int(distance * 2.0)
        elif distance > 5:
            print("Danger!!!")
            speed = 0
        else:
            print("Crash......")
            speed = 0
            break
        # print(speed)
        forward(speed)
        time.sleep(0.1)
except:
    pass

"""

forward(0)
print("End")
