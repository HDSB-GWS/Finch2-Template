from BirdBrain import Finch
import time

myFinch = Finch('A')

myFinch.resetEncoders()


for i in range(0,10):
    print("Right wheel rotations: ", myFinch.getEncoder('R'))
    print("Left wheel rotations: ", myFinch.getEncoder('L'))  
    print("Compass Heading: ", myFinch.getCompass())    
    print("Magnetic Field: ", myFinch.getMagnetometer()) 
    # print("Sound: ", myFinch.getSound())   
    # print("Temperature: ", myFinch.getTemperature())                                     
    myFinch.setBeak(100, 100, 100)
    myFinch.setMotors(-50,50)
    time.sleep(1)
    myFinch.setBeak(0, 0, 0)
    myFinch.stop()
    time.sleep(1)
	
myFinch.stopAll()
