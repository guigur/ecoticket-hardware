Le code est a éxécuter OBLIGATOIREMENT sur un systeme linux.

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

Pour Node.js :
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install -y build-essential

Pour le BLE :
sudo apt-get install bluetooth bluez libbluetooth-dev libudev-dev

Le programme est à lancer en root mais en éxécutant cette commande vous pourrez le lancer en non-root (normalement) :
sudo apt-get install libcap2-bin
sudo setcap cap_net_raw+eip $(eval readlink -f `which node`)

---

MAJ 17/04/2016 : l'adresse MAC est récupérée automatiquement !
MAJ 25/05/2016 : nouveau parser + ajout du support du restaurant Le Comptoir (voir Setup)
MAJ 10/07/2016 : implémentation du BLE + nouveaux packages à installer + il faut lancer le programme en root

Setup :
Le parser ne fonctionne plus avec des fichiers de conf, on utilise désormais
un parser différent par commerce.
Commerces supportés :
	- Caisse en Ligne (pour tester)
	- Le Comptoir (restaurant de Bobby)
Le parser est le fichier ParserClass.py et celui par defaut et celui du Comptoir.
Si vous voulez changer de parser, il faut copier coller un des parsers disponibles
dans le dossier confs à la place du ParserClass.py à la racine du projet.

Instructions de lancement :
python Main.py
Selectionner la première option pour le QRCode (le NFC ne fonctionne pas encore)
Flasher le QRCode avec votre appli et tout doit se faire tout seul comme avec
l'appli Android (disponible sur le Drive)
Le programme ne se quitte pas tout seul, il faut le ctrl-c

---

Merci de ne pas modifier le code a part pour changer les valeur décrites
précédement (à savoir le nom du PDF).
Si vous remarqué un disfonctionnement ou quelque autre chose qui nécessite d'y
porter attention, merci de le dire.
