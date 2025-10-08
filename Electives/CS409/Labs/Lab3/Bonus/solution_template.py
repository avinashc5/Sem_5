from pwn import *
from hashlib import md5
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint
from tqdm import tqdm

HOST = "0.cloud.chals.io"
PORT = 13071

# Uncomment the 'process' line below when you want to test locally, uncomment the 'remote' line below when you want to execute your exploit on the server
# target = process(["python", "./server.py"])
target = remote(HOST, PORT)

def recvuntil(msg):
    resp = target.recvuntil(msg.encode()).decode()
    print(resp, end='')
    return resp

def sendline(msg):
    print(msg)
    target.sendline(msg.encode())

def recvline():
    resp = target.recvline().decode()
    print(resp, end='')
    return resp

def recvall():
    resp = target.recvall().decode()
    print(resp, end='')
    return resp



# ===== YOUR CODE BELOW =====
# Set your target hash (in hex) in the variable "target_hash"

target_hash = None
# ===== YOUR CODE ABOVE =====

recvuntil("Give me your target hash (in hex): ")
sendline(target_hash)

# ===== YOUR CODE BELOW =====
# Implement the function "get_cpft_message(prefix: bytes) -> bytes" to return a messgae which starts with the given prefix and has the same hash as the target hash

def get_cpft_message(prefix: bytes) -> bytes:
    pass
# ===== YOUR CODE ABOVE =====

NUM_TRIALS = 100
for _ in range(NUM_TRIALS):
    recvuntil("Custom Prefix: ")
    custom_prefix = bytes.fromhex(recvline())
    recvuntil("Enter your message: ")
    message = get_cpft_message(custom_prefix)
    sendline(message.hex())

recvline()
recvline()

target.close()
