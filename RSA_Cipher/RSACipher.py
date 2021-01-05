### Python implementations of RSA cipher 
### The following uses native algorithms
### For faster versions, see gmpy2 (GNU MP library) 

import random

def gcd(p,q):
    """
    calculate the gcd(greatest common divisor) of two positive integers
    """
    while q != 0:
        p, q = q, p%q
    return p

def lcm(p,q):
    """
    calculate the lcm(least common multiple) of two positive integers
    """
    return (p*q)//gcd(p,q)

def is_coprime(p, q):
    """
    Check whether {x} and {y} are coprime
    """
    return gcd(p, q) == 1

def is_prime(n):
    """
    check whether a number is a prime
    """
    
    if (n <= 1):
        return False
 
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False
 
    return True

def next_prime(n):
    """
    find the next prime number of {n}
    """
    i = n
    while True:
        if is_prime(i):
            return i
        i += 1
    return     

def invert_bf(a, m):
    """
    Modular multiplicative inverse  a^{-1} mod({m}).
    with a brute force search
    """
    a = a % m 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1

def invert(a, m): 
    """
    Modular multiplicative inverse  a^{-1} mod({m}).
    with the extended Eucleandian algorithm
    """
    
    q0, r0, t0 = 0, m, 0
    q1, r1, t1 = 0, a%m, 1
    
    while r1 != 1:
        q, r = divmod(r0, r1)
        t = t0 - q*t1
        q0, r0, t0 = q1, r1, t1
        q1, r1, t1 = q, r, t
    return t1 % m


def powmod(a, b, m):
    """
    Compute a^b mod (m) with the Fast Modular Exponentiation algorithm
    compute a^1, a^2, a^4, a^8 .. mod m, since a^{2^n} mod = (a^{2^{n-1}} mod)^2 mod 
    It runs much faster than a**b %m  
    """
    
    # q, r keep quotient, remainder of b/2 
    # initial value
    q, r = b, 0
    # track a^{2n} mod m
    apowmod = a % m 
    # set return result to 1 at first
    result = 1
    # iterative till the quotient is 0
    while q>0:
        # get the quotient, remainder
        q, r = divmod(q, 2)
        # if that bit is non-zero
        if r==1:
            # multiply the a^{2^n} mod to result
            result = result*apowmod % m
        # compute a^{2^n} mod from a^{2^{n-1}} mod
        apowmod = apowmod**2 % m
    # all done     
    return result

def generate_prime(bits_min=0, bits_max=32):
    """
    generate a prime number between 2^bits_min and 2^bits_max
    """
    temp = random.randint(2**bits_min, 2**bits_max)
    return next_prime(temp)

def generate_key(bits=(2,6), debug=False, e=None):
    """
    generate RSA key with p, q between 2^{bits[0]} and 2^{bits[1]}
    {debug} = True to print  
    """
    
    bits2 = bits
    
    # generate two primes numbers (0, 2^bits1-1) and (0, 2^bits2-1)
    p = generate_prime(bits[0], bits[1])
    # make sure they are not the same
    while True:
        q = generate_prime(bits2[0], bits2[1])
        if q != p:
            break
    
    # n = p*q
    n = p*q
    # lambda(n) = lcm(p-1, q-1)
    lambda_n = lcm(p-1, q-1)
   
    # choose e to be coprime with lambda_n
    if e is None:
        e = 1
        while e<=1 or gcd(e, lambda_n) != 1 :
            e = random.randint(2, lambda_n)
    
    
    # get d as  d*e mod lambda_n = 1
    d = invert(e, lambda_n)
    
    if debug:
        print("RSA Key Generator")
        print("p= ", p, " q= ", q)
        print("lambda(n) =", lambda_n)
        print("Public/Encryption Key  (e, n):", (e, n))
        print("Private/Decryption Key (d, n):", (d, n))
    
    return (d,n),(e,n)


def generate_key_pq(p, q, debug=False, e=None):
    """
    generate RSA key with p, q
    {debug} = True to print  
    """
    
    # n = p*q
    n = p*q
    # lambda(n) = lcm(p-1, q-1)
    lambda_n = lcm(p-1, q-1)
   
    # choose e to be coprime with lambda_n
    if e is None:
        e = 1
        while e<=1 or gcd(e, lambda_n) != 1 :
            e = random.randint(2, lambda_n)
    
    
    # get d as  d*e mod lambda_n = 1
    d = invert(e, lambda_n)
    
    if debug:
        print("RSA Key Generator")
        print("p= ", p, " q= ", q)
        print("lambda(n) =", lambda_n)
        print("Public/Encryption Key  (e, n):", (e, n))
        print("Private/Decryption Key (d, n):", (d, n))
    
    return (d,n),(e,n)


def encrypt(plain, key):
    """
    Encrypt {plain} (an integer) with the public key (e, n)
    """
    e, n = key
    return powmod(plain, e, n)
    
def decrypt(cipher, key):
    """
    decrypt the {cipher} (an integer) with the private key (d, n)
    """
    d, n = key
    return powmod(cipher, d, n)

def fermat_factors(n) :
    """
    use Fermat's theroem to decompose {n} into two prime numbers
    i.e., to crack the RSA key by factorizing {n}
    """
    from math import ceil, sqrt
    
   # for odd positive integers only 
    if(n<= 0): 
        return n   
  
    # check if n is a even number  
    if(n & 1) == 0:   
        return n / 2, 2
          
    a = ceil(sqrt(n)) 
  
    #if n is a perfect root,  
    #then both its square roots are its factors 
    if(a * a == n): 
        return (a, a) 
  
    while True: 
        b2 = a * a - n  
        b = int(sqrt(b2)) 
        if b * b == b2 : 
            break
        else: 
            a += 1 
    return a-b, a + b