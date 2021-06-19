"""
sudo apt-get update
sudo apt-get install rpi.gpio
"""

import RPi.GPIO as GPIO
import time

dirA1 = 29
dirA2 = 31
spdA = 33

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
GPIO.setup(dirA1,GPIO.OUT)
GPIO.setup(dirA2,GPIO.OUT)
GPIO.setup(spdA,GPIO.OUT)
GPIO.output(dirA1,GPIO.LOW)
GPIO.output(dirA2,GPIO.LOW)
pwmA=GPIO.PWM(spdA,1000) #freq
pwmA.start(25)

GPIO.output(dirA1,GPIO.HIGH)
GPIO.output(dirA2,GPIO.LOW)
pwmA.ChangeDutyCycle(25)


time.sleep(5)
#Always at the end of the code
GPIO.cleanup()  

