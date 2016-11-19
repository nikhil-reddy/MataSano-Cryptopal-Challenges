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
    check_string =s;
    max_val=0
    pos =0;
    for i in range(0,256):
        res = strxor_c(check_string, i)
        temp =score(res)
        if temp > max_val:
            max_val=temp
            pos =i
    
    return pos,max_val,check_string


f_in= open("file.txt",'r')
f_out = open("ans.txt",'w')

final_max = 0
final_pos =0
final_string =""
for line in f_in:
    line= line.strip()
    s = line.decode('hex')
    pos,max_val,fin = check(s)
    if max_val> final_max:
        final_max = max_val
        final_pos =pos
        final_string = fin
print final_max, final_pos , strxor_c(final_string,final_pos)
