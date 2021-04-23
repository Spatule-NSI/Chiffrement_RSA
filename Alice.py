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
    serveur.connect((hote, port))

except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("Connexion établie avec Bob.")



msgServeur = serveur.recv(1024).decode()

while 1:
    if msgServeur.upper() == "FIN" or msgServeur =="":
        break
    if msgServeur == "Vous êtes connecté avec Bob.":
        print("Bob>",msgServeur)
    else:
        print("Bob>")
    msgClient = input("Alice> ")
    msgClient = chiffre(k["priv"][0],k["priv"][1],msgClient)
    ''.join(msgClient)
    serveur.send(msgClient.encode())
    msgServeur = serveur.recv(1024).decode()
    print(msgServeur)
    msgServeur = cut(msgServeur,2)
    msgServeur = dechiffre(pub["pub"][0],pub["pub"][1],msgServeur)
print("Connexion interrompue.")
serveur.close()