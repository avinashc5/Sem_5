from pwn import *
from hashlib import sha256

HOST = "0.cloud.chals.io"
PORT = 12145

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


def get_proof(index: int) -> tuple[int, list[str]]:
    recvuntil(f"-{DATA_LEN-1}: ")
    sendline(str(index))
    recvuntil("Value: ")
    val = int(recvline().strip())
    recvuntil("Proof: ")
    proof = eval(recvline().strip())
    return val, proof


recvuntil("Data Length: ")
DATA_LEN = int(recvline().strip())
recvuntil("Root Hash: ")
ROOT_HASH = recvline().strip()

# ===== YOUR CODE BELOW =====
# You can use the function "get_proof(index : int) -> tuple[int, list[str]]" to retrieve the ASCII value of the character at the specified index and a list of hexstrings of the proof
# Set the data variable to your guess of data (in bytes)
# The variable "DATA_LEN" stores the length of the flag
# The variable "ROOT_HASH" stores the root hash of the Merkle Tree

data = None
# ===== YOUR CODE ABOVE =====

recvuntil("(in hex): ")
sendline(data.hex())

recvline()

target.close()
