import EcoticketClass

#os.system("sudo hciconfig hci0 noleadv")
#os.system("sudo hciconfig hci0 leadv 0")
os.system("sudo hciconfig hci0 piscan")
os.system("sudo sdptool add SP")

eco = EcoticketClass.EcoTicket()
eco.main()
