'''
Created on Feb 3, 2012

@author: alex
'''

from numpy import matrix
from random import random

defaultAlphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
m = None #matrix([[0,2,3,1],[0,1,1,2],[2,2,1,0],[1,2,1,3]])

def setSeed(seed):
    random.seed(seed)
    
def setMatrix(size):
    m = matrix(7)
    for i in range(m.rows):
        for j in range(m.cols):
            m[i,j] = random.random()

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

def cipher(digits,base,length):
    v = matrix(digits).transpose()
    if not m: setMatrix(length)
    r = m*v
    return map(lambda x: x%base,r.transpose().tolist()[0])
      
def toAlphabet(digits, alphabet):
    s = ""
    for i in digits:
        s = s + alphabet[i]
    return s

def tuid(index, length, **kwargs):
    if kwargs.has_key("alphabet"): a = kwargs["alphabet"]
    else: a = defaultAlphabet
    
    digits = convertBase(index, len(a),length)
    digits = cipher(digits,len(a),length)
    return toAlphabet(digits,a)

def testCoverage():
    d = set(['dfre','4sdr','rfdw'])
    for i in range(0,pow(36,4)+10):
        if i%32768==0: print i
        s = tuid(i,4)
        if s in d:
            print i,s
        else:
            d.add(s)