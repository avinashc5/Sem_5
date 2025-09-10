from pwn import *

HOST = "0.cloud.chals.io"
PORT = 19966

# Uncomment the 'process' line below when you want to test locally, uncomment the 'remote' line below when you want to execute your exploit on the server
target = process(["python", "./server.py"])
# target = remote(HOST, PORT)

def recvuntil(msg):
    resp = target.recvuntil(msg.encode()).decode()
    print(resp)
    return resp

def sendline(msg):
    print(msg)
    target.sendline(msg.encode())

def recvline():
    resp = target.recvline().decode()
    print(resp)
    return resp

def recvall():
    resp = target.recvall().decode()
    print(resp)
    return resp


recvuntil("IV: ")
IV = bytes.fromhex(recvline())

recvuntil("Flag: ")
flag_enc = bytes.fromhex(recvline())


def validate_padding(iv_hex: str, ciphertext_hex: str) -> bool:
    recvuntil("validated:\n")
    sendline(ciphertext_hex)
    recvuntil("IV:\n")
    sendline(iv_hex)
    response = recvline()
    valid_padding = ("Valid Padding!" in response)
    return valid_padding


# ===== YOUR CODE BELOW =====
# The variable IV has the iv (as a bytes object)
# The variable flag_enc has the ciphertext (as a bytes object)
# You can call the function validate_padding(iv_hex: str, ciphertext_hex: str) -> bool which takes in the hex of the iv (str) and hex of the ciphertext (str) and returns True if the corresponding plaintext has valid padding, and return False otherwise (as dictated by the server's response)

# ===== YOUR CODE BELOW =====

target.close()
