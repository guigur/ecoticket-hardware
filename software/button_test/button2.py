from gpiozero import LED, Button
from signal import pause

#led = LED(17)
button = Button(4)

button.when_pressed = print "lol"
#button.when_released = led.off

pause()
