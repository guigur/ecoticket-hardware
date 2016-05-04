import RPi.GPIO as GPIO
import time
from PIL import Image
from time import sleep

class TFT_display:
	SCLK = 21
	SDAT = 20
	DC = 6
	RESET = 26
	BACKLIGHT = 5
	CS = 16
	pins = [SCLK, SDAT, DC, RESET, BACKLIGHT, CS]
	storedBitmap = []
	#RGB888 Color constants
	BLACK = 0x000000
	RED = 0xFF0000
	GREEN = 0x00FF00
	BLUE = 0x0000FF
	WHITE = 0xFFFFFF
	COLORSET = [RED,GREEN,BLUE,WHITE]
	#Screen dimentons
	COL = 128
	ROW = 128
	COLSTART = 1
	ROWSTART = 0

	#ST7735 commands
	SWRESET = 0x01 #software reset
	SLPOUT = 0x11 #sleep out
	DISPON = 0x29 #display on
	CASET = 0x2A #column address set
	RASET = 0x2B #row address set
	RAMWR = 0x2C #RAM write
	MADCTL = 0x36 #axis control
	COLMOD = 0x3A #color mode

	########################################################################
	#
	# Low-level routines
	# These routines access GPIO directly
	########################################################################
	def SetPin(self,pinNumber,value):
		GPIO.output(pinNumber,value)

	def InitIO(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		for pin in self.pins:
			GPIO.setup(pin,GPIO.OUT)
		GPIO.output(self.RESET, 0)
		sleep(0.05);
		GPIO.output(self.RESET, 1)
		GPIO.output(self.SCLK, 0)

		GPIO.output(self.BACKLIGHT, 1)
	  
	   # p = GPIO.PWM(BACKLIGHT, 50)  # channel=12 frequency=50Hz
		# p.start(0)
		#GPIO.output(CS, 0)
		
	def BacklightPulse(self):
		for dc in range(0, 101, 5):
			p.ChangeDutyCycle(self.dc)
			time.sleep(0.1)
		for dc in range(100, -1, -5):
			p.ChangeDutyCycle(self.dc)
			time.sleep(0.1)
	########################################################################
	#
	# Bit-Banging (software) SPI routines:
	# TODO: delete this code and use true SPI
	#
	#
	def PulseClock(self):
		#pulses the serial clock line HIGH
		self.SetPin(self.SCLK,1) #bit clocked on low-high transition
		self.SetPin(self.SCLK,0) #no delay since python is slow
	def WriteByte(self,value, data=True):
		"sends byte to display using software SPI"
		mask = 0x80 #start with bit7 (msb)
		self.SetPin(self.DC,data) #low = command; high = data
		for b in range(8): #loop for 8 bits, msb to lsb
			self.SetPin(self.SDAT,value & mask) #put bit on serial data line
			self.PulseClock() #clock in the bit
			mask >>= 1 #go to next bit
	def WriteCmd(self,value):
		"Send command byte to display"
		self.WriteByte(value,False) #set D/C line to 0 = command
	def WriteWord (self,value):
		"sends a 16-bit word to the display as data"
		self.WriteByte(value >> 8) #write upper 8 bits
		self.WriteByte(value & 0xFF) #write lower 8 bits
	def WriteList (self,byteList):
		"Send list of bytes to display, as data"
		for byte in byteList: #grab each byte in list
			self.WriteByte(byte) #and send it
	def Write888(self,value,reps=1):
		"sends a 24-bit RGB pixel data to display, with optional repeat"
		red = value & 0xFF #red = upper 8 bits
		green = (value>>8) & 0xFF #green = middle 8 bits
		blue = value>>16 & 0xFF #blue = lower 8 bits
		RGB = [red,green,blue] #assemble RGB as 3 byte list
		for a in range(reps): #send RGB x optional repeat
			self.WriteList(RGB)

	########################################################################
	#
	# ST7735 driver routines:
	#
	#
	def InitDisplay(self):
		"Resets & prepares display for active use."
		self.WriteCmd (self.SWRESET) #software reset, puts display into sleep
		time.sleep(0.2) #wait 200mS for controller register init
		self.WriteCmd (self.SLPOUT) #sleep out
		time.sleep(0.2) #wait 200mS for TFT driver circuits
		self.WriteCmd (self.DISPON) #display on!
	def SetAddrWindow(self,x0,y0,x1,y1):
		"sets a rectangular display window into which pixel data is placed"
		self.WriteCmd(self.CASET) #set column range (x0,x1)
		self.WriteWord(x0)
		self.WriteWord(x1)
		self.WriteCmd(self.RASET) #set row range (y0,y1)
		self.WriteWord(y0)
		self.WriteWord(y1)
	def DrawPixel(self,x,y,color): #BLUE GREEN RED
		"draws a pixel on the TFT display"
		self.SetAddrWindow(x,y,x,y)
		self.WriteCmd(self.RAMWR)
		self.Write888(color)
	def FillRect(self,x0,y0,x1,y1,color):
		"fills rectangle with given color"
		width = x1-x0+1
		height = y1-y0+1
		self.SetAddrWindow(x0,y0,x1,y1)
		self.WriteCmd(self.RAMWR)
		self.Write888(color,width*height)
	def FillScreen(self,color):
		"Fills entire screen with given color"
		self.FillRect(self.COLSTART,self.ROWSTART,self.COL + self.COLSTART,self.ROW + self.ROWSTART,color)
	def ClearScreen(self):
		"Fills entire screen with black"
		self.FillRect(self.COLSTART,self.ROWSTART,self.COL + self.COLSTART,self.ROW + self.ROWSTART, self.RED)
	   

	def StoreBMP(self,x0, y0, x1, y1):
		im = Image.open("test.png")
		height = x1 + x0
		width = y1 + y0
		x = x0
		y = y0
		while (y < height):
			while (x < width):
				r, g, b = im.getpixel((x, y))
				self.storedBitmap.append(r)
				self.storedBitmap.append(g)
				self.storedBitmap.append(b)
				x = x + 1
			x = x0
			y = y + 1

	def DisplayBMP(self,imgd,x0, y0, x1, y1):
		multi = 0
		count = 0
		height = x1 + x0
		width = y1 + y0
		x = x0
		y = y0
		img = Image.open("qrcodes.bmp")
		while (y < height):
			while (x < width):
                                r, g, b = img.getpixel((x, y))
				#r = img[count*multi]
				#g = img[count*multi+1]
				#b = img[count*multi+2]
				self.SetAddrWindow(x,y,x,y)
                                self.WriteCmd(self.RAMWR)
				self.Write888((r << 16) + (g << 8) + b)
				x = x + 1
				count = count + 1
				multi = 3
			x = x0
			y = y + 1

	########################################################################
	#
	# Testing routines:
	#
	#
	def TimeDisplay(self):
		"Measures time required to fill display twice"
		#startTime=time.time()
		#print " Now painting screen GREEN"
		#FillScreen(GREEN)
		#print " Now clearing screen"
		
		#elapsedTime=time.time()-startTime
		#print " Elapsed time %0.1f seconds" % (elapsedTime)
		

	########################################################################
	#
	# Main Program
	#
	def main(self):
                print "hello"
		self.InitIO()
		self.InitDisplay()
		self.ClearScreen()
		#self.StoreBMP(0, 0, 128, 128)
		#self.DisplayBMP(img, 0, 0, 128, 128)
	# END ###############################################################
