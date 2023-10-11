from hashlib import md5

def encrypt(plaintext, key):
    key = md5(key).digest()
    msg = plaintext + b'|' + key
    # print(msg)
    encrypted = b'K'
    for i in range(len(msg)):
        encrypted += bytes([(msg[i] + key[i%len(key)]  + encrypted[i]) & 0xff])
    return encrypted.hex()

flag = b"KMA{anh xoa di roi}"
key = b"anh xoa di roi"
ciphertext = encrypt(flag, key)
print(ciphertext)
# 4b851cc4cdd1c7a3b7a3d83095a46a320e6b21e9e5afab7b8869d930c9cd981a0523a037faca8425f9a921c6ebca8f7087f8aab5bc53fe9cd5acfa9e