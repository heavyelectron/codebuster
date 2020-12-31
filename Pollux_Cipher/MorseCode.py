# Python program to implement Morse Code Translator 
  
# Dictionary representing the morse code chart 

MORSE_CODE_DASH = '-'
MORSE_CODE_DOT_S = '.' 
MORSE_CODE_DOT = '•' 
MORSE_CODE_DOT_L = '●'
MORSE_CODE_DIV = 'x'
MORSE_CODE_UNKNOWN = '$'

MORSE_CODE_DICT = {'A': '•-', 'B': '-•••', 'C': '-•-•', 
                    'D': '-••', 'E': '•', 'F': '••-•', 'G': '--•', 
                    'H': '••••', 'I': '••', 'J': '•---', 'K': '-•-', 
                    'L': '•-••', 'M': '--', 'N': '-•', 
                    'O': '---', 'P': '•--•', 'Q': '--•-', 
                    'R': '•-•', 'S': '•••', 'T': '-', 
                    'U': '••-', 'V': '•••-', 'W': '•--', 
                    'X': '-••-', 'Y': '-•--', 'Z': '--••', 
                    '1': '•----', '2': '••---', '3': '•••--', 
                    '4': '••••-', '5': '•••••', '6': '-••••', 
                    '7': '--•••', '8': '---••', '9': '----•', 
                    '0': '-----', 
                    ', ': '--••--', '.': '•-•-•-', '?': '••--••', 
                    '/': '-••-•', '-': '-••••-', 
                    '(': '-•--•', ')': '-•--•-'}

# reverse dictionary
# may be generated as {v: k for k, v in MORSE_CODE_DICR.items()}
MORSE_CODE_DECIPHER_DICT = {'•-': 'A', '-•••': 'B', '-•-•': 'C', 
                            '-••': 'D', '•': 'E', '••-•': 'F', '--•': 'G', 
                            '••••': 'H', '••': 'I', '•---': 'J', '-•-': 'K', 
                            '•-••': 'L', '--': 'M', '-•': 'N', 
                            '---': 'O', '•--•': 'P', '--•-': 'Q', 
                            '•-•': 'R', '•••': 'S', '-': 'T', '••-': 
                            'U', '•••-': 'V', '•--': 'W', 
                            '-••-': 'X', '-•--': 'Y', '--••': 'Z', 
                            '•----': '1', '••---': '2', '•••--': '3', 
                            '••••-': '4', '•••••': '5', '-••••': '6', 
                            '--•••': '7', '---••': '8', '----•': '9', 
                            '-----': '0', 
                            '--••--': ', ', '•-•-•-': '.', '••--••': '?', 
                            '-••-•': '/', '-••••-': '-', 
                            '-•--•': '(', '-•--•-': ')'}


def encrypt(message):
    """
    encypt {message} in plain text with Morse Code
    """
    # create an empty string for cipher
    cipher = '' 
    
    # iterative all letters
    for letter in message:
        # check spaces
        if letter != ' ': 
            # Look up the dictionary for the Morse code
            code = MORSE_CODE_DICT.get(letter.upper())
            # if its code doesn't exists, skip
            if code is not None:
                # otherwise, add it to cipher 
                # with a divider for letters
                cipher += code + MORSE_CODE_DIV
        else: 
            # add additional divider for space
            cipher += MORSE_CODE_DIV
    
    # remove the last divider
    if cipher[-1] == MORSE_CODE_DIV:
        cipher = cipher[:-1]

    return cipher
  
    
def decrypt(message, helper=False): 
    """
    Decrypt Morse codes into plain text
    The input uses one MORSE_CODE_DIV to separate letters, 
    two MORSE_CODE_DIV to separate words
    if helper is on, print code and aligned decipher
    """
    # add a divider to the end in case it is not provided
    message += MORSE_CODE_DIV
    
    # deciphered text
    decipher = '' 
    # if helper is on
    if helper:
        decipher_aligned = ''
    
    # track the Morse code
    code = '' 
    for letter in message: 
        # checks for divider 
        if (letter != MORSE_CODE_DIV): 
            # counter to keep track of div 
            i = 0
            # storing morse code of a single character 
            code += letter 
  
        # in case of divider 
        else: 
            # if i = 1 that indicates a new character 
            i += 1
  
            # if i = 2 that indicates a new word 
            if i == 2 : 
  
                 # adding space to separate words 
                decipher += ' '
                if helper:
                    decipher_aligned += ' '
            else: 
                # accessing the keys using their values (reverse of encryption)
                dletter = MORSE_CODE_DECIPHER_DICT.get(code)
                # if code is unknown, use a symbol
                dletter = dletter if dletter is not None else MORSE_CODE_UNKNOWN 
                decipher += dletter
                # for the aligned text
                if helper:
                    decipher_aligned += dletter + ' '*len(code)
                
                code = '' 
  
    if helper:
        print("Morse Code  :", message)
        print("Deciphertext:", decipher_aligned)

    return decipher