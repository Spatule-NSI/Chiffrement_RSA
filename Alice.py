from serveur import key, chiffre
import socket, sys

HOST = '127.0.0.1'
PORT = 33000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serveur.connect((HOST, PORT))

except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("Vous êtes connecté avec Bob.")

msgServeur = mySocket.recv(1024).decode()

while 1:
    if msgServeur.upper() == "FIN" or msgServeur =="":
        break
    print("Serveur>", msgServeur)
    msgClient = input("Client> ")
    msgClient = chiffre(k["priv"][0],k["priv"][1],msgClient)
    serveur.send(str(msgClient).encode())
    msgServeur = serveur.recv(1024).decode()
    
print("Connexion interrompue.")
serveur.close()
