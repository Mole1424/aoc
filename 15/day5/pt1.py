from pathlib import Path

with Path("input.txt").open() as f:
    strings = f.read().splitlines()

num_nice = 0
for string in strings:
    previous_char = ""
    num_vowels = 0
    double_letter = False
    no_disallowed = True
    for current_char in string:
        if current_char in "aeiou":
            num_vowels += 1
        if current_char == previous_char:
            double_letter = True
        if previous_char + current_char in ("ab", "cd", "pq", "xy"):
            no_disallowed = False
            break
        previous_char = current_char
    num_nice += num_vowels >= 3 and double_letter and no_disallowed

print(num_nice)
