'''
@author: Alex Decker
'''

from numpy import matrix, zeros, linalg
import random

defaultAlphabet = "0123456789abcdefghijklmnopqrstuvwxyz"

key = None
alph = None
idLength = None

def tuid_init(seed, length, alphabet="0123456789abcdefghijklmnopqrstuvwxyz"):
    global key,alph,idLength
    random.seed(seed)
    alph = alphabet
    idLength = length
    key = None
    
    
def tuid(index):  
    digits = convertBase(index, len(alph),idLength)
    v = matrix(digits).transpose()
    
    if key is None: genKey(idLength)
    r = key*v
    ciphered = map(lambda x: x%len(alph),r.transpose().tolist()[0])
    return toAlphabet(ciphered,alph)


def genKey(size):
    """Generates alph random square matrix of the given size

    A valid key matrix must be invertible (determinant != 0,etc)
    and the determinant cannot have any common factors with 
    the length of the alph used. genKey guarantees these properties
    in order to guarnatee uniqueness.
    """
    global key
    key = matrix(zeros((size,size)))
    (rows,cols) = key.shape
    valid = False
    while not valid:
        
        #generate matrix randomly
        for i in range(rows):
            for j in range(cols):
                # range is arbitrary
                key[i,j] = random.randint(0,10)
                
        valid = True
        
        #test if matrix is valid: see above
        det = int(round(linalg.det(key)))        
        if det == 0:
            valid = False
        
        #testing for factors, usually called once so just using alph naive approach
        for i in range(min(abs(det),len(alph)),1,-1):
            if det % i == 0 and len(alph) % i == 0:
                valid = False


def toAlphabet(digits, alph):
    s = ""
    for i in digits:
        s = s + alph[int(i)]
    return s        


def convertBase(num, base, length):
    try:
        num = int(num)
        base = int(base)
    except:
        return None
    
    digits = [0] * length
    
    for i in range(length-1,-1,-1):
        r = num % base
        digits[i] = r
        num = num / base
    return digits