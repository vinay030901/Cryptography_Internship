import os
import binascii
from chacha20poly1305 import ChaCha20Poly1305

key = os.urandom(32)
cip = ChaCha20Poly1305(key)

csv_path = r"C:\Users\ACER\PycharmProjects\intership\Train\Patient_Profile.csv"
text = open(csv_path, "r")
text = ' '.join([i for i in text])
text = text.replace(",", " ")
# print(text)

keytext = r"C:\Users\ACER\PycharmProjects\intership\key.txt"
with open(keytext, 'wb') as file_object:
    file_object.write(key)

with open(keytext, 'rb') as file1:
    sendkey = file1.read()
print(binascii.hexlify(sendkey))
binarytxt = str.encode(text)
# print(binarytxt)


nonce = os.urandom(12)
ciphertext = cip.encrypt(nonce, binarytxt)
print(binascii.hexlify(ciphertext))

cip = ChaCha20Poly1305(sendkey)
plaintext = cip.decrypt(nonce, ciphertext)
print(plaintext)
