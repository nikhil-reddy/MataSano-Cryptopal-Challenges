def PKCS7(text):
	# text = raw_input("Enter String: ")
	l = len(text)
	k = 20
	val = k-(l % k)
	for i in xrange(val):
		text += '/'
		text += str(hex(val))

	return text

print PKCS7('YELLOW SUBMARINE')
