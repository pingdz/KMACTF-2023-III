cipher = bytes.fromhex('4b851cc4cdd1c7a3b7a3d83095a46a320e6b21e9e5afab7b8869d930c9cd981a0523a037faca8425f9a921c6ebca8f7087f8aab5bc53fe9cd5acfa9e')

sumx = bytearray(b'')
for i in range(len(cipher) - 1):
    sumx.extend([(cipher[i+1] - cipher[i]) & 0xff])
sum = bytes(sumx)
key = [0] * 16
hint = b'KMA{'
for i in range(4):
    key[i] = ((sum[i] - hint[i]) & 0xff)
for i in range(11, 15):
    key[i] = ((sum[i + 32] - key[i-11]) & 0xff)
for i in range(5, 9):
    key[i] = ((sum[i + 43] - key[i-5]) & 0xff)
key[10] = ((sum[53] - key[5]) & 0xff)
key[15] = ((sum[58] - key[10]) & 0xff)
key[4] = ((sum[47] - key[15]) & 0xff)
key[9] = ((sum[52] - key[4]) & 0xff)
print('key:', key)
print('msg: ', end = '')
for i in range(len(sum)):
    print(chr((sum[i] - key[i % 16]) & 0xff), end = '')