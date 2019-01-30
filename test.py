import wiringpi
import time
while 1:
    wiringpi.softPwmWrite(4,100)
    print("testing")
    time.sleep(0.15)