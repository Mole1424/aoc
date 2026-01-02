from pathlib import Path

with Path("input.txt").open() as f:
    strings = f.read().splitlines()

total_len = 0
encoded_len = 0

for string in strings:
    total_len += len(string)

    string_len = 2  # extra slashes for start and end chars

    for char in string:
        if char == "\\" or char == '"':
            string_len += 1
        string_len += 1
    encoded_len += string_len

print(encoded_len - total_len)
