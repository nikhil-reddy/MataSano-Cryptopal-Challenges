import binascii
import base64
from Crypto.Util.strxor import strxor

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





str1 = "this is a test"
str2 = "wokka wokka!!!"
f = open("file1-6.txt",'r')
line = f.read()
line_send= base64.b64decode(line)
# print line_send
ans = find_keysize(line_send)

print ans
