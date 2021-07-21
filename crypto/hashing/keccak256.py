from Crypto.Hash import keccak
import binascii


keccak256 = keccak.new(data=b'hello', digest_bits=256).digest()
print("keccak256('hello') -- ", binascii.hexlify(keccak256))
