import socket, sys

hote = ''
port = 

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
    print("Serveur>", msgServeur)
    msgClient = input("Alice> ")
    serveur.send(msgClient.encode())
    msgServeur = serveur.recv(1024).decode()
    
print("Connexion interrompue.")
serveur.close()
