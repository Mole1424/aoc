from hashlib import md5
from pathlib import Path

with Path("input.txt").open() as f:
    door_id = f.readline().strip()

# door_id = "abc"

password = [None, None, None, None, None, None, None, None]
index = 0
while True:
    hash = md5((door_id + str(index)).encode()).hexdigest()

    if hash.startswith("00000") and hash[5] in "01234567":
        if password[int(hash[5])] is None:
            password[int(hash[5])] = hash[6]
        if None not in password:
            break

    index += 1

print("".join(password))
