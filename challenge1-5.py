import binascii
from Crypto.Util.strxor import strxor_c

def xor_cipher(input,key):
        text = input
        key_hex = key
        length_text = len(text)
        length_key = len(key)
        i = 0
        cipher= b''
        for i in range(length_text):
                cipher+= str(strxor_c(text[i],key_hex[i%length_key]))
        return cipher

input = raw_input("Enter String: ")
key = "ICE"
ans=xor_cipher(input.encode('hex'),key.encode('hex'))
print ans
