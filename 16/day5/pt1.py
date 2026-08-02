from hashlib import md5
from pathlib import Path

with Path("input.txt").open() as f:
    door_id = f.readline().strip()

password = ""
index = 0
while True:
    hash = md5((door_id + str(index)).encode()).hexdigest()

    if hash.startswith("00000"):
        password += hash[5]
        if len(password) == 8:
            break

    index += 1

print(password)
