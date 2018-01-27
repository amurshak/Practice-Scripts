#Encryption by Alex Murshak
#Encrypts a given string
#Decrypts a given string accordingly.

encrypt = input('Enter text to encrypt : ')
encrypt = encrypt.lower().replace(" ", "")

empty = []
for i in encrypt:
    empty.append(chr(ord(i) + 2))

print(empty)
decrypt = input('Enter text to decrypt : ')
decrypt = decrypt.lower().replace(" ", "")
for i in decrypt:
    print(chr(ord(i) - 2))

