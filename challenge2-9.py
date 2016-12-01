def PKCS7(text):
	# text = raw_input("Enter String: ")
	l = len(text)
	k = 20
	val = k-(l % k)
	for i in xrange(val):
		text += '/0x4'

	return text

print PKCS7('YELLOW SUBMARINE')
