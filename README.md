# ecoticket-hardware
This is the hardware part of the **Ecoticket** system.
In this repot, you will find the schematics, the gerbers files, the proteus project and some code 
### Hardware
The **Ecoticket** *alpha* is based arround the **Raspberry PI**. 
The PCB is 10x10 cm and plugs directly on the PI.
Keep in mind it's just an alpha.
## TODO LIST
The ethernet interfaces on the Alpha does not work
The NRF51822 is not connected to the Raspberry PI
The crystals footprints are mirrored
The TX and RX lines are reversed
The footprint of the Raspberry PI is also mirrored
The holes are not drilled
### 3D render
![the ecoticket main view](/PCB/Realease%20alpha/pcb_alpha_front_w_pi.png "render")
### Here is the schematics
![the ecoticket main view](/PCB/pre-beta/Schematics/misc.bmp "Main view")
![serial debug](/PCB/pre-beta/Schematics/ftdi.bmp "the serial debug")
![PN532 nfc interface](/PCB/pre-beta/Schematics/nfc.bmp "the nfc interface")
![ENC28J60 ethernet interfaces](/PCB/pre-beta/Schematics/ethernets.bmp "the 2 ethernet interface")

### And the gerber files preview
![the ecoticket alpha](/PCB/Realease%20alpha/pcb%2018.03.16.PNG "The gerber viewer")
