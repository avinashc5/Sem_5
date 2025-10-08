from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

FLAG = "REDACTED"

KEY = get_random_bytes(16)
IV = get_random_bytes(16)


def cbc_mac(key, iv, data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(data)[-AES.block_size:]


if __name__ == "__main__":
    DATA = b"user=cs409learner&password=V3ry$3cur3p455"
    MAC = cbc_mac(KEY, IV, pad(DATA, AES.block_size))

    print("Welcome to the gates of the Security Variance Authority!")
    print(f"Here is a MAC of the credentials you were originally assigned: {MAC.hex()}")
    print(f"You've been provided the IV because we don't intend to keep it a secret: {IV.hex()}\n")

    print(f"Möbius Hacker: Psst, I managed to secure you one usage of MAC generation with the key for any message of your choice.")
    print(f"Möbius Hacker: However, do not let your original credentials be any part of this message, else your identity could be discovered and the Security-Hunters will prune you.")
    hacked_data = bytes.fromhex(
        input(f"Möbius Hacker: Give your message (in hex) > "))
    if DATA in hacked_data:
        print("Möbius Hacker: I should have known better than to trust you.")
        exit(1)
    print(f"Möbius Hacker: Generating the MAC of your message, hold on a minute...")
    print(
        f"Möbius Hacker: Here's your MAC (in hex) --> {cbc_mac(KEY, IV, hacked_data).hex()}\n")

    credentials = bytes.fromhex(input(
        "Hello Variant, please enter your idenitity credentials to access the system (in hex): "))
    if not credentials.startswith(DATA):
        print("Invalid credentials")
        exit(1)

    input_mac = bytes.fromhex(input(
        "To ensure you've recevied the credentials on discretion of the Security-Keepers, enter the MAC of your credentials (in hex): "))
    if input_mac != cbc_mac(KEY, IV, credentials):
        print(cbc_mac(KEY, IV, credentials))
        print("Incorrect MAC")
        exit(1)

    if b"admin=true" in credentials:
        print(f"\nMs. SecureHours: Hey y'all! Here's your flag --> {FLAG}")
    else:
        print("\nMs. SecureHours: You're inside the SVA, Variant.")
