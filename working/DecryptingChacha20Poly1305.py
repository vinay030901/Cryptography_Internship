import os
import binascii
import time
from datetime import datetime
from chacha20poly1305 import ChaCha20Poly1305

keytext = r"C:\Users\ACER\PycharmProjects\intership\working\key.txt"
with open(keytext, 'rb') as file1:
    sendkey = file1.read()

encrypt_data_path = r'C:\Users\ACER\PycharmProjects\intership\working\encrypted.txt'
with open(encrypt_data_path, 'rb') as file2:
    patient_profile_data = file2.read()

nonce_path = r'C:\Users\ACER\PycharmProjects\intership\working\nonce.txt'
with open(nonce_path, 'rb') as object1:
    nonce = object1.read()

cip = ChaCha20Poly1305(sendkey)
decrypt_path = r'C:\Users\ACER\PycharmProjects\intership\working\decrypted.txt'

start = time.process_time()
starttime = datetime.now()
plaintext = cip.decrypt(nonce, patient_profile_data)
print("time taken for decryption: ", time.process_time() - start)
print("time in date time mode: ", datetime.now() - starttime)

with open(decrypt_path, 'wb') as filewrite:
    filewrite.write(plaintext)
print("file written")
