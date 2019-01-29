import wiringpi
import time

def dis():
    wiringpi.wiringPiSetup()
    wiringpi.digitalWrite(28,0)
    t1=time.time()
    time.sleep(1)
    wiringpi.digitalWrite(28,1)
    t2=time.time()
    s=(t2-t1)*340/2
    print (s)
while 1:
    dis()