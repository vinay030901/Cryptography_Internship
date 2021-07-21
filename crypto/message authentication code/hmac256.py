import hashlib
import hmac
import binascii

hmac256 = hmac.new(b'key', b'hello', hashlib.sha256).digest()
print("hmac256('hello') -- ", binascii.hexlify(hmac256))


def hmac_256(key, msg):
    return hmac.new(key, msg, hashlib.sha256).digest()


key = b"12345"
msg = b"vinay"

print("hmac: ", binascii.hexlify(hmac_256(key, msg)))
