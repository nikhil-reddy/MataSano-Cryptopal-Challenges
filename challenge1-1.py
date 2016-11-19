var = raw_input("Please enter hex: ")

decode_base64 = var.decode('hex').encode('base64')

print decode_base64
