from time import sleep
from gpiozero import Button
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(22, GPIO.IN)

while True:
    if ( GPIO.input(4) == False ):
        print "button 1"
    if ( GPIO.input(17) == False ):
        print "button 2"
    if ( GPIO.input(22) == False ):
        print "button 3"
            
#button1.wait_for_press()

#print "the button has been pressed"
