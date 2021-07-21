import os
import binascii
import time
from datetime import datetime
from chacha20poly1305 import ChaCha20Poly1305

key_first_health_camp = os.urandom(32)
cip_first_health_camp = ChaCha20Poly1305(key_first_health_camp)

key_patient_profile = os.urandom(32)
cip_patient_profile = ChaCha20Poly1305(key_patient_profile)

# First health camp attendance data to text

First_healthcamp_csv_path = r"C:\Users\ACER\PycharmProjects\intership\working\Train\First_Health_Camp_Attended.csv"
"""textFirst_Health_Camp = open(First_healthcamp_csv_path, "r")
textFirst_Health_Camp = ' '.join([i for i in textFirst_Health_Camp])
textFirst_Health_Camp = textFirst_Health_Camp.replace(",", " ")"""

# Patient Profile data converted to text

Patient_Profile_csv_path = r"C:\Users\ACER\PycharmProjects\intership\working\Train\Patient_Profile.csv"
textPatient_Profile = open(Patient_Profile_csv_path, "r")
textPatient_Profile = ' '.join([i for i in textPatient_Profile])
textPatient_Profile = textPatient_Profile.replace(",", " ")

# conversion of text data to binary
binary_patient_profile_data = str.encode(textPatient_Profile)

keytext_path = r"C:\Users\ACER\PycharmProjects\intership\working\key.txt"
with open(keytext_path, 'wb') as file_object:
    file_object.write(key_patient_profile)

nonce = os.urandom(12)
nonce_path = r'C:\Users\ACER\PycharmProjects\intership\working\nonce.txt'
with open(nonce_path, 'wb') as file_nonce:
    file_nonce.write(nonce)

start = time.process_time()
starttime = datetime.now()
ciphertext = cip_patient_profile.encrypt(nonce, binary_patient_profile_data)
print("time taken for encryption: ", time.process_time() - start)
print("\ntime taken in date time mode: ", datetime.now()-starttime)

# storing the data in text file
encrypt_path = r'C:\Users\ACER\PycharmProjects\intership\working\encrypted.txt'
with open(encrypt_path, 'wb') as encrypt_file:
    encrypt_file.write(ciphertext)

print("data stored")
