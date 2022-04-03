import json
import socket
import datetime

def openClientTunnel(host,
                     port,
                     buffer=4096):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host, port))
    print("Connexion au serveur de projet")
    print(f'Connexion faite à: {datetime.datetime.now()}')
    print(f'Connexion faite via le port: {port} à l\'adresse: {host}')
    req = 0
    
    while True:
        reponse = client.recv(buffer)
        print(reponse.decode("utf-8"))
        req = input("")
        client.send(req.encode("utf-8"))
#Si le client souhaite créer un compte
        if req == "1":
            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix = str(input(""))
            client.send(choix.encode("utf-8")) #nom

            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix = str(input(""))
            client.send(choix.encode("utf-8")) #prenom

            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix = str(input(""))
            client.send(choix.encode("utf-8"))# mail

            reponse1 = client.recv(buffer)
            print(reponse1.decode("utf-8"))
            choix1 = str(input(""))
            client.send(choix1.encode("utf-8"))#password

            reponse2 = client.recv(buffer)
            print(reponse2.decode("utf-8"))
            choix2= str(input(""))
            client.send(choix2.encode("utf-8"))#passwordconfirme

            while reponse1 != reponse2 :
                    print("Les mots de passes ne sont pas identiques")
        client.close()
        print("Connexion fermée")
#Le client entre ses identifiants
        if req == "2":
            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix = str(input(""))
            client.send(choix.encode("utf-8")) #mail

            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            choix = str(input(""))
            client.send(choix.encode("utf-8")) #password
        client.close()
        print("Connexion fermée")
if __name__ == '__main__':
    openClientTunnel("192.168.10.1", 50000)

            
