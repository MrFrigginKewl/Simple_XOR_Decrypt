MyHexEncrypted = ['0x11', '0x03', '0x10', '0x17', '0x12']
# The hex values that have been encrypted with the string PASSWD.
XOR_KEY = "PASSWD"
# we have 5 hex values
# we have a 5 letter XOR Key

Encrypted_Decimal_Values = []
# create an empty list

for i in MyHexEncrypted:
	Encrypted_Decimal_Values.append(int(i,16))
print (Encrypted_Decimal_Values)
# loop through the HEX Values and convert them to Decimal.

decrypted_values = []
# create an empty list that will hold our decrypted values.

# below is sample code that presents an alternative way to do this
for i in range(len(Encrypted_Decimal_Values)):
    decrypted_value = Encrypted_Decimal_Values[i] ^ ord(XOR_KEY[i])
    decrypted_values.append(decrypted_value)

print("Decrypted Values Decimal:", decrypted_values)

print()
# create a line break for readability
print("PlainText String")
for i in decrypted_values:
	print(chr(i),end="")
	# convert each decimal value to ascii using the chr() method
