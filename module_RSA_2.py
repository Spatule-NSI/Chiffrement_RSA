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
