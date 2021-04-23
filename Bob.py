from serveur import key, chiffre
from Test import premier, cut, pgcd, pgcde
from Utilisateur import dechiffre
import numpy as np
import socket, sys

hote = '127.0.0.1'
port = 33000
k = key()


serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serveur.bind((hote,port))

except socket.error:
    print("La liaison avec Alice a échoué.")
    
print("Serveur prêt, en attente de requêtes ...")
serveur.listen(1)
connexion, adresse = serveur.accept()
print("Alice est connectée, adresse IP %s, port %s" % (adresse[0], adresse[1]))



msgServeur = "Vous êtes connecté avec Bob."
connexion.send(msgServeur.encode())
msgClient = connexion.recv(1024).decode()
while 1:
    print("Alice>")
    if msgClient.upper() == "FIN" or msgClient =="":
        break
    msgServeur = input("Bob> ")
    msgServeur = chiffre(k["priv"][0],k["priv"][1],msgServeur)
    ''.join(msgServeur)
    serveur.send(msgClient.encode())
    msgServeur = msgClient.recv(1024).decode()
    print(msgClient)
    msgClient = cut(msgClient, 2)
    msgClient = dechiffre(pub["pub"][0],pub["pub"][1],msgClient)
connexion.send("fin".encode())
print("Connexion interrompue.")
connexion.close()