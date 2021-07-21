from Crypto.Cipher import AES
import scrypt, os, binascii


def encrypt_AES_GCM(msg, password):
    kdfSalt = os.urandom(16)
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return kdfSalt, ciphertext, aesCipher.nonce, authTag


def decrypt_AES_GCM(encryptedMsg, password):
    (kdfSalt, ciphertext, nonce, authTag) = encryptedMsg
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext


msg = b'Message for AES-256-GCM + Scrypt encryption'
password = b's3kr3tp4ssw0rd'
encryptedMsg = encrypt_AES_GCM(msg, password)
print("encryptedMsg", {
    'kdfSalt': binascii.hexlify(encryptedMsg[0]),
    'ciphertext': binascii.hexlify(encryptedMsg[1]),
    'aesIV': binascii.hexlify(encryptedMsg[2]),
    'authTag': binascii.hexlify(encryptedMsg[3])
})

decryptedMsg = decrypt_AES_GCM(encryptedMsg, password)
print("decryptedMsg", decryptedMsg)

"""
The above code encrypts using AES-256-GCM given text message by given text password.
During the encryption, the Scrypt KDF function is used (with some fixed parameters) to derive a secret key from the
password. 
The randomly generated KDF salt for the key derivation is stored together with the encrypted message and will 
be used during the decryption. Then the input message is AES-encrypted using the secret key and the output consists
of ciphertext + IV (random nonce) + authTag. The final output holds these 3 values + the KDF salt.
During the decryption, the Scrypt key derivation (with the same parameters) is used to derive the same secret
key from the encryption password, together with the KDF salt (which was generated randomly during the encryption). 
Then the ciphertext is AES-decrypted using the secret key, the IV (nonce) and the authTag. In case of success, 
the result is the decrypted original plaintext. In case of error, the authentication tag will fail to authenticate 
the decryption process and an exception will be thrown.
"""