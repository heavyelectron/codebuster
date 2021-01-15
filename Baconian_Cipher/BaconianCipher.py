### Baconian Cipher



Baconian_Table_24 = {
    'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 
    'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'K', 'ABABA': 'L', 'ABABB': 'M', 'ABBAA': 'N', 
    'ABBAB': 'O', 'ABBBA': 'P', 'ABBBB': 'Q', 'BAAAA': 'R', 'BAAAB': 'S', 'BAABA': 'T', 
    'BAABB': 'U', 'BABAA': 'W', 'BABAB': 'X', 'BABBA': 'Y', 'BABBB': 'Z'}
    

Baconian_Table_26 = {    
    'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 
    'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J', 'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 
    'ABBBA': 'O', 'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T', 
    'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y', 'BBAAB': 'Z'}
    
"""
Baconian 24 Table generator

bdict = {}
j=0
for i in range(24):
    key = "{0:b}".format(i).zfill(5)
    key=key.replace('0', 'A')
    key=key.replace('1', 'B')
    
    
    bdict.update({key : chr(j+65)})
    
    j+=1 
    if j== ord('J')-65 :
        j+=1
    elif j==ord('V')-65 :
        j+=1    
    
print(bdict)
"""

SYMBOL_UNKNOWN='-'

def get_key(pdict, value):
    
    for key, val in pdict.items():
        if val == value:
            return key
    print(f"{value} is not found in dict") 
    return

    
def encrypt(plaintext, use_24=True):
    """
    Encypt a {plaintext} with Baconian Code
    with 24-variation if {use_24}=True, otherwise, use 26-variation
    """
    
    if use_24 :
        bacon = Baconian_Table_24
    else:
        bacon == Baconian_Table_26
    
    cipher = ""
    
    for letter in plaintext:
        
        if letter.isalpha():
            uletter = letter.upper()
            if uletter == 'J':
                uletter = 'I'
            elif uletter == 'V':
                uletter = 'U'
            cipher += get_key(bacon, uletter)+' '
        # not an alphabetc letter
        else:
            cipher += letter
            
    return cipher


def decrypt(ciphertext, use_24=True):
    """
    Decypt a {ciphertext} with Baconian Code, 
    with 24-variation if {use_24}=True, otherwise, use 26-variation
    """
        
    if use_24 :
        bacon = Baconian_Table_24
    else:
        bacon == Baconian_Table_26
    
    decipher = ""
        
    for code in ciphertext.split(' '):
        letter = bacon.get(code)
        if letter is not None:
            decipher += letter+' '
        elif code =='':  
            decipher += ' '
        else:
            decipher += code+' '
            
    return decipher


def decrypt_symbols(symboltext, alist, blist, use_24=True):
    """
    
    """
    ciphertext = ''
    for letter in symboltext:
        if letter in alist:
            ciphertext += 'A'
        elif letter in blist:
            ciphertext += 'B'
        elif letter == ' ':
            ciphertext += letter
        else:
            ciphertext += SYMBOL_UNKNOWN
    
    return decrypt(ciphertext, use_24)

def decrypt_helper(symboltext, alist, blist, use_24=True):

    import string
    ciphertext = ''
    symboltext_reformat = ''
    
    for letter in symboltext:
        if  letter in string.punctuation:
            continue
        elif ord(letter) ==10:
            symboltext_reformat += ' '
        else:
            symboltext_reformat += letter.upper()
    
    
    for letter in symboltext_reformat:
        if letter in alist:
            ciphertext += 'A'
        elif letter in blist:
            ciphertext += 'B'
        elif letter == ' ':
            ciphertext += ' '        
        else:
            ciphertext += SYMBOL_UNKNOWN
            
    print("Ciphertxt:", symboltext_reformat)
        
    print("Baconian :", ciphertext)
    
    if use_24 :
        bacon = Baconian_Table_24
    else:
        bacon == Baconian_Table_26
    
    decipher = ""
        
    for code in ciphertext.split(' '):
        letter = bacon.get(code)
        if letter is not None:
            decipher += letter+' '*5
        elif code =='':  
            decipher += ' '
        else:
            decipher += code+' '
    
    print("Decrypted:", decipher)
    
    return    

