input = 29000000
rough_bound = input // 10
num_presents = [0] * (rough_bound + 1)

for elf in range(1, rough_bound + 1):
    for house in range(elf, rough_bound + 1, elf):
        num_presents[house] += elf * 10

        if num_presents[house] >= input:
            print(house)
            exit()
