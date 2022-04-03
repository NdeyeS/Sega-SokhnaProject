import socket
import time
import json
import database
Liste = []

def openServer(host,
               port,
               buffer=2048):
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind(('', port))  # Écoute sur le port 50000
    serveur.listen(5)
#Récupération infos clients lors d'une création de compte
    while True:
        client, infosClient = serveur.accept()
        print("Client connecté. Adresse " + infosClient[0])
        req = ("Veuillez choisir une action svp :")
        (" S'il s a agit d une création de compte tapez 1, ou tapez 2 s'il s'agit d une connexion")
        client.send(req.encode("utf-8"))
        inf = client.recv(buffer)
        if (inf.decode("utf-8") == 1):

            req = ("Veuillez entrer votre nom svp : ") 
            client.send(req.encode("utf-8"))
            inf = client.recv(buffer)
            Liste.append(inf.decode("utf-8"))


            req = ("Veuillez entrer votre prenom svp : ") 
            client.send(req.encode("utf-8"))
            inf = client.recv(buffer)
            Liste.append(inf.decode("utf-8"))

            req = (("Veuillez entrer votre mail svp : ")) 
            client.send(req.encode("utf-8"))
            inf = client.recv(buffer)
            Liste.append(inf.decode("utf-8"))

            req1 = (("Veuillez entrer votre mot de passe svp : ")) 
            client.send(req1.encode("utf-8"))
            inf1 = client.recv(buffer)
            Liste.append(inf1.decode("utf-8"))

            req2 = (("Veuillez  confirmer votre mot de passe svp : ")) 
            client.send(req2.encode("utf-8"))
            inf2 = client.recv(buffer)
            while inf1 != inf2 :
                    print("Les mots de passes ne sont pas identiques")
            Liste.append(inf1.decode("utf-8"))

            if database.Account(Liste) == True:
                client.send((("Compte créee")).encode("utf-8"))
            else:
                client.send((("Erreur aux niveaux des champs")).encode("utf-8"))
#Récupération des identifiants   
        while True:
            if((inf.decode("utf-8")) == 2):

                reqA = (("Veuillez entrer votre adresse mail svp : ")) 
                client.send(reqA.encode("utf-8"))
                infA = client.recv(buffer)
                Liste.append(infA.decode("utf-8"))


                reqB =(("Veuillez entrer votre mot de passe svp : ")) 
                client.send(reqB.encode("utf-8"))
                infB = client.recv(buffer)
                Liste.append(infB.decode("utf-8"))

            if database.Login(Liste) == True:
                client.send((("Bienvenue")).encode("utf-8"))
            else:
                client.send(("Erreur aux niveaux des champs")).encode("utf-8")

    serveur.close()

if __name__ == "__main__":
    
    openServer('192.168.10.2', 50000)
     
