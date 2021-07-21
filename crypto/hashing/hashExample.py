import hashlib
import binascii

text = 'Hello'
data = text.encode("utf8")

sha256 = hashlib.sha256(data).digest()
print("SHA256('Hello') -- ", binascii.hexlify(sha256))

sha3_256 = hashlib.sha3_256(data).digest()
print("SHA3_256('Hello') -- ", binascii.hexlify(sha3_256))

blake2s = hashlib.new('blake2s', data).digest()
print("blake2s('Hello') -- ", binascii.hexlify(blake2s))

ripemd160 = hashlib.new('ripemd160', data).digest()
print("ripemd160('Hello') -- ", binascii.hexlify(ripemd160))