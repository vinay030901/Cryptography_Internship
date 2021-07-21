import binascii
import os
import time

from Crypto.Cipher import AES


def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    cipherText, authTag = aesCipher.encrypt_and_digest(msg)
    return cipherText, aesCipher.nonce, authTag


def decrypt_AES_GCM(encryptedMsg, secretKey):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext


secretKey = os.urandom(32)  # 256-bit random encryption key
print("Encryption key:", binascii.hexlify(secretKey))

msg = b'this is the text to be converted or encrypted for safety purposes'
start=time.process_time()
encryptedMsg = encrypt_AES_GCM(msg, secretKey)
print("encryption time: ", time.process_time()-start)
print("encryptedMsg", {
    'ciphertext': binascii.hexlify(encryptedMsg[0]),
    'aesIV': binascii.hexlify(encryptedMsg[1]),
    'authTag': binascii.hexlify(encryptedMsg[2])
})

decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
print("decryptedMsg", decryptedMsg)

"""The AES-GCM encryption takes as input a message + encryption key and produces as output a set of values:
 { ciphertext + nonce + authTag }.
The ciphertext is the encrypted message.
The nonce is the randomly generated initial vector (IV) for the GCM construction.
The authTag is the message authentication code (MAC) calculated during the encryption.
The encryption key size generated in the above code is 256 bits (32 bytes) and it configures the AES-GCM 
cipher as AES-256-GCM. If we change the key size to 128 bits or 192 bits, we shall use AES-128-GCM or
 AES-192-GCM respectively."""