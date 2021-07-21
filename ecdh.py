from tinyec import registry
import secrets

curve = registry.get_curve('brainpoolP256r1')


def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]


def ecc_calculate_encryption_keys(pubkey):
    cipherTextPrivKey = secrets.randbelow(curve.field.n)
    cipherTextPubKey = cipherTextPrivKey * curve.g
    sharedECCKey = cipherTextPrivKey * pubkey
    return sharedECCKey, cipherTextPubKey


def ecc_calculate_decryption(privKey, ciphertextPubKey):
    sharedECCKey = privKey * ciphertextPubKey
    return sharedECCKey


privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g
print("Private key: ", hex(privKey))
print("Public key: ", compress_point(pubKey))

(encryptKey, cipherTextPubKey) = ecc_calculate_encryption_keys(pubKey)
print("Cipher text public key: ", compress_point(cipherTextPubKey))
print("Encryption key: ", compress_point(encryptKey))

decryptKey = ecc_calculate_decryption(privKey, cipherTextPubKey)
print("Decryption key: ", compress_point(decryptKey))
