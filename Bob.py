import socket, sys
hote = ''
port = 
counter = 0

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serveur.bind((hote,port))

except socket.error:
    print("La liaison avec Alice a échoué.")
    
while 1:
    print("Serveur prêt, en attente de requêtes ...")
    serveur.listen(2)
    
    connexion, adresse = serveur.accept()
    counter +=1
    print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))
    
    msgServeur = " Vous êtes connecté au serveur Chiffrement RSA !"
    connexion.send(msgServeur.encode())
    msgClient = connexion.recv(1024).decode()
    while 1:
        print("Alice>", msgClient)
        if msgClient.upper() == "FIN" or msgClient =="":
            break
        msgServeur = input("Bob> ")
        connexion.send(msgServeur.encode())
        msgClient = connexion.recv(1024).decode()
    connexion.send("fin".encode())
    print("Connexion interrompue.")
    connexion.close()
    
    ch = input("<R>ecommencer <T>erminer ?")
    if ch.upper() == 'T':
        break