# Sega-SokhnaProject
	Environnemment technique: 
	-- 2 machines Ubuntu (20.04) et 1 machine Kali Linux (20.04)
	-- Fixation des adresses IP grâce à netplan ( /etc/netplan/)
	-- Machine serveur: installation des paquets bind9 pour le DNS et isc-dhcp-server pour le DHCP
	-- Machine Kali linux : installation du paquet ufw
![image](https://user-images.githubusercontent.com/99363547/161441647-3c5c3f20-3b9a-4823-9047-e8a52232b1bf.png)

	1)Partie 01
	-- Explication du script Install_MYSQL_DEPENDENCIES.sh : il faut donner les droits d'execution au script (chmod a+x) , puis l'executer ./(nom_script)
	-- Explication du script Install_IREDMAIL_DEPENDENCIES.sh : il faut donner les droits d'execution au script (chmod a+x) , puis l'executer ./(nom_script).Cela installera IREDMAIL 1.5.2
![image](https://user-images.githubusercontent.com/99363547/161440942-a6ff7e28-2f08-493a-ac1d-478ad822ba07.png)




-- Analyse des paquets avec Wireshark :

      	1.1)Filtrage: Protocole UDP seulement
    -Pour le protocole UDP nous avons le service DNS qui peut utiliser TCP ou UDP port 53
    -Il y a des échanges de questions DNS entre le serveur DNS (192.168.10.1) et le client (192.168.10.3)
    -C'est pour cela le port source est 46576 (client) et celui de destination est le port 53.
	  -Analyse du datagramme:
	     L'entête d'un datagramme UDP contient quatre champs
	          -Source port : port source qui est le client
	          -Destination Port : port dest qui 
	          -Length : longueur totale du segment UDP 66 Octets
	          -CheckSum: celle-ci permet de s'assurer de l'intégrité du paquet reçu.
![image](https://user-images.githubusercontent.com/99363547/161439560-0849eff3-84c6-4fac-8a91-34a1af9f592f.png)


      1.2)Filtrage(udp.port == 53 || tcp.port == 53) ou bootp 
			-Pour ce type de filtrage nous notons principalement le protocol DHCP qui utilise le port 68 UDP (source) et le port 67 UDP (destination).Il ya des 		échanges    de requêtes DHCP entre la machine cliente et la machine serveur(192.168.10.1)
  	-La premiere trame est de DHCPRequest (broadcast) qui part du client vers le serveur à la suite d'un dhclient -v au niveau du client.Le client accepte          accepte l'offre du serveur et demande sa configuration
	          Source (0.0.0.0) --> Destination (255.255.255.255)
  	-La deuxieme trame est le DHCPACK(unicast) qui part du serveur vers le client.Ici le serveur répond avec l'adresse IP octroyée et les options
	Source-Serveur(192.168.10.1)-->Destination-Serveur(192.168.10.3)
![image](https://user-images.githubusercontent.com/99363547/161440718-1e5d67ad-52d2-466d-8474-494d9fc867ee.png)

	

      1.3)Filtrage Protocole TCP seulement
  	Frame 808: 78 bytes on wire (624 bits), 78 bytes captured (624 bits) on interface eth0, id 0
  	Internet Protocol Version 4, Src: 192.168.10.4, Dst: 192.168.10.1 Question DNS entre le client et le serveur avec le flag SYN
  	Structure d'un segment TCP:Transmission Control Protocol, Src Port: 49338, Dst Port: 53, Seq: 0, Len: 0
    	Source Port: 49338
    	Destination Port: 53
    	Sequence number: 0    (relative sequence number)
    	Sequence number (raw): 2099954149 : numéro de séquence du premier octet de données
    	[Next sequence number: 1    (relative sequence number)]
    	Acknowledgment number: 0 : concerne le flag ACK
    	Acknowledgment number (raw): 0
    	1011 .... = Header Length: 44 bytes (11)
    	Flags: 0x002 (SYN)

    
  	1.4) Autorisation des trafics avec ufw
  	Nous avons autorisée le trafic HTTP/S , SSH, DNS avec le port 53 et DHCP avec les ports 68 et 67 entrant et venant des addresses IP 192.168.10.1 jusqu'à       	192.168.10.10 .
![image](https://user-images.githubusercontent.com/99363547/161440779-5956b1f3-3af5-40c2-863a-bff045791886.png)

	
	
	
------------------------------------------------------------------------------------------------------------------------------------------------------------		
    

