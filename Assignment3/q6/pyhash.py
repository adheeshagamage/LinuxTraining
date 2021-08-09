import sys
import hashlib

paswd = bytes(str(sys.argv[1]),'utf-8')
hashValue = hashlib.pbkdf2_hmac(hash_name='sha512',password=paswd,salt=b'Km5d5ivMy8iexuHcZrsD',iterations=200000)
print(hashValue.hex())
