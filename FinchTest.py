from BirdBrain import Finch
import time

bird = Finch('A')

for i in range(0,10):
    bird.setBeak(100, 100, 100)
    time.sleep(1)
    bird.setBeak(0, 0, 0)
    time.sleep(1)
	
myFinch.stopAll()
