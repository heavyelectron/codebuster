
EnglishLetterFrequencyDict = {
    'E': '12.51%',
    'T': '9.25%',
    'A': '8.04%',
    'O': '7.60%',
    'I': '7.26%',
    'N': '7.09%',
    'S': '6.54%',
    'R': '6.12%',
    'H': '5.49%',
    'L': '4.14%',
    'D': '3.99%',
    'C': '3.06%'  # more to be added
}


def createCipherDict():
    """
    
    """
    import random
    
    # create a list of alphabets
    plain = [None]*26
    # assign them to letters
    for i in range(26):
        plain[i] = chr(i+ord('A'))
        
    # flag to check whether the letter remains itself
    matchFlag = True
    # repeat the following procedure untill none of letters remains the same
    while(matchFlag):
        # create a cipher 
        cipher = plain[:]
        # scrabmle the cipher
        random.shuffle(cipher)
        for i in range(26):
            if cipher[i] == plain[i]:
                matchFlag = True
                break
            else:
                matchFlag = False
    
    # make a dict
    cipherDict = {}
    for i in range(26):
        cipherDict.update({plain[i]: cipher[i]})
        
    return cipherDict

def inverseCipherDict(cipherDict):
    
    """
    """
    invCipherDict = {v: k for k, v in cipherDict.items()}
    
    return dict(sorted(invCipherDict.items()))


def printCipherTable(cipherDict, isInverse=False):
    """
    """
    
    key = [p for p,c in cipherDict.items()]
    value = [c for p,c in cipherDict.items()]
    
    if not isInverse:
        print("Plain:  ", ''.join(p for p in key))
        print("Cipher: ", ''.join(p for p in value))
    else:
        print("Cipher: ", ''.join(p for p in key))
        print("Plain:  ", ''.join(p for p in value))
        
def createK1CipherDict(keyword):
    """
    Create a K1 Cipher dictionary
    """
    import random
    
    # remove duplicate letters from keyword
    key = ''.join(dict.fromkeys(keyword.upper()))
    keylen = len(key)
    if len(keyword) != keylen:
        print("Keyword is updated to remove duplicate letters", key)
        
    # split key to list
    
    
    # create a list for plain
    plain = [None]*26
    # generate a random location to put keyword
    loc = random.randint(0, 25)
    for i in range(keylen):
        plain[(loc+i) % 26] = key[i]
    # set the rest
    loc += keylen
    for i in range(26):
        char = chr(i+ord('A'))
        if not (char in key):
            plain[loc%26] = char
            loc+=1

    # create a list of alphabets for cipher
    cipher = [None]*26
    # assign them to letters
    for i in range(26):
        cipher[i] = chr(i+ord('A'))
    
    # make a dict
    cipherDict = {}
    for i in range(26):
        cipherDict.update({plain[i]: cipher[i]})
        
    return cipherDict
        
        
def encrypt(plaintext, cipher):
    """
    Encrypt a {plaintext} with the {cipher} table
    """
    
    # create an empty string for output
    result = "" 
  
    # iterate over the input text
    for i in range(len(plaintext)): 
        # get the character
        char = plaintext[i] 
        # if it's a upper case letter 
        if (char.isupper()): 
            result += cipher.get(char)
        # if it's a lower case letter 
        elif (char.islower()): 
            result += cipher.get(char.upper()).lower()
        # All others including space, numbers, symbols
        else:
            # just copy it
            result += char
    # return the encrypted text
    return result 
    
def decrypt(ciphertext, decipher):
    """
    Decrypt a {ciphertext} with the {decipher} table, i.e., inverse of a ciphertalbe
    """
    
    # create an empty string for output
    result = "" 
  
    # iterate over the input text
    for i in range(len(ciphertext)): 
        # get the character
        char = ciphertext[i] 
        # if it's a upper case letter 
        if (char.isupper()): 
            result += decipher.get(char)
        # if it's a lower case letter 
        elif (char.islower()): 
            result += decipher.get(char.upper()).lower()
        # All others including space, numbers, symbols
        else:
            # just copy it
            result += char
    # return the decrypted text
    return result  


def LetterCounter(text):
    """
    Count the letters in {text}
    Return a dict with {'Letter': count}
    """
    # init an empty list of counts for 'A-Z'
    count = [0]*26
    
    # iterate over text
    for i in range(len(text)):
        # get the character
        char = text[i]
        # check whether it's a letter
        if char.isalpha():
            # if a letter, add its count
            # ord() takes ascii code, 65=ord('A')
            count[ord(char.upper())-65] += 1
    
    # make a dict
    countDict = {}
    # iterate 'A' to 'Z' 
    for i in range(26):
        # add letter and its count to dict
        countDict.update({chr(65+i): count[i]})
    # all done
    return countDict 

def LetterCounterSorted(text):
    """
    Count the letters in {text}
    Return a dict with {'Letter': count} which is sorted by count
    """
    
    # call the count method to get the count dict
    countDict = LetterCounter(text)
    # sort by count 
    return dict(sorted(countDict.items(), key=lambda item: item[1], reverse=True))
    

def LetterFrequency(text):
    """
    Count the frequecy (%) of letters in {text}
    """
    
    # call the count method to get the count dict
    countDict = LetterCounterSorted(text)
    
    # sort countDict
    
    # get total counts
    totalCounts = 0
    for letter,count in countDict.items():
        totalCounts += count
    
    # create a frequency dict
    freqDict = {}
    for letter,count in countDict.items():
        freqDict.update({letter: "{:.2%}".format(count/totalCounts)})
        
    return freqDict


def MonoAlphaCipherHelper(text):
    """
    Format the count dict {'Letter': count} into a Markdown table
    """
    
    # get the counts
    countDict = LetterCounter(text)
    
    # print a table of counts
    print("|Ct  | A| B| C| D| E| F| G| H| I| J| K| L| M| N| O| P| Q| R| S| T| U| V| W| X| Y| Z|")
    print("|----|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|")
    
    countLine = "|Freq|"
    for letter, count in countDict.items():
        countLine += "{:2}".format(count)+"|"
    print(countLine)
    print("|Pt  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")
    
    # sort the dict by count
    countDict = dict(sorted(countDict.items(), key=lambda item: item[1], reverse=True))
    # get the most used 12 letters
    letters=''
    for letter,count in countDict.items():
        letters += letter
    print("")
    print("Letter with most counts:  ", letters[0:12])
    print("Most used English letters:", "ETAOINSHRDLU")

    return

def decrypt_BF(ciphertext, matchrate=0.8):
    """
    A brute force approach to decipher any mono-alphabetic substitution ciphers
    THIS PROGRAM DOESNOT WORK: generating 26! list is impossible, needs another way to generate permutations
    """
    
    # use a spellchecker to check whether words are in dictionary
    from spellchecker import SpellChecker
    # create an English spell checker
    spell = SpellChecker(language=u'en')
    
    # set the criterion for the number of matched words
    wordsCount = len(spell.split_words(ciphertext))
    wordsMatchCountMin = int(matchrate*wordsCount)
    
    # create a list of alphabets for ct
    cipher = [None]*26
    # assign them to letters
    for i in range(26):
        cipher[i] = chr(i+ord('A'))
    
    # generate all possible permutations
    import itertools 
    plain_lists = list(itertools.permutations(cipher))
    
    for i in range(len(plain_lists)):
        # create the plain list
        plain = plain_lists[i]
        
        # create the decipher dict
        decipherDict = {}
        # iterate 'A' to 'Z' 
        for seq in range(26):
            # add letter and its count to dict
            decipherDict.update({ cipher[seq]: plain[seq]})
        
        # decrypt with the current decipher table
        decrypted = decrypt(ciphertext, decipherDict)
        # split the text into a list of words
        wordsList = spell.split_words(decrypted)
        wordsCount = len(wordsList)
        
        print(i)
        # check whether it is a real word
        dictWordsList = spell.known(wordsList)
        if len(dictWordsList) >= wordsMatchCountMin:
            print("Find dictionary words at shift ", shift)
            printCipherTable(decipherDict, isInverse=True)
            return decrypted
    
    print("All trials failed")
    return ""
    
    return
