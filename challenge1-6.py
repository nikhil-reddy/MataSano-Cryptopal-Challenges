import binascii
import base64
from Crypto.Util.strxor import strxor, strxor_c

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
    # print max
    return pos
def edit_distance(str1, str2):
	bin_str1= '0'+bin(int(binascii.hexlify(str1),16))[2:]
	bin_str2= '0'+bin(int(binascii.hexlify(str2),16))[2:]

	if len(bin_str1)!= len(bin_str2):
		return -1
	hamming_distance =0;
	for i in xrange(len(bin_str2)):
		if bin_str2[i] != bin_str1[i]:
			hamming_distance += 1

	return hamming_distance

def find_keysize(str):
	min_dist = 9999999
	final_keysize = 0
	for i in xrange(2,40):
		temp = calc_normalised_edit_distance(str , i)
		if temp < min_dist:
			min_dist = temp
			final_keysize = i

	return final_keysize


def calc_normalised_edit_distance(str, keysize):

	str_block1 = str[0:keysize]
	str_block2 = str[keysize:keysize*2]

	dist = edit_distance(str_block1, str_block2)
	ans = dist/keysize

	return ans

def block_arrange(str, keysize):
	list_normal=[]
	list_arranged=[]

	for i in xrange(0 , len(str) , keysize):
		list_normal.append(str[i:i+keysize])

	for i in xrange(0,keysize-1):
		temp_string=""
		for j in xrange(len(list_normal)):
			temp_string+= list_normal[j][i] 
		list_arranged.append(temp_string)

	return list_arranged


def calc_key(str, keysize):
	arranged_list = block_arrange(str,keysize)
	key =""
	for i in xrange(0,keysize-1):
		pos_temp = check(arranged_list[i])
		print chr(pos_temp)
		key += chr(pos_temp)

	# print key



str1 = "this is a test"
str2 = "wokka wokka!!!"
f = open("file1-6.txt",'r')
line = f.read()
line_send= base64.b64decode(line)
# print line_send
keysize_send = find_keysize(line_send)

final_key = calc_key(line_send , keysize_send)
print final_key

