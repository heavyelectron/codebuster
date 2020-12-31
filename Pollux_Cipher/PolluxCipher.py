### Pollux Cipher

import MorseCode
from MorseCode import MORSE_CODE_DICT, MORSE_CODE_DECIPHER_DICT, MORSE_CODE_DASH, MORSE_CODE_DOT, MORSE_CODE_DIV


### Pollux Cipher Key is defined as a dict of lists
#  cipherKey = { '.' : [3, 5],
#                '-' : [0, 7, 9], 
#                'x' : [1, 2, 4, 8] }

### Decipher Key is defined as a dict 
# DecipherKey = { 1: 'x', 2: 'x', 3: '.', 4: 'x' .... }
# If the symbol is unkown, we use MORSE_CODE_UNKNOWN='$'
#    e.g., 6: '$'

MORSE_CODE_UNKNOWN='$'

def keyGenerator(counts=(4,3,3)):
    """
    Generate a random Pollux Cipher Key with 0 to 9
    divided into three groups for three symbols, 
    as specified by {counts}  
    """
    import random 
    # a list of 0-9
    numbers = [i for i in range(10)]
    # shuffle it
    random.shuffle(numbers)
    # generate two numbers to divide them into three groups 
    n1,n2,n3 = counts
    key = { MORSE_CODE_DOT: numbers[:n1],
            MORSE_CODE_DASH: numbers[n1:n1+n2],
            MORSE_CODE_DIV : numbers[n1+n2:] }
    return key

def keyInverse(key):
    """
    Inverse the Pollux number {key}
    """
    
    inv_key = {}
    for symbol, numbers in key.items():
        for number in numbers:
            inv_key.update( {number: symbol})
    # return a sorted key
    return dict(sorted(inv_key.items()))    
    
def encrypt(message, key, helper=False):
    """
    use Pollux cipher to encrypt a {message} with a given number {key}
    if {helper} is true, print the Morse Code
    """
    import random 
    
    cipher = ''
    # encrypt the message to Morse Code at first
    morse_code = MorseCode.encrypt(message)

    # iterate over 
    for code in morse_code:
        # get its number list
        numbers = key.get(code)
        # randomly choose one and assign it to key
        cipher += str(random.choice(numbers))

    # if helper, print out the morse_code
    if helper:
        print("Pollux Cipher Encryption")
        print("Key dictionary:", key)
        print("Plaintext :", message)
        print("Morse Code:", morse_code)    
        print("Ciphertext:", cipher)    
    # all done
    return cipher
    
def decrypt(ciphertext, key, is_inverse_key=False, helper=False):
    """
    Decrypt a Pollux encrypted {ciphertext}
    {key} is encryption dict if {is_inverse_key}=False, otherwise, is the decryption key
    if {helper} is true, print the intermediate Morse Code results
    Note: if the key is incomplete, the text may include "unknown" letters
    """
    
    if not is_inverse_key:
        key = keyInverse(key)
    
    if helper:   
        print("Pollux Cipher Decrytion")
        print("Decryption key:", key)
        print("Ciphertext  :", ciphertext)  
    # decode to Morse Code at first
    morse_code = ''
    # iterative the ciphertext to transform numbers to symbols
    for letter in ciphertext:
        code = key.get(int(letter))
        code = code if code is not None else MORSE_CODE_UNKNOWN
        morse_code += code
    
    # decode to plaintext
    decipher = MorseCode.decrypt(morse_code, helper=helper)
    return decipher