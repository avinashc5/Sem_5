import hmac
from hashlib import sha256
from Crypto.Random import get_random_bytes, random
from time import sleep

FLAG = "REDACTED"

hmac_key = get_random_bytes(16)

def compare_digests(dig1, dig2):
    if len(dig1) != len(dig2):
        return False
    for idx in range(len(dig1)):
        if dig1[idx] == dig2[idx]:
            sleep(1)
        else:
            return False
    return True

if __name__ == "__main__":
    msg_len = random.randint(32, 64)
    inp = bytes.fromhex(input(f"Give me any message of length {msg_len} (in hex): "))
    if len(inp) != msg_len:
        print("Invalid input length")
        exit(1)
    msg_hmac = hmac.new(hmac_key, inp, sha256).hexdigest()

    while True:
        inp_hex = input("Guess the first 10 characters of the HMAC hexdigest of your message to prove your omniscience: ")
        if compare_digests(msg_hmac[:10], inp_hex):
            print("Wow, you are omniscient!")
            print(f"Here's your flag: {FLAG}")
        else:
            print("Nope, that's not it")
        
