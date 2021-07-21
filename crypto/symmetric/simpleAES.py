import pyaes, pbkdf2, os,secrets, binascii

# derive a 256-bit key from the password
password = "Vinay@01"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print("key: ", binascii.hexlify(key))

# implementation of aes cipher
# Encrypt the plaintext with the given key:
# ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
iv = secrets.randbits(256)
plainText = "my name is Vinay"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
cipherText = aes.encrypt(plainText)
print("the encrypted cipher text is: ", binascii.hexlify(cipherText))
print("Length is: ", len(binascii.hexlify(cipherText)))

# Decrypt the ciphertext with the given key:
# plaintext = AES-256-CTR-Decrypt(ciphertext, key, iv)

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(cipherText)
print("The decrypted text is: ", decrypted)