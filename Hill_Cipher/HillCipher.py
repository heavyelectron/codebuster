### Hill Cipher 

import numpy as np

def gcd(p,q):
    """
    Create the gcd of two positive integers.
    """
    while q != 0:
        p, q = q, p%q
    return p

def isCoprime(x, y):
    """
    Check whether {x} and {y} are coprime
    """
    return gcd(x, y) == 1

def modInverse(a, m):
    """
    Modular multiplicative inverse  n^{-1} mod({m}). 
    """
    a = a % m 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1
    
def cofactor(matrix, row, col):
    """
    return the cofactor of a matrix element (i,j) of {m}
    """
    
    rows, cols = matrix.shape
    
    cf = []
    for i in range(rows):
        if i == row:
            continue
        for j in range(matrix.shape[1]):
            if j== col:
                continue
            cf.append(matrix[i,j])
    return np.asarray(cf).reshape(rows-1, cols-1)
    

def determinant(matrix):
    """
    return the determinant of a matrix
    """
    rows,cols = matrix.shape
    if rows == 1:
        return matrix[0,0]
    
    det = 0
    sign = 1
    for j in range(cols):
        elem = matrix[0,j]
        cof = cofactor(matrix, 0, j) 
        det += sign*elem*determinant(cof)
        sign = -sign
    return det


def adjugateMatrix(m):
    """
    return the adjugate matrix of {m}
    """
    # get number of rows and columns
    rows, cols = m.shape
    # create a matrix for adjugate 
    adj = np.ndarray(shape=(cols, rows), dtype=m.dtype)
    
    # define an alternating sign
    sign = 1
    # iterate over iterms
    for i in range(rows):
        for j in range(cols):
            # get cofactor
            cf = cofactor(m,i,j)
            # note the order of j,i due to transpose
            adj[j,i] = sign*determinant(cf)
            # flip the sign
            sign = -sign
    # all done 
    return adj
    
def modInverseMatrix(mat, m=26):
    """
    return the modular multiplicative inverse of matrix {mat} mod{m}
    """
    
    # calculate the determinant 
    det = determinant(mat) % m
    if not isCoprime(det, m):
        print("the determinant of the matrix is not coprime with m, irrevertible")
        return
    # get the inverse of the determinant
    detinv = modInverse(det, m)
    # the inverse of detinv*adj(mat)
    return (adjugateMatrix(mat)*detinv % m)


def checkKeyValidity(key):
    """
    Check whether a {key} is valid for Hill Cipher
    """
    if type(key) is list:
        key = np.asarray(key)
    # calculate determinant    
    det = determinant(key)
    # check whether it's coprime with 26
    return isCoprime(det, 26)
  

def keyGenerator(size=2):
    """
    generate a Hill Cipher key of sizexsize, default 2x2    
    """
    import random
    
    key = np.ndarray(shape=(size,size), dtype=np.int64)
    validKey = False
    # keep regenerate untill key is valid
    while(not validKey):
        for i in range(size):
            for j in range(size):
                key[i,j] = random.randint(0,25)
        validKey = checkKeyValidity(key)
        
    return key
    
def encrypt(plaintext, key, check_length=False):
    """
    Encrypt a {plaintext} with a Hill cipher encryption {key}
    {check_length} is only used for decryption, printing a warning if there are some letters left 
    """
    # get the group size from the key   
    size = key.shape[0]
    
    # count the alphabetic letters in plaintext
    length = 0
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            length += 1
    
    # split the string to a list as str doesn't support item assignment
    ciphertext = [c for c in plaintext]
    
    # check whether needs padding
    remainder = length % size
    if remainder != 0:
        # patching Zs at the end
        ciphertext += ['Z']*(size-remainder)
        if check_length:
            # when used at decryption, remainder should be 0
            print("Warining: the message is not properly grouped")
            
    
    # letters are encrypted in group of {size}
    # track the character location
    seq = 0 
    pos = [0]*size
    # store the current encryption group
    activeplain = np.ndarray(shape=size, dtype=np.int64)
    
    # iterate over the plain text
    for i in range(len(ciphertext)):
        # get the character
        char =ciphertext[i]
        # check whether it's a letter
        if char.isalpha():
            # assign the letter 
            activeplain[seq] = ord(char.upper())-ord('A') 
            pos[seq] = i
            # increase the seq
            seq += 1
            # if seq reaches group size  
            if seq == size:
                # encrypt the group
                activecipher = key.dot(activeplain) % 26
                # copy it to cipher text 
                for j in range(size):
                    ciphertext[pos[j]] = chr(activecipher[j]+ord('A'))
                # reset the seq counter
                seq = 0

    # return the joined string
    return ''.join(ciphertext)
    
    
    
    
def decrypt(ciphertext, key):
    """
    Decrypt a {ciphertext} with a Hill cipher decryption {key}
    """
    
    # with the decryption key, as inverse of the encryption key
    # the decrypt is the same as encrypt   
    # but we need to warn if the text mod size(2 or 3) != 0 
    return encrypt(ciphertext, key, check_length=True)    
    
    


        
    
    
    
    
 




    