Le code est a éxécuter OBLIGATOIREMENT sur un systeme linux.

Le PDF de test fourni est test3.pdf, le nom de ce PDF est harcoded dans
EcoticketClass.py (vous pouvez changer le PDF de test mais dans ce cas là il
faut penser a modifier le nom).

A savoir que contrairement à la précédente version je n'utilise pas d'OCR
mais une fonction built-in de linux qui me permet de lire les data du fichier
PDF directement. Cela signifie que le programme ne fonctionnera pas si vous
utilisez un ticket de caisse scanné en PDF. Vous devez utiliser un ticket
imprimé en PDF.
Personnelement j'ai généré le ticket fourni à l'aide d'un logiciel de caisse
en ligne :
http://caisse.enregistreuse.fr/

---

Les installations a effectuer sont les suivantes (il se peut que j'en ai
oublié, si tel est le cas merci de me le dire) :

Pour le bluetooth :
sudo apt-get install bluetooth libbluetooth-dev
sudo pip install pybluez

Pour le QRCode :
https://pypi.python.org/pypi/qrcode

Pour Rapspberry PI:
-sudo sdptool add SP
-Edit /lib/systemd/system/bluetooth.service and add "-C" after "bluetoothd"
-Reboot

---

MAJ 17/04/2016 : l'adresse MAC est récupérée automatiquement !

Instructions de lancement :
python Main.py
Selectionner la première option pour le QRCode (le NFC ne fonctionne pas encore)
Flasher le QRCode avec votre appli et tout doit se faire tout seul comme avec
l'appli Android (disponible sur le Drive)
Le programme ne se quitte pas tout seul, il faut le ctrl-c

---

Merci de ne pas modifier le code a part pour changer les valeur décrites
précédement (à savoir le nom du PDF et l'adresse mac).
Si vous remarqué un disfonctionnement ou quelque autre chose qui nécessite d'y
porter attention, merci de le dire.
