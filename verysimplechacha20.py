import os
from chacha20poly1305 import ChaCha20Poly1305
import time

key = os.urandom(32)
cip = ChaCha20Poly1305(key)

nonce = os.urandom(12)
start = time.process_time()
ciphertext = cip.encrypt(nonce, b'this is the text to be converted or encrypted for safety purposes')
print("time taken for encryption: ", time.process_time()-start)

startd = time.process_time()
plaintext = cip.decrypt(nonce, ciphertext)
print("time taken for decryption: ", time.process_time()-startd)
print(plaintext)