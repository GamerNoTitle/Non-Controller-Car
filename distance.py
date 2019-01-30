import wiringpi
import time
def dis():
    wiringpi.digitalWrite(28,0)
    t1=time.time()  
    time.sleep(0.00015)
    wiringpi.digitalWrite(28,1)
    while not wiringpi.digitalRead(29):
        t_n=time.time()
        if (t_n - t1)>=0.1:
            break
    while wiringpi.digitalRead(29):
        t_n=time.time()
        if (t_n - t1)>=0.1:
            break
    t2=time.time()
    s=(t2-t1)*34000/2
    print (s)
    return s
wiringpi.wiringPiSetup()
wiringpi.pinMode(28,1)
wiringpi.pinMode(29,0)
#while 1:
#    dis()
#    time.sleep(0.1)