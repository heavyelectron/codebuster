### Affine Cipher Utilities


### A Python dictionary has the structure { key: value}
# for example, 
# a cipher/decipher table = {'A': 'G', 'B': 'F', 'C': 'E', 
#                            'D': 'D', 'E': 'C', 'F': 'B', 
#                            ...., 'X': 'J', 'Y': 'I', 'Z': 'H'}


# the numbers coprime with 26
coprime_list = [1,3,5,7,9,11,15,17,19,21,23,25]


def randomKey():
    """
    Generate a random Affine Cipher key
    """
    import random
    # randomly choose one from the coprime list is {a} is not provided
    a = coprime_list[random.randrange(len(coprime_list))]
    # randomly pick a number from 0 to 25      
    b = random.randrange(26)
    return a,b


def createCipherDict(key):
    """
    Create affine cipher dictionary from two integers {key}=(a,b)
    randomly generate one if {key} is None
    """    

    a, b = key
    # check whether 'a' is coprime     
    if not a%26 in coprime_list:
        print("Bad choice of a")
        return 
   
    # create a list of alphabets
    plain = [None]*26
    cipher = [None]*26
    # assign them to letters
    for i in range(26):
        # plain text is alphabet
        plain[i] = chr(i+ord('A'))
        # take linear tansform and mod 26
        j = (a*i+b) % 26
        # assign the code to cipher 
        cipher[i] = chr(j+ord('A'))
    
    # make a python dictionary
    cipherDict = {}
    for i in range(26):
        cipherDict.update({plain[i]: cipher[i]})
        
    return cipherDict

### Invert a cipherDict to a decipherDict or vice versa
def inverseDict(dictionary):
    
    """
    Invert a cipher/dicipher table
    """
    inverseDict = {v: k for k, v in dictionary.items()}
    
    return dict(sorted(inverseDict.items()))

### Printout the cipher table
def printCipherTable(cipherDict, isCipher=True):
    """
    """
    
    key = [p for p,c in cipherDict.items()]
    value = [c for p,c in cipherDict.items()]
    
    if isCipher:
        print("Plain:  ", ''.join(p for p in key).lower())
        print("Cipher: ", ''.join(p for p in value))
    else:
        print("Cipher: ", ''.join(p for p in key))
        print("Plain:  ", ''.join(p for p in value).lower())
        
# substitute letters with the dictionary
def substitute(text, dictionary):
    """
    substitute letters in {text} with the {dictionary}
    """
    
    # create an empty string for output
    result = "" 
  
    # iterate over the input text
    for char in text: 
        # if it's a upper case letter 
        if (char.isupper()): 
            result += dictionary.get(char)
        # if it's a lower case letter 
        elif (char.islower()): 
            result += dictionary.get(char.upper()).lower()
        # All others including space, numbers, symbols
        else:
            # just copy it
            result += char
    # return the decrypted text
    return result        
        

def encrypt(plaintext, key):
    """
    Encrypt a {plaintext} with the affine {key}=(a,b)
    """
    cipherdict = createCipherDict(key)
    # encrypt it 
    return substitute(plaintext, cipherdict) 


def decrypt(ciphertext, key):
    """
    decrypt a {ciphertext} with {key}=(a,b)
    """
    # create the cipher dictionary
    cipherdict = createCipherDict(key)
    # get the decipher dictionary
    decipherdict = inverseDict(cipherdict)
    
    # decrypt it 
    return substitute(ciphertext, decipherdict)
    

def findKey(plaintext, ciphertext):
    """
    Find the key (a,b) from the provided {plaintext} and {ciphertext}
    Only the first two letters are used
    """
    
    # get the x values for the first two letters in plain text
    p0 = ord(plaintext[0].upper())-ord('A')
    p1 = ord(plaintext[1].upper())-ord('A')
    
    # get the x values for the first two letters in cipher text
    c0 = ord(ciphertext[0].upper())-ord('A')
    c1 = ord(ciphertext[1].upper())-ord('A')  
    
    # simply iterate over all possibilities
    for a in coprime_list:
        for b in range(26):
            if (a*p0+b) % 26 == c0 and (a*p1+b) % 26 == c1:
                # find a match, return
                return a,b
    # none is found
    print("The Affine key is not found, try other two letters")
    return