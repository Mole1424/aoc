from pathlib import Path
from hashlib import md5

with Path("input.txt").open() as f:
    secret_key = f.readline().strip()

i = 0
while True:
    i = i + 1
    input = secret_key + str(i)
    hash = md5(input.encode()).hexdigest()
    if hash.startswith("00000"):
        print(i)
        break
