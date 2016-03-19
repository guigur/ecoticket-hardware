# ecoticket-harware
This is the harware part of the Ecoticket system.
In this repot, you will found the schematics, the gerbers files, the proteus project and some code 
## Hardware
The ecoticket *alpha* is based arround the **Raspberry PI**. 
The PCB is 10x10 cm and plugs directly on the PI.
Keep in mind it's just an alpha.

### Here is the schematics
![the ecoticket main view](/PCB/Schematics/PNG/otherthings.png "Main view")
![serial debug](/PCB/Schematics/PNG/ft232rl.png "the serial debug")
![PN532 nfc interface](/PCB/Schematics/PNG/nfc.png "the nfc interface")
![ENC28J60 ethernet interfaces](/PCB/Schematics/PNG/ethernet interface.png "the 2 ethernet interface")

### And the gerber files preview
![the ecoticket alpha](/PCB/pcb%2018.03.16.PNG "The gerber viewer")

## Program for the NRF51822 (BT module)
This part is empty for now

## Program for the ENC28J60
The Ecoticket's Hardware use 2 ENC28J60 chips. They act like ethernet interface thru the SPI bus.
This part is also empty
