from pathlib import Path

with Path("input.txt").open() as f:
    number = f.readline().strip()

for _ in range(40):
    new_num_parts = []
    num_count = 1
    repearing_num = number[0]

    for digit in number[1:]:
        if digit == repearing_num:
            num_count += 1
        else:
            new_num_parts.append(str(num_count))
            new_num_parts.append(repearing_num)
            repearing_num = digit
            num_count = 1

    new_num_parts.append(str(num_count))
    new_num_parts.append(repearing_num)

    number = "".join(new_num_parts)

print(len(number))
