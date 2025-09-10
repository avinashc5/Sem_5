from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

FLAG = b"REDACTED"

key = get_random_bytes(AES.block_size)
iv = get_random_bytes(AES.block_size)


def validate_padding(iv_: bytes, ct: bytes) -> bool:
    cipher = AES.new(key, AES.MODE_CBC, iv=iv_)
    try:
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return True
    except:
        return False


if __name__ == "__main__":
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(FLAG, AES.block_size))

    print("Welcome to Padding Oracle Laboratories!")
    print("We let you know if your plaintext complies with PKCS#7 standards or not.")
    print("But you never get to see the plaintext anyway, so there's very little harm this info does.")
    print("Enjoy your stay at the lab!\n")

    print(f"IV: {iv.hex()}")
    print(f"Encrypted Flag: {ciphertext.hex()}\n")

    while True:
        print("Enter ciphertext (in hex) to be validated:")
        ct = bytes.fromhex(input())
        print("Enter the IV:")
        iv = bytes.fromhex(input())

        if validate_padding(iv, ct):
            print("Valid Padding!\n")
        else:
            print("Invalid Padding!\n")

    
    
