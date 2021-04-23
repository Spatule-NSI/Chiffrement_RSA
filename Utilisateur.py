def dechiffre(n, d, *crypt):
    """ `*crypt` est une liste des blocks à déchiffrer"""
    #dechiffrage des blocs
    resultat = [str((int(i)**d)%n) for i in crypt]
        
    #on rajoute les 0 en debut de blocs pour refaire des blocs de 4
    for i, s in enumerate(resultat):
        if len(s) < 4:
            while len(s) < 4:
                s = '0' + s
            resultat[i] = s
        
    #on refait des groupes de 3 et on les convertie directement en ascii
    g = ''.join(resultat)
    asci = ''
    d , f = 0 , 3
    while f < len(g):
        asci = asci + chr(int(g[d:f])) #conversion ascii
        d , f = f , f + 3
    return asci