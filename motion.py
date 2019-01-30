import time
import wiringpi
wiringpi.wiringPiSetup()

wiringpi.pinMode(1,1)
wiringpi.softPwmCreate(1,0,100)
wiringpi.softPwmWrite(1,0)

wiringpi.pinMode(4,1)
wiringpi.softPwmCreate(4,0,100)
wiringpi.softPwmWrite(4,0)

wiringpi.pinMode(5,1)
wiringpi.softPwmCreate(5,0,100)
wiringpi.softPwmWrite(5,0)

wiringpi.pinMode(6,1)
wiringpi.softPwmCreate(6,0,100)
wiringpi.softPwmWrite(6,0)

def forward(speed):
    if speed >=100:
        speed=100
        wiringpi.softPwmWrite(1,0)
        wiringpi.softPwmWrite(4,speed)
        wiringpi.softPwmWrite(5,0)
        wiringpi.softPwmWrite(6,speed)
    elif speed<0:
        speed=abs(speed)
        wiringpi.softPwmWrite(1,speed)
        wiringpi.softPwmWrite(4,0)
        wiringpi.softPwmWrite(5,speed)
        wiringpi.softPwmWrite(6,0)
    #elif speed <=0:
    #    speed=0

#while 1:
#   forward(100)
#    print("testing")
#    time.sleep(0.15)