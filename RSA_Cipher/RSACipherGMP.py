### Python implementations of RSA cipher 
### gmpy2 (GNU MP library) version 

import random
import gmpy2
from gmpy2 import mpz
import time

rand_state = gmpy2.random_state(mpz(time.time()*1000))

def gcd(p,q):
    """
    calculate the gcd(greatest common divider) of two positive integers
    """
    return gmpy2.gcd(p,q)

def lcm(p,q):
    """
    calculate the lcm(least common multiplier) of two positive integers
    """
    return gmpy2.lcm(p,q)

def is_coprime(p, q):
    """
    Check whether {x} and {y} are coprime
    """
    return gcd(p, q) == 1

def is_prime(n):
    """
    check whether a number is a prime
    """
 
    return gmpy2.is_prime(n)

def next_prime(n):
    """
    find the next prime number of {n}
    """
    return gmpy2.next_prime(n)    

def invert(a, m):
    """
    Modular multiplicative inverse  n^{-1} mod({m}). 
    """
    return gmpy2.invert(a,m) 

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
        print("Public/Encryption Key  (e, n):", (int(e), int(n)))
        print("Private/Decryption Key (d, n):", (int(d), int(n)))
    
    return (d,n),(e,n)

def encrypt(plain, key):
    """
    Encrypt {plain} (an integer) with the public key (e, n)
    """
    e, n = key
    return plain**e % n 
    
def decrypt(cipher, key):
    """
    decrypt the {cipher} (an integer) with the private key (d, n)
    """
    d, n = key
    return cipher**d % n

def fermat_factors(n) :
    """
    use Fermat's theroem to decompose {n} into two prime numbers
    i.e., to crack the RSA key by factorizing {n}
    """
    
    Number = mpz(n)
    
    if gmpy2.is_square(Number) :
        a = gmpy2.isqrt(Number)
        return (a, a)
    
    a = gmpy2.isqrt(Number)+1
    while True:
        b2 = gmpy2.mul(a,a) - Number
        if gmpy2.is_square(b2) :
            break
        else:
            a += 1
    b = gmpy2.isqrt(b2)   
    return (a-b,  a+b)