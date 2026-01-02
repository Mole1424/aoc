from pathlib import Path

with Path("input.txt").open() as f:
    strings = f.read().splitlines()

total_len = 0
compiled_len = 0

for string in strings:
    total_len += len(string)
    string = string.removeprefix('"').removesuffix('"')
    previous_char = ""
    current_slash = False
    string_len = 0
    for current_char in string:
        string_len += 1

        if current_char == "\\":
            if current_slash:
                string_len -= 1
                current_slash = False
            else:
                current_slash = True
        elif current_slash:
            if current_char == "x":
                string_len -= 3  # account for future \x.. and we've already plussed one
            else:
                string_len -= 1
            current_slash = False
        previous_char = current_char
    compiled_len += string_len

print(total_len - compiled_len)
