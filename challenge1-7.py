import binascii
import base64
from Crypto.Cipher import AES

f_in = open('file1-7.txt', 'r')
ciphertext = base64.b64decode(f_in.read())

key = b'YELLOW SUBMARINE'
key_cipher = AES.new(key, AES.MODE_ECB)
ans = key_cipher.decrypt(ciphertext)
print ans
