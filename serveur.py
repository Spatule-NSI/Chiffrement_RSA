import numpy as np
from Test import premier, pgcd, pgcde
from Utilisateur import dechiffre

def key():   #1
    
    """retourne un dictionnaire contenant la clé privée et la clé publique sous forme de tuples: {priv:(clé privée),pub:(clé publique)}"""
    
    #choix au hasard de deux entiers premiers (n et q)
    p = np.random.choice(1000,1)
    q = np.random.choice(1000,1)
    
    while premier(p) is False:
        p = np.random.choice(1000,1)
    while premier(q) is False:
        q = np.random.choice(1000,1)
        
    #calcul de n et m
    n = p*q
    m = (p-1)*(q-1)
    
    #recherche de c premier de m (c'est a dire tel que pgcd(m,c)=1 ) et de d = pgcde(m,c) tel que 2 < d < m
    r = 10
    d = 0
    while r != 1 or d <= 2 or d >= m:
        c = np.random.choice(1000,1)
        r, d, v = pgcde(c,m)
    n, c, d = int(n), int(c), int(d)
    return {"priv":(n,c), "pub":(n,d)}

def chiffre(n, c, msg):
    #conversion du message en codes ascii   
    asc = [str(ord(j)) for j in msg]
    
    #ajout de 0 pour avoir une longueur fixe (3) de chaque code asccii
    for i, k in enumerate(asc):
        if len(k) < 3:      
            while len(k) < 3:
                k = '0' + k
            asc[i] = k
    
    #formation de blocs de taille inferieure a n (ici blocs de 4)
    ascg = ''.join(asc)
    d , f = 0 , 4
    while len(ascg)%f != 0:        #on rajoute eventuellement des 0 a la fin de ascg de maniere a ce que len(ascg) soit un multiple de f
        ascg = ascg + '0'
    l = []
    while f <= len(ascg):
        l.append(ascg[d:f])
        d , f = f , f + 4
    #chiffrement des groupes
    crypt = [str(((int(i))**c)%n) for i in l]
    return crypt
