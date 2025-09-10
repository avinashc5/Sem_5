from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

FLAG = "REDACTED"

HEADER = "_Have you heard about the \{quick\} brown fox which jumps over the lazy dog?\n__The decimal number system uses the digits 0123456789!\n___The flag is: "

def new_encrypt(key: bytes, plaintext: str) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    modified_plaintext = ''.join([char*AES.block_size for char in plaintext]).encode()
    return cipher.encrypt(modified_plaintext)

if __name__ == '__main__':
    with open("ciphertext.bin", 'wb') as f:
        f.write(new_encrypt(get_random_bytes(16), HEADER+FLAG))

