import RPi.GPIO as GPIO
import time

dirA1 = 5


GPIO.cleanup()  
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dirA1,False)
 
while(1):
    GPIO.output(dirA1,True)
    time.sleep(5)
    GPIO.output(dirA1,False)
    time.sleep(5)


#Always at the end of the code
GPIO.cleanup()  

