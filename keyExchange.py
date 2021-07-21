from tinyec import registry
import secrets


def compress(pubkey):
    return hex(pubkey.x) + hex(pubkey.y % 2)[2:]


curve = registry.get_curve('brainpoolP256r1')

alicePrivateKey = secrets.randbelow(curve.field.n)
alicePublicKey = alicePrivateKey * curve.g
print("Alice public key is: ", compress(alicePublicKey))

bobPrivateKey = secrets.randbelow(curve.field.n)
bobPublicKey = bobPrivateKey * curve.g
print("Bob public key is: ", compress(bobPublicKey))

print("Now exchange of public keys through internet")

aliceSharedKey = alicePrivateKey * bobPublicKey
bobSharedKey = bobPrivateKey * alicePublicKey

print("Alice shared key is: ", compress(aliceSharedKey))
print("Bob shared key is: ", compress(bobSharedKey))

print("Both shared keys are equal: ", aliceSharedKey == bobSharedKey)
