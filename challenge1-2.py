from Crypto.Util.strxor import strxor

var1 = raw_input("First hex: ")
var2 = raw_input("Second hex: ")

out = strxor(var1.decode('hex'), var2.decode('hex')).encode('hex')

print out
