SPANISH_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ',
                    'O', 'P', 'Q', 'R', 'S', 'T', 
                    'U', 'V', 'W', 'X', 'Y', 'Z']

ENGLISH_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                    'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 
                    'U', 'V', 'W', 'X', 'Y', 'Z']

alphabet = SPANISH_alphabet

ALPHABET_UNKNOWN = '-'

def letterCount(text):
    """
    Count the letters in {text}
    Return a dict with {'Letter': count}
    """
    
    alphabet_length = len(alphabet)
    # init an empty list of counts for 'A-Z'
    count = [0]*alphabet_length
    
    # iterate over text
    for char in text:
        # check whether it's a letter
        if char.isalpha():
            # if a letter, add its count
            count[alphabet.index(char)] += 1
    
    # make a dict
    countDict = {}
    # iterate 'A' to 'Z' 
    for i in range(alphabet_length):
        # add letter and its count to dict
        countDict.update({alphabet[i]: count[i]})
    
    # all done
    return countDict

def createCipher():
    """
    
    """
    import random
    
    length = len(alphabet)
    # create a list of alphabets
    plain = alphabet
        
    # flag to check whether the letter remains itself
    matchFlag = True
    # repeat the following procedure untill none of letters remains the same
    while(matchFlag):
        # create a cipher 
        cipher = plain[:]
        # scrabmle the cipher
        random.shuffle(cipher)
        for i in range(length):
            if cipher[i] == plain[i]:
                matchFlag = True
                break
            else:
                matchFlag = False
    
    # make a dict
    cipherDict = {}
    for i in range(length):
        cipherDict.update({plain[i]: cipher[i]})
        
    return cipherDict

def inverseCipherDict(cipherDict):
    
    """
    """
    invCipherDict = {v: k for k, v in cipherDict.items()}
    
    return dict(sorted(invCipherDict.items()))
        
        
def encrypt(plaintext, cipher):
    """
    Encrypt a {plaintext} with the {cipher} table
    """
    
    # create an empty string for output
    ciphertext = "" 
  
    # iterate over the input text
    for char in plaintext: 
        # if it's a upper case letter 
        if (char.isupper()): 
            ciphertext += cipher.get(char)
        # if it's a lower case letter 
        elif (char.islower()): 
            ciphertext += cipher.get(char.upper()).lower()
        # All others including space, numbers, symbols
        else:
            # just copy it
            ciphertext += char
    # return the encrypted text
    return ciphertext
    
def decrypt(ciphertext, decipher):
    """
    Decrypt a {ciphertext} with the {decipher} table, i.e., inverse of a ciphertalbe
    """
    
    # create an empty string for output
    result = "" 
  
    # iterate over the input text
    for char in ciphertext: 
        # if it's a upper case letter 
        if (char.isupper()):
            dchar = decipher.get(char)
            result += dchar if dchar is not None else ALPHABET_UNKNOWN
        # if it's a lower case letter 
        elif (char.islower()): 
            dchar = decipher.get(char.upper())
            result += dchar.lower() if dchar is not None else ALPHABET_UNKNOWN
        # All others including space, numbers, symbols
        else:
            # just copy it
            result += char
    # return the decrypted text
    return result  


def decryptHelper(ciphertext, key={}):
    
    countDict = letterCount(ciphertext.upper())
    
    alphabet_length = len(alphabet)
    
    # print a table
    print("Cipher table and letter frequency:")
    print('| Cipher | ' + '| '.join([letter  for letter in alphabet])+'|')
    print('|:------:|'  + '--|'*alphabet_length)
    print('|Freqnecy|' + '|'.join([str(count).rjust(2) for count in countDict.values()])+'|')
    
    decipher_line = '| Plain  |'
    for letter in alphabet:
        dl = key.get(letter)
        dl = dl if dl is not None else ' '
        decipher_line += ' '+ dl + '|'
            
    print(decipher_line)
    
    plaintext = decrypt(ciphertext, key)
    
    print("Ct:", ciphertext)
    print("Pt:", plaintext)
    return