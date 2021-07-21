import binascii
import hashlib

sha256 = hashlib.sha256(b'hello champ').digest()
print("SHA256('hello champ') -- ", binascii.hexlify(sha256))

sha512 = hashlib.sha512(b'good morning').digest()
print("SHA512('good morning') -- ", binascii.hexlify(sha512))

keccak256 = hashlib.k
