import binascii
import base64
from Crytpo.Cipher import AES

f_in = open("file1-7.txt",'r')

cipher_text = base64.b64decode(open(f_in.read())


key = '0'+bin(int(binascii.hexlify("YELLOW SUBMARINE"),16))[2:]
key_cipher = AES.new(key, AES>MODE_ECB)
ans =key_cipher.decrypt(x)

print ans
