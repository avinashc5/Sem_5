from pwn import *
import time

HOST = "0.cloud.chals.io"
PORT = 30216

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


def send_guess(hmac_guess : str) -> int:
    recvuntil("omniscience: ")
    sendline(hmac_guess)
    resp = recvline()
    if "omniscient" in resp:
        recvline()
        return 1
    else:
        return -1


recvuntil("of length ")
msg_len = int(recvuntil(" ")[:-1])

# ===== YOUR CODE BELOW =====
# The variable "msg_len" contains the length of the message that the server is asking for
# Set the message that you want to send to the server (in hex, as str) in the variable "msg"

msg = None
# ===== YOUR CODE ABOVE =====

recvuntil("in hex): ")
sendline(msg)

# ===== YOUR CODE BELOW =====
# Use the function "send_guess(hmac_guess : str) -> int" to send your guess of the first 10 hexchars of the hmac to the server
#   A return value of -1 indicates that your guess was incorrect
#   A return value of 1 indicates the your guess was correct


# ===== YOUR CODE ABOVE =====

target.close()
