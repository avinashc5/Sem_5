from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor

HOST = "0.cloud.chals.io"
PORT = 32703

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


recvuntil("originally assigned: ")
original_mac = recvline().strip()
recvuntil("secret: ")
iv = recvline().strip()

# ===== YOUR CODE BELOW =====
# The variable "orginal_mac" contains the MAC digest (as a hex string) of the credentials you were originally assigned
# The variable "iv" contains the IV (as a hex string) used to generate the MAC
# Set the data (in hex) you want to send to Möbius Hacker in the variable "mobius_data"

mobius_data = None
# ===== YOUR CODE ABOVE =====

recvuntil("(in hex) > ")
sendline(mobius_data)
recvuntil("(in hex) --> ")
mobius_mac = recvline().strip()

# ===== YOUR CODE BELOW =====
# The variable "orginal_mac" contains the MAC digest (as a hex string) of the credentials you were originally assigned
# The variable "iv" contains the IV (as a hex string) used to generate the MAC
# The variable "mobius_mac" contains the MAC digest (as a hex string) of the message you sent to Möbius Hacker
# Set the credetials to be sent to the server in the variables "creds"
# Set the mac to be sent to the server in the variable "forged_mac"

creds = None
forged_mac = None
# ===== YOUR CODE ABOVE =====

recvuntil("idenitity credentials to access the system (in hex): ")
sendline(creds)

recvuntil("MAC of your credentials (in hex): ")
sendline(forged_mac)

recvline()
recvline()

target.close()
