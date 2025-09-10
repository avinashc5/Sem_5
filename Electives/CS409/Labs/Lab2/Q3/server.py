from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

FLAG = "REDACTED"

key = get_random_bytes(AES.block_size)

def validate_param_format(params: bytes) -> bool:
    return all([param.count(b'=') == 1 for param in params.split(b'&')])


if __name__ == "__main__":
    while True:
        choice = int(input("Do you want to 1) encrypt parameters, or 2) submit parameters: "))

        if choice == 1:
            params = input("Enter parameters: ").encode()
            if (not validate_param_format(params)) or (b"admin=true" in params):
                print("Malicious activity detected! Terminating...")
                exit(0)
            
            cipher = AES.new(key, AES.MODE_CBC, iv=key)
            ciphertext = cipher.encrypt(pad(params, AES.block_size))
            print(f"Encrypted parameters (hex): {ciphertext.hex()}\n")
        elif choice == 2:
            ciphertext = bytes.fromhex(input("Enter encrypted parameters (in hex): "))
            cipher = AES.new(key, AES.MODE_CBC, iv=key)
            params_padded = cipher.decrypt(ciphertext)
            params = ""
            try:
                params = unpad(params_padded, AES.block_size).decode()
            except:
                print("Invalid parameters! Incorrect padding or Non-ASCII characters detected!")
                print(f"Invalid Decryption Result (hex): {params_padded.hex()}\n")
                continue
            
            if "admin=true" in params:
                print("Welcome, admin!")
                cipher = AES.new(key, AES.MODE_CBC,iv=key)
                print(f"Here's your encrypted flag: {cipher.encrypt(pad(FLAG.encode(), AES.block_size)).hex()}")
                exit(0)
            else:
                print("Your parameters have been successfully submitted!\n")
        else:
            print("Invalid choice!")
            exit(0)
    
