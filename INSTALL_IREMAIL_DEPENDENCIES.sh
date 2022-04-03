#!/bin/bash
#seule dépendance d'iredmail
clear
wget https://github.com/iredmail/iRedMail/archive/1.5.2.tar.gz

tar xvf /root/scripts/1.5.2.tar.gz

cd iRedMail-1.5.2

chmod a+x iRedMail.sh

bash iRedMail.sh
