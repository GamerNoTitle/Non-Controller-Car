import distance
import time
import ../acc/acc as mv
s=0.0
while 1:
    distance()
    if s<=80 and s>50:
        mv.forward(50)
    elif s<=50 and s>30:
        mv.forward(30)
    elif s<=30:
        mv.forward(0)
    elif s>80
        mv.forward(100)
    time.sleep(0.2)