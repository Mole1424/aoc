from pathlib import Path

with Path("input.txt").open() as f:
    password = list(map(lambda x: ord(x) - 97, f.readline().strip()))

invalid_chars = {ord("i") - 97, ord("o") - 97, ord("l") - 97}
while True:
    has_all_valid = any(c not in invalid_chars for c in password)

    has_straight = False
    if has_all_valid:
        for i in range(len(password) - 2):
            if (
                password[i] + 1 == password[i + 1]
                and password[i] + 2 == password[i + 2]
            ):
                has_straight = True
                break

    has_pairs = False
    if has_straight:
        pairs = {}
        i = 0
        while i < len(password) - 1:
            if password[i] == password[i + 1]:
                pairs[password[i]] = True
                i += 2
            else:
                i += 1
        if len(pairs) >= 2:
            has_pairs = True

    if has_all_valid and has_straight and has_pairs:
        break

    for i in range(len(password) - 1, -1, -1):
        password[i] += 1
        if password[i] >= 26:
            password[i] = 0
        else:
            break

print("".join(list(map(lambda x: chr(x + 97), password))))
