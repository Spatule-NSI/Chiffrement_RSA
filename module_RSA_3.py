import numpy as np




def premier(n):
    
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
    
    while (b>0):
        
        r=a%b
        
        a,b=b,r
        
    return a
    
    
    
def pgcde(a, b):

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






def key():

    p = np.random.choice(1000,1)
    q = np.random.choice(1000,1)
    
    while premier(p) is False:
        p = np.random.choice(1000,1)
        
    while premier(q) is False:
        q = np.random.choice(1000,1)
        

    n = p*q
    m = (p-1)*(q-1)

    r = 10
    d = 0
    while r != 1 or d <= 2 or d >= m:
        c = np.random.choice(1000,1)
        r, d, v = pgcde(c,m)
        
    n, c, d = int(n), int(c), int(d)
    

    return {"priv":(n,c), "pub":(n,d)}
    
    
    
    
    
def chiffre(n, c, msg):
    
 
    asc = [str(ord(j)) for j in msg]
    

    for i, k in enumerate(asc):
        
        if len(k) < 3:      
            
            while len(k) < 3:
                
                k = '0' + k
            
            asc[i] = k
                
    ascg = ''.join(asc)
    
    d , f = 0 , 4
    
    while len(ascg)%f != 0: 
        
        ascg = ascg + '0'

    l = []
    
    while f <= len(ascg):
        
        l.append(ascg[d:f])
        
        d , f = f , f + 4

    crypt = [str(((int(i))**c)%n) for i in l]
    
    return crypt
    
    
    
    
    
    
    
    
    

    
    
    
    
def dechiffre(n, d, *crypt):

    resultat = [str((int(i)**d)%n) for i in crypt]
        
        
    for i, s in enumerate(resultat):
        
        if len(s) < 4:
            
            while len(s) < 4:
                
                s = '0' + s
            
            resultat[i] = s
        
    g = ''.join(resultat)
    
    asci = ''
    
    d , f = 0 , 3
    
    while f < len(g):
        
        asci = asci + chr(int(g[d:f])) 
        
        d , f = f , f + 3
    
    
    
    
    return asci