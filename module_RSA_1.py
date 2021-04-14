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
    
    
    







def key():
    
    p = np.random.choice(1000,1)
    q = np.random.choice(1000,1)
    
    while premier(p) is False:
        p = np.random.choice(1000,1)
        
    while premier(q) is False:
        q = np.random.choice(1000,1)
        