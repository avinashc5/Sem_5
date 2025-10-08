from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from hashlib import md5
from tqdm import tqdm

class MyCustomHash:
    block_size = 4 # in bytes
    iv = b"\x42"*block_size

    def __init__(self):
        self.data = None
    
    def update(self, data: bytes):
        self.data = pad(data, MyCustomHash.block_size)
    
    @staticmethod
    def _compress(chain: bytes, block: bytes) -> bytes:
        return md5(chain + block).digest()[:MyCustomHash.block_size]

    def digest(self) -> bytes:
        chain_value = self.iv
        for idx in range(0, len(self.data), MyCustomHash.block_size):
            block = self.data[idx:idx+MyCustomHash.block_size]
            chain_value = MyCustomHash._compress(chain_value, block)
        return chain_value
    
    def hexdigest(self) -> str:
        return self.digest().hex()



def generate_colliding_message_blocks(hash1, hash2):
    chain1_hashmap = set()
    chain1_rdict = {}
    for i in range(2**(MyCustomHash.block_size*4)):
        msg_block = int.to_bytes(i, MyCustomHash.block_size, 'big')
        chain_output = MyCustomHash._compress(hash1, msg_block)
        chain1_hashmap.add(chain_output)
        chain1_rdict[chain_output] = msg_block
    
    for i in range(2**(MyCustomHash.block_size*8)):
        msg_block = int.to_bytes(i, MyCustomHash.block_size, 'big')
        chain_output = MyCustomHash._compress(hash2, msg_block)
        if chain_output in chain1_hashmap:
            return chain1_rdict[chain_output], msg_block, chain_output
    
    return None, None, None


# Diamond Structure Generation
num_layers = 17
hash_blocks = None
edge_blocks = None

CACHED = False

if CACHED:
    hash_blocks = eval(open("hblocks.data", 'r').read())
    edge_blocks = eval(open("eblocks.data", 'r').read())
else:
    hash_blocks = []
    edge_blocks = []
    for i in range(num_layers):
        hash_blocks.append([None]*2**(num_layers-1-i))
        if i != num_layers-1:
            edge_blocks.append([None]*2**(num_layers-1-i))

    # Generate the 0th layer
    for idx in range(len(hash_blocks[0])):
        hash_blocks[0][idx] = get_random_bytes(MyCustomHash.block_size)

    # Generate the intermediate layers
    for layer in range(1, num_layers):
        print(f"[+] On Layer {layer}:")
        for idx in tqdm(range(len(hash_blocks[layer]))):
            hash1 = hash_blocks[layer-1][idx*2]
            hash2 = hash_blocks[layer-1][idx*2+1]
            msg_block1, msg_block2, chain_output = generate_colliding_message_blocks(hash1, hash2)
            hash_blocks[layer][idx] = chain_output
            edge_blocks[layer-1][idx*2] = msg_block1
            edge_blocks[layer-1][idx*2+1] = msg_block2

    with open("hblocks.data", 'w') as f:
        f.write(str(hash_blocks))

    with open("eblocks.data", 'w') as f:
        f.write(str(edge_blocks))