
from smartGPIO import GPIO
from lib_tft144 import TFT144
from time import sleep



if GPIO.RPI_REVISION == 0:   # VIRTUAL-GPIO
    RST =  8
    CE =  10    # VirtGPIO: the chosen Chip Select pin#. (different from rpi)
    DC =   9
    LED =  7
    spi = GPIO.SpiDev()
    # the virtual GPIO module directly supports spidev function

else:   # RPI
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    RST = 25    # RST may use direct +3V strapping, and then be listed as 0 here. (Soft Reset used instead)
    CE =   0    # RPI GPIO: 0 or 1 for CE0 / CE1 number (NOT the pin#)
    DC =  24    # Labeled on board as "A0"   Command/Data select
    LED = 23    # LED may also be strapped direct to +3V, (and then LED=0 here). LED sinks 10-14 mA @ 3V
    import spidev
    spi = spidev.SpiDev()

TFT = TFT144(GPIO, spi, CE, DC, RST, LED, TFT144.ORIENTATION90, isRedBoard=False)
# TFT = TFT144(GPIO, spi, CE, DC)     # the minimalist version

posx=0
posy=0

TFT.draw_bmp("depth1.bmp")
#"img_128x/ecoticket_logo_128x.bmp")
sleep(10)

print ("Rectangle")
TFT.draw_filled_rectangle(0,0,50,50 ,TFT.RED)
#TFT.draw_filled_rectangle(0,64,128,128,TFT.BLACK)
#for i in range (4,32,4):
 #  TFT.draw_rectangle(i,i,128-i,64-i,TFT.colour565(i-1,i-1,i-1))
sleep(10)
#print ("Line:")
TFT.draw_line(0,0,128,128,TFT.GREEN)
TFT.draw_line(0,128,128,0,TFT.GREEN)

print ("Circles:")
TFT.draw_circle(64,64,63,TFT.BLUE)
TFT.draw_circle(64,64,53,TFT.BLUE)
TFT.draw_circle(64,64,43,TFT.BLUE)
TFT.draw_circle(64,64,33,TFT.BLUE)

