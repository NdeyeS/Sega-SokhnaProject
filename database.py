import os

import mysql.connector  as db

#from mariadb import Error

import sys
#Connexion à la base de données 
def ConnectDB():
    try:
        con = db.connect(
           host='localhost',
           database='project',
           user='root',
           password='passer')
        print("Base de données connectee")
        return con

    except db.Error as e:
        print(f"Erreur lors de la connexion : {e}")
        return False
        sys.exit(1)

#Creation d'un compte avec verification du mail
def Account(Liste: list):
    try:
        con = ConnectDB()
        cur = con.cursor()
        cur.executemany("INSERT INTO user VALUES('Liste[0]','Liste[1]','Liste[2]','Liste[3]')")
        con.commit()
        if (Liste[2]in(cur.execute("SELECT mail FROM user"))):
             print("Mail deja present")
        else:
            print("Donnees inserees avec succes")
    except db.Error as e:
        print(f"Erreur lors de l'insertion:{e}")


#Fonction qui permet qu'un utilisateur se connecte à son compte
def Login(Liste:list)-> list:
    try:
        con = ConnectDB()
        cur = con.cursor()
        cur.execute("SELECT * from user where mail = '{Liste[2]}' AND password = '{Liste[3]}'")
    except db.Error as e:
        print("Indentifiants Invalides")
