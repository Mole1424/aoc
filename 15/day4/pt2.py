from pathlib import Path
from hashlib import md5

with Path("input.txt").open() as f:
    secret_key = f.readline().strip()

i = 0
while True:
    i = i + 1
    input = secret_key + str(i)
    hash = md5(input.encode()).digest()
    if hash[:3] == b"\x00\x00\x00":
        print(i)
        break
