# -*- coding: utf-8 -*-
import re

class Parser():

    conf_values = ["Le Comptoir", "fra", "Restaurant", 20, "TOTAL", "[x]]"]
    cleaned = []
    parsed = []

    def getConf(self):
        return self.conf_values

    # Call this function in EcoticketClass.py
    def parseFile(self, filename, conf_values, date, ShopName):
        # Clean file and keep only articles and prices in cleaned[]
        self.cleanFile(filename, conf_values[3], conf_values[4])
        # Parse cleaned[] and put results in parsed[]
        total = self.doParsing(conf_values[5], date, ShopName)
        # Create and fill file
        self.makeFile(filename)
        return total

    def cleanFile(self, filename, j, eof):
        i = 0
        f = open(filename, 'r')
        line = f.readline()

        while line:
            if (line.rstrip('\n') == "Tva"):
                break
            elif (i > int(j)):
                self.cleaned.append(line)
            line = f.readline()
            i += 1
        f.close()

    def doParsing(self, delimiters, date, ShopName):
        i = 0
        j = 1
        last1 = 0
        last2 = 99
        last3 = 99
        tmp_product = ""
        tmp_quantity = ""
        self.parsed.append("----\n")
        for line in self.cleaned:
            if (line.rstrip('\n') == "TTC 1"):
                break
            if (line != '\n' and i == 0):
                tmp_product = line.rstrip('\n')
                last1 = i
            if (line != '\n' and i == 1):
                tmp_product = tmp_product + " " + line.rstrip('\n')
                last1 = i
            if (line != '\n' and i == (last1 + 2)):
                quantity = line.rstrip('\n')
                quantity = quantity.replace(',00', '')
                tmp_quantity = quantity
                last2 = i
            if (line != '\n' and i == (last2 + 4)):
                price = line
                price = price.replace(',', '.')
                self.parsed.append(tmp_quantity + ' X ' + tmp_product + '____' + price)
                last3 = i
                j+=1
            if (i == (last3 + 3)):
                i = 0
                last1 = 0
                last2 = 99
                last3 = 99
            else:
                i += 1
        i = 0
        tmp = 0
        total = ""
        for line in self.cleaned:
            if (line.rstrip('\n') == "TTC 3"):
                tmp = 1
            if (tmp == 1):
                i+=1
            if (i == 3):
                total = line.rstrip('\n')
                total = total.replace(',', '.')
                self.parsed.append("TOTAL____" + total + "\n")
                self.parsed.append("----\n")
		# Append total a the beginning of txt file
		totall = total.replace('.', '-')
        	totall = total.rstrip('\n')
        	totall = total.rstrip('€')
		self.parsed = self.parsed[:1] + [date + '_' + total + '_' + ShopName] + self.parsed[1:]
		break
        return total

    def makeFile(self, filename):
        file = open(filename, 'w')
        file.writelines(self.parsed)
        file.close()
