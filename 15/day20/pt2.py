input_target = 29000000
rough_bound = input_target // 11 * 2
num_presents = [0] * (rough_bound + 1)

for elf in range(1, rough_bound + 1):
    count = 0
    for house in range(elf, rough_bound + 1, elf):
        num_presents[house] += elf * 11
        count += 1
        if count == 50:
            break

for house, total in enumerate(num_presents):
    if total >= input_target:
        print(house)
        break
