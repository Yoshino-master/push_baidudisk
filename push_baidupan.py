import time, random
from pymouse import *
from pykeyboard import *

m = PyMouse()
maxh, maxw, maxinterval = 500, 500, 10

duration = float(input("Input the time you want to run this program:"))
start = time.time()
t = start
while(t - start < duration):
    m.move(int(random.random()*maxh), \
           int(random.random()*maxw))
    time.sleep(random.random()*maxinterval)
    t = time.time()
