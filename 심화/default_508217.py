import hashlib
import binascii

# Case 1 :
# directly input time and bits hex type

# 1. Getting header values from blockexplorer.com
# Block Header Element = { Version, PrevBlock, MerkleRoot, Time, Bits, Nonce }

version = "20000000" #2

hash_PrevBlock = "00000000000000000060e66690d8a6646b7f8bb4aeb3fa7be258ae4011e362b5"
hash_MerkleRoot = "98f0bb94fc154733f22ac54994e9637981900fcee8a0db7d5880b5b79ca3853d"

time = "5A7BEAA4"
# Must convert to Hex : 5A7BEAA4
bits = "1761E9F8"
# Must convert to Hex : 1761E9F8
nonce = 2699712111                      # In decimal notation
nonce = hex(int(0x100000000)+nonce)[-8:]

# 2. Convert them in little-endian hex notation

version = binascii.hexlify(binascii.unhexlify(version)[::-1])
hash_PrevBlock = binascii.hexlify(binascii.unhexlify(hash_PrevBlock)[::-1])
hash_MerkleRoot = binascii.hexlify(binascii.unhexlify(hash_MerkleRoot)[::-1])
time = binascii.hexlify(binascii.unhexlify(time)[::-1])
bits = binascii.hexlify(binascii.unhexlify(bits)[::-1])
nonce = binascii.hexlify(binascii.unhexlify(nonce)[::-1])

# 3. Concatenating header values

header = version + hash_PrevBlock + hash_MerkleRoot + time + bits + nonce

# 4. Taking the double-SHA256 hash value

header = binascii.unhexlify(header)
hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
hash = binascii.hexlify(hash)

# 5. Converting the hash value in big-endian hex notation

hash = binascii.hexlify(binascii.unhexlify(hash)[::-1])
print  hash
