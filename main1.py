import distance
import time
import motion as mv
s=0.0
while 1:
    s=distance.dis()
    if s<=80 and s>50:
        speed=int(distance.dis()*0.9)
        mv.forward(speed)
    elif s<=50 and s>30:
        speed=int(distance.dis()*0.5)
        mv.forward(speed)
    elif s<=30:
        mv.forward(0)
        break
    elif s>80:
        mv.forward(100)
    time.sleep(0.2)