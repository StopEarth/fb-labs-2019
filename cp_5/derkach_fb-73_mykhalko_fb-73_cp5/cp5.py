import random as rnd

def Random():
    k = rnd.randint(2**256, 2**256 + 10**6)
    if k % 2 == 0:
        k += 1
    return k

def RandomBin(n):
    a = ''
    a += '1'
    for i in range(1,n-1):
        a += str(rnd.randint(0,1))
    a += '1'
    return(a)

def Decomposition(a):
    s = 0
    d = a - 1
    while 1:
        if  d % 2 == 0:
            s +=1
            d //= 2
        else :
            return d, s
        if d == 0:
            return d, s
    
def gsd(a, b):
    if b > a:
        a, b = b, a
    while 1:
        q = a // b
        r = a % b
        if r == 0:
            break
        a, b = b, r
    return b

def Inverse(a, m):
    if gsd(a,m) == 1:
        r0, r1 , u0, u1, y0, y1 =a, m, 1, 0, 0, 1
        while r1:
            q = r0 // r1
            r0, r1= r1, r0 % r1
            u0, u1 = u1, u0 - u1*q
            y0, y1 = y1, y0 - y1*q
            if a*u0+m*y0 == 1:
                return u0
        else:
            return 'error'

def Equation(a, m, b):
    r0, r1 , u0, u1, y0, y1 =a, m, 1, 0, 0, 1
    while r1:
        q = r0 // r1
        r0, r1= r1, r0 % r1
        u0, u1 = u1, u0 - u1*q
        y0, y1 = y1, y0 - y1*q
        if a*u0+m*y0 == 1:
            if u0 < 0:
                return ((u0 + m) * b) % m
            else:
                return (u0 * b) % m 
    if b % r0 !=0:
        return 'error'
    else:
        u0 = Ober(a//r0, m//r0, b//r0)
        listO = []
        while 1:
            listO.append(u0)
            u0 += m//r0
            if u0 > m:
                return listO

        
def MR_Test(p):
    d, s = Decomposition(p)
    counter = 0
    k = 10
    while 1:
        x = rnd.randint(1,p)
        if gsd(x, p) > 1:
            return 'Skladne'
        else:
            if (pow(x,d,p) == 1) or (pow(x,d,p) == p-1):
                counter += 1
            else:
                for r in range(1, s+1):
                    xr = pow(x,d * (2**r), p)
                    if xr == 1:
                        break
                    if xr == p-1:
                        return "Skladne"
                    if r == s:
                        return "Skladne"
                counter += 1
        if counter >= k:
            return 'Proste'
    return
        
def Simple(k):
    while 1:
        if MR_Test(k) == 'Proste':
            print('Proste', k)
            return k
        else:
            print('Skladne', '  ', k)
            k += 2

def GenerateKeyPairs(p, q):
    n = p * q
    fi = (p-1) * (q-1)
    while 1:
        e = rnd.randint(2,fi-1)
        if gsd(e, fi) == 1:
            break
    d = Inverse(e, fi)
    if d < 0:
        d += fi
    return [n,e], [d,p,q]

def Encrypt(M, publickKey):
    n = publickKey[0]
    e = publickKey[1]
    C = pow(M, e, n)
    return C

def Decrypt(C, publickKey, privateKey):
    n = publickKey[0]
    d = privateKey[0]
    M = pow(C, d, n)
    return M

def Sign(M, privateKey, publickKey):
    d = privateKey[0]
    n = publickKey[0]
    S = pow(M, d, n)
    return S

def Verify(M, S, publickKey):
    e = publickKey[1]
    n = publickKey[0]
    if M == pow(S, e, n):
        return True
    else:
        return False

def SendKey(privateKey, publickKey, publickKey1):
    n = publickKey[0]
    n1 = publickKey1[0]
    e1 = publickKey1[1]
    d = privateKey[0]
    k = rnd.randint(1, n)
    k1 = pow(k, e1, n1)
    S = Sign(k, privateKey, publickKey)
    S1 = pow(S, e1, n1)
    return [k1, S1]

def ReceiveKey(privateKey1, publickKey1, publickKey, Secret):
    d1 = privateKey1[0]
    n1 = publickKey1[0]
    n = publickKey[0]
    e = publickKey[1]
    k1 = Secret[0]
    S1 = Secret[1]
    k = pow(k1, d1, n1)
    S = pow(S1, d1, n1)
    if Verify(k, S, publickKey) == 1:
        return k
    else:
        return False

#k = int(RandomBin(256),2)
#Simple(k)

p = 61016536761549808177766998725050708214036184934330506106473389443256538982951
q = 77063376686433988721982243451642158198129151802221411743266048425964211544487
p1 = 59911669318890845110286375051706919254685458523121630945592714532645154040803
q1 = 79986807161860903828678238002470619150351311243618900021813191076996514964699
M = 1257563954208230606439734671520215224675224935703233663

def RSA():
    p = int(RandomBin(256),2)
    q = int(RandomBin(256),2)
    p1 = int(RandomBin(256),2)
    q1 = int(RandomBin(256),2)
    p = Simple(p)
    q = Simple(q)
    p1 = Simple(p1)
    p2 = Simple(p2)
    if p*q > p1*q1:
        p, q = p1, q1
    publickKey, privateKey = GenerateKeyPairs
    M = int(RandomBin(128),2)
    
