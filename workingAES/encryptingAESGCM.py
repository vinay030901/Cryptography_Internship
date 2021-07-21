import binascii
import os
import time
from datetime import datetime
from Crypto.Cipher import AES


def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    cipherText, authTag = aesCipher.encrypt_and_digest(msg)
    return cipherText, authTag


secretKey = os.urandom(32)  # 256-bit random encryption key
aesCipher = AES.new(secretKey, AES.MODE_GCM)
key_path = r'C:\Users\ACER\PycharmProjects\intership\workingAES\key.txt'
with open(key_path, 'wb') as key_object:
    key_object.write(secretKey)

Patient_Profile_csv_path = r"C:\Users\ACER\PycharmProjects\intership\workingAES\Train\Patient_Profile.csv"
textPatient_Profile = open(Patient_Profile_csv_path, "r")
textPatient_Profile = ' '.join([i for i in textPatient_Profile])
textPatient_Profile = textPatient_Profile.replace(",", " ")

# conversion of text data to binary
binary_patient_profile_data = str.encode(textPatient_Profile)

start=time.process_time()
startdate = datetime.now()
encryptedMsg = encrypt_AES_GCM(binary_patient_profile_data, secretKey)
print("time for encryption: ", time.process_time()-start)
print("time for encryption: ", datetime.now()-startdate)
encrypt_path = r'C:\Users\ACER\PycharmProjects\intership\workingAES\encryptedAES.txt'
with open(encrypt_path,'wb') as encrypt_object:
    encrypt_object.write(encryptedMsg[0])
print("encrypted successfully")

