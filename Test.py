import numpy as np

def premier(n):
    
    """retourne True si n est premier, False dans le cas contraire.
    n doit etre un entier"""
    
    if n == 1 or n == 2:
        return True        
    if n%2 == 0:
        return False
    r = n**0.5
    if r == int(r):
        return False
    for x in range(3, int(r), 2):
        if n % x == 0:
            return False    
    return True

def cut(k, long):
    
    """"découpe des blocs de longueur `long` dans une chaine de caractères k et retourne une liste des blocs"""
    
    d = 0
    f = long
    l = []
    while f <= len(k):
        l.append(k[d:f])
        d = f
        f = f + long
    m = len(k)%long
    if m != 0:
        l.append(k[len(k)-m:])
    return l

def pgcd(a,b):
    
    """retourne le plus grand dénominateur commun de a et b"""
    
    while (b>0):
        r=a%b
        a,b=b,r
    return a
    
def pgcde(a, b):
    
    """ pgcd étendu avec les 2 coefficients de bézout u et v
    Entrée : a, b entiers
    Sorties : r = pgcd(a,b) et u, v entiers tels que a*u + b*v = r
    """
    r = a
    u = 1
    v = 0
    rp = b
    up = 0
    vp = 1
    while rp != 0:
        q = r//rp
        rs, us, vs = r, u, v
        r, u, v = rp, up, vp
        rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)    
    return (r, u, v)