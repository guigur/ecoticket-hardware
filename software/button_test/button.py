from time import sleep
from gpiozero import Button

button1 = Button(4)
button2 = Button(17)
button3 = Button(22)

button1.wait_for_press()
button2.wait_for_press()
print "the button has been pressed"
