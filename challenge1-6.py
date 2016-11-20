import binascii
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



str1 = "this is a test"
str2 = "wokka wokka!!!"
ans = edit_distance(str1,str2)

print ans
