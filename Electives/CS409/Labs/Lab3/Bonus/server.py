from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Random.random import randint
from hashlib import md5

FLAG = "REDACTED"

class LightHash:
    block_size = 4 # in bytes
    iv = b"\x42"*block_size

    def __init__(self):
        self.data = None
    
    def update(self, data: bytes):
        self.data = pad(data, LightHash.block_size)
    
    @staticmethod
    def _compress(chain: bytes, block: bytes) -> bytes:
        return md5(chain + block).digest()[:LightHash.block_size]

    def digest(self) -> bytes:
        chain_value = self.iv
        for idx in range(0, len(self.data), LightHash.block_size):
            block = self.data[idx:idx+LightHash.block_size]
            chain_value = LightHash._compress(chain_value, block)
        return chain_value
    
    def hexdigest(self) -> str:
        return self.digest().hex()



if __name__ == "__main__":
    target_hash = None
    try:
        target_hash = bytes.fromhex(input("Give me your target hash (in hex): "))
    except ValueError:
        print("Invalid input")
        exit(1)
    if len(target_hash) != LightHash.block_size:
        print("Invalid hash")
        exit(1)

    NUM_TRIALS = 100
    HASHER = LightHash()
    for trial_idx in range(NUM_TRIALS):
        print(f"Trial [{trial_idx+1}/{NUM_TRIALS}]")
        custom_prefix_length = randint(2*LightHash.block_size, 32*LightHash.block_size)
        custom_prefix = get_random_bytes(custom_prefix_length)
        print(f"Custom Prefix: {custom_prefix.hex()}")
        
        msg = None
        try:
            msg = bytes.fromhex(input("Enter your message: "))
        except ValueError:
            print("Invalid input")
            exit(1)
        
        if not msg.startswith(custom_prefix):
            print("Message does not start with custom prefix!")
            exit(1)
        
        HASHER.update(msg)
        if HASHER.digest() != target_hash:
            print(f"Incorrect hash! Target not achieved!")
            exit(1)
        
        print("")
    

    print(f"You've proved your worth! Here's your flag: {FLAG}")
