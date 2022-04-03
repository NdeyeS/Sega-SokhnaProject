!/bin/bash
apt install wget #seule dépendance d'iredmail
wget https://github.com/iredmail/iRedMail/archive/1.5.2.tar.gz
cd /root/scripts
tar xvf /root/scripts/1.5.2.tar.gz
cd iRedMail-1.5.2
chmod a+x iRedMail.sh
bash iRedMail.sh
