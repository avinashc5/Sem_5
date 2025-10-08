from hashlib import sha256
import random
import string

FLAG = "REDACTED"
DATA = ''.join(random.choices(string.printable, k=64)).encode()

class MerkleTree:
    class _Node:
        def __init__(self, hash):
            self.hash = hash
            self.left = None
            self.right = None
    
    def __init__(self, data):
        self.data = data

        # Simplification for this challenge, not needed in general:
        assert((len(data) & (len(data)-1) == 0) and len(data) != 0) # Checks that len(data) is an integral power of 2

        self.root = self._build_tree(data)

    def _build_tree(self, data):
        if len(data) == 1:
            return self._Node(sha256(data).digest())
        else:
            left = self._build_tree(data[:len(data)//2])
            right = self._build_tree(data[len(data)//2:])
            node = self._Node(sha256(left.hash + right.hash).digest())
            node.left = left
            node.right = right
            return node
    
    def get_root_hash(self):
        return self.root.hash
    
    def get_proof(self, index):
        proof = []
        self._get_proof(self.root, 0, len(self.data), index, proof)
        return (self.data[index], proof)
    
    def _get_proof(self, node, start, end, index, proof):
        mid = (start+end)//2
        if node.left is None:
            return
        if index < mid:
            # print("R")
            proof.append(node.right.hash)
            self._get_proof(node.left, start, mid, index, proof)
        else:
            # print("L")
            proof.append(node.left.hash)
            self._get_proof(node.right, mid, end, index, proof)


if __name__ == "__main__":
    mtree = MerkleTree(DATA)
    print(f"Data Length: {len(DATA)}")
    print(f"Root Hash: {mtree.get_root_hash().hex()}")

    for _ in range(len(DATA)//4):
        try:
            idx = int(input(f"Enter index 0-{len(DATA)-1}: "))
            if 0 <= idx < len(DATA):
                val, proof = mtree.get_proof(idx)
                print(f"Value: {val}")
                print(f"Proof: {[proof_element.hex() for proof_element in proof]}")
            else:
                print("Invalid index")
                exit(1)
        except ValueError:
            print("Invalid input")
            exit(1)

    data_guess = bytes.fromhex(input("\nEnter data (in hex): "))
    if data_guess == DATA:
        print(f"Here's your flag: {FLAG}")
    else:
        print(DATA)
        print("Don't you understand that this is secure?")
