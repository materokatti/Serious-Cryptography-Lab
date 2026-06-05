from os import urandom

KEY_SIZE = 16


def rc4_init(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def rc4_crypt(key, data):
    S = rc4_init(key)
    i = j = 0
    result = bytearray()
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(byte ^ k)
    return bytes(result)


# Pick a random 16-byte key.
k = urandom(KEY_SIZE)
print(f"k = {k.hex()}")

# Set plaintext p.
p = b"Hello, RC4 stream cipher!"
print(f"p = {p.decode()}")

# Encrypt: XOR plaintext with the keystream generated from k.
c = rc4_crypt(k, p)
print(f"enc({p.hex()}) = {c.hex()}")

# Decrypt: the same XOR operation with the same key recovers p.
p_dec = rc4_crypt(k, c)
print(f"dec({c.hex()}) = {p_dec.hex()}")

# A different key produces a different ciphertext for the same plaintext.
k2 = urandom(KEY_SIZE)
print(f"k2 = {k2.hex()}")
c2 = rc4_crypt(k2, p)
print(f"enc({p.hex()}) = {c2.hex()}")
