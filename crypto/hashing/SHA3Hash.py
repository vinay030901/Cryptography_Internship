import hashlib
import binascii

sha3_256hash = hashlib.sha3_256(b'hello').digest()
print("SHA3_256Hash('hello')-- ", binascii.hexlify(sha3_256hash))

"""digest function is the output of the hash function, 
for ex.- sha256 has a digest of 256 bits, i.e. its digest has a length of 32 bytes

b denotes a byte string, it is byte type instead of string type

hexlify(data) returns the hexadecimal representation of binary data"""