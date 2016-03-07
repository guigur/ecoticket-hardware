import os
import sys
import random

import PythonMagick

from PIL import Image
import pytesseract

class EcoTicket():
    ## Conf values
    # 0 -> Title
    # 1 -> Language
    conf_values = []

    ## Ticket data
    ticketData = ""

    ## Ticket tamp name
    ticketName = ""

    ## Define conf values from the conf file
    def parseConfFile(self):
        file = open('./parsing.conf')
        for line in file:
            self.conf_values.append(line.rstrip('\n'))
        file.close()
        return

    ## Convert pdf received to a png
    # args -> path/to/file.pdf
    # return -> name of the png file
    def pdf2png(self, pdf):
        img = PythonMagick.Image()
        img.density("300")
        img.read(pdf) # read in at 300 dpi
        pngname = str(random.getrandbits(32))
        img.write(pngname+".png")
        return pngname

    ## Perform OCR on the png ticket
    # args -> ticket png name (without extension)
    def doOcr(self, filename):
        self.ticketData = pytesseract.image_to_string(Image.open(filename+'.png'), lang = self.conf_values[1])
        return True

    def main(self):
        print ("Main : Start Parsing ...")
        ## Define conf values from the conf file
        self.parseConfFile()
        print ("Main : End Parsing ...")

        print ("Main : Start Converting ...")
        ## Convert pdf to png (for test purposes, "casino.pdf" is used)
        self.ticketName = self.pdf2png("casino.pdf")
        print ("Main : End Converting ...")

        print ("Main : Start OCR ...")
        ## Perform OCR on jpeg ticket
        self.doOcr(self.ticketName)
        os.remove(self.ticketName+".png")
        file = open(self.ticketName+".tmp", 'w')
        file.write(self.ticketData)
        file.close()

        ## Test sending file via beam
        os.system("python beam.py send file "+self.ticketName+".tmp")

        print ("Main : End OCR ...")
        return
