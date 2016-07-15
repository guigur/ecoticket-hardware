echo "Installing node ..."
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
apt-get install -y nodejs
apt-get install -y build-essential
pip install Naked
echo "Done"

echo "Installing WatchDog ..."
pip install watchdog
echo "Done !"

echo "Installing QRCode ..."
tar -xvf qrcode-5.3.tar.gz
cd qrcode-5.3
python setup.py install
cd ..
echo "Done !"

echo "Install CUPS ..."
apt-get install cups-pdf
lpadmin -p cups-pdf -v cups-pdf:/ -E -P /usr/share/ppd/cups-pdf/CUPS-PDF.ppd
lpoptions -d cups-pdf
mkdir ~/PDF
touch ~/PDF/tmp.pdf
echo "Done !"

cd ../js

echo "Installing bluetooth ..."
apt-get install bluetooth libbluetooth-dev
pip install pybluez
npm init
npm install uuid
npm install bleno
npm install bluetooth-hci-socket
echo "Done !"

