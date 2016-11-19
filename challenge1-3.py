import binascii
from Crypto.Util.strxor import strxor_c

# From http://www.data-compression.com/english.html
freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}
def score(s):
    score = 0
    for c in s: 
        if c in freqs:
            score += freqs[c]
    # print score
    return score

def check(s):
    max=0
    pos =0;
    for i in range(0,256):
        res = strxor_c(s, i)
        temp =score(res)
        if temp > max:
            max=temp
            pos =i
    print max
    return pos

var = raw_input("Enter hex: ")
input = var.decode('hex')
ans = check(input)
print ans

print strxor_c(input,ans)