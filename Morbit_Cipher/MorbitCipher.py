### Morbit Cipher

import MorseCode
from MorseCode import MORSE_CODE_DICT, MORSE_CODE_DECIPHER_DICT, MORSE_CODE_DASH, MORSE_CODE_DOT, MORSE_CODE_DIV,MORSE_CODE_UNKNOWN


### Morbit Cipher/Decipher Key is defined as a list/string of numbers 1-9, or a keyword 
#   and convert to a python dict
# {'4': '••', '5': '•-', '3': '•x', '8': '-•', '6': '--', '1': '-x', '7': 'x•', '2': 'x-', '9': 'xx'}


Morbit_Symbol_List = [
    MORSE_CODE_DOT+MORSE_CODE_DOT, 
    MORSE_CODE_DOT+MORSE_CODE_DASH,
    MORSE_CODE_DOT+MORSE_CODE_DIV,
    MORSE_CODE_DASH+MORSE_CODE_DOT,
    MORSE_CODE_DASH+MORSE_CODE_DASH,
    MORSE_CODE_DASH+MORSE_CODE_DIV,
    MORSE_CODE_DIV+MORSE_CODE_DOT,
    MORSE_CODE_DIV+MORSE_CODE_DASH,
    MORSE_CODE_DIV+MORSE_CODE_DIV]

Morbit_Symbol_Unknown = MORSE_CODE_UNKNOWN*2
    

def word_alphabetic_order(word):
    """
    Generate the number list for letters appear in a {word} in alphabetic orders
    For example: "WISECRACK" return [9, 5, 8, 4, 2, 7, 1, 3, 6]
    """
    
    # split the word into list of letters
    letters = [letter for letter in word]
    # sort the letters, together with locations
    letters_sorted = sorted((let,loc) for loc, let in enumerate(letters))
    # get the list of locations
    letters_loc = [loc for let,loc in letters_sorted]
    # re-order the location to get the indices
    index_sorted = sorted((loc, index) for index,loc in enumerate(letters_loc))
    # get the indices, which give the required order  
    orders = [i+1 for loc, i in index_sorted]
    return orders
    
    
def keyGenerator(keyword=None):
    """
    Generate a random Morbit Cipher Key with 0 to 9
    divided into three groups for three symbols, 
    as specified by {counts}  
    """
    # if keyword is not provided, randomly generate a sequence of numbers 1-9
    if keyword is None:
        import random 
        # a list of 1-9
        numbers = [i for i in range(1,10)]
        # shuffle it
        random.shuffle(numbers)
    # else 
    else: 
        keyword_adjusted = keyword.upper()
        # while length < 9, duplicate 
        while len(keyword_adjusted) < 9:
                keyword_adjusted +=  keyword_adjusted
        # if length >9, cut 
        if len(keyword_adjusted) > 9:
            keyword_adjusted = keyword_adjusted[:9] 
        
        print("Keyword adjusted:", keyword_adjusted)
            
        numbers = word_alphabetic_order(keyword_adjusted)    
     
    return numbers
    
def key_convert(key):
    """
    Convert a Morbit {key} into a python dictionary 
    
    Accetable {key} format:
    str of numbers 
    list of numbers or number characters
    dict
    """
    
    # if the key is a string of numbers
    if isinstance(key, str):
        key_list = [number for number in key]
        key_return = dict(zip(Morbit_Symbol_List, key_list))
 
    # if the key is a list
    elif isinstance(key, list):
        # a list of numbers
        if isinstance(key[0], int):
            key_list = [str(number) for number in key]
            key_return = dict(zip(Morbit_Symbol_List, key_list))
        else:
            key_return = dict(zip(Morbit_Symbol_List, key))
    
    # if already a dictionary
    elif isinstance(key, dict):
        key_return = key
        
    else:
        print(f"Key type is {type(key)} not supported")
        raise TypeError 
    
    return key_return



def key_print(key):
    """
    Print out a Morbit {key} table
    """
    # convert to dict if necessary
    key_ad = key_convert(key)
    print("Morbit Cipher Key:")
    print(''.join([n for n in key_ad.values()]))
    print(MORSE_CODE_DOT*3+MORSE_CODE_DASH*3+MORSE_CODE_DIV*3)
    print((MORSE_CODE_DOT+MORSE_CODE_DASH+MORSE_CODE_DIV)*3)
    return


def encrypt(message, key, helper=False):
    """
    use Morbit cipher to encrypt a {message} with a given number {key}
    if {helper} is true, print the Morse Code
    """
    
    # convert key if necessary
    key_encryption = key_convert(key)
    
  
    # encrypt the message to Morse Code at first
    morse_code = MorseCode.encrypt(message)
    
    if len(morse_code) %2 ==1:
        morse_code += MORSE_CODE_DIV

    ciphertext = ''     
    # iterate over 
    for i in range(0,len(morse_code),2):
        code = morse_code[i:i+2]
        # get its number and add to list
        ciphertext += key_encryption.get(code)

    # if helper, print out the morse_code
    if helper:
        print("Morbit Cipher Encryption")
        key_print(key_encryption)
        print("Plaintext :", message)
        print("Morse Code:", morse_code)    
        print("Ciphertext:", ' '.join(c for c in ciphertext))    
    # all done
    return ciphertext


def decrypt(ciphertext, key, helper=False):
    """
    Decrypt a Morbit encrypted {ciphertext} with a (complete /partial) {key}
    Note: if the key is incomplete, the text may include "unknown" letters
    """
    
    key_encryption = key_convert(key)
    key_decryption = {v: k for k, v in key_encryption.items()}

    # clean up the ciphertext
    ct = ''
    for c in ciphertext:
        if c.isdigit():
            ct += c
    
    
    if helper:   
        print("Morbit Cipher Decrytion")
        key_print(key_encryption)
        print("Ciphertext  :", ' '.join(c for c in ct))  
        
    # decode to Morse Code at first
    morse_code = ''
    # iterative the ciphertext to transform numbers to symbols
    for letter in ct:
        code = key_decryption.get(letter)
        code = code if code is not None else Morbit_Symbol_Unknown
        morse_code += code
    
    # decode to plaintext
    decipher = MorseCode.decrypt(morse_code, helper=helper)
    return decipher