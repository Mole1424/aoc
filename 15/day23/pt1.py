from pathlib import Path

registry = {"a": 0, "b": 0}

with Path("input.txt").open() as f:
    instructions = f.read().splitlines()

current_index = 0

while current_index < len(instructions):
    opcode, args = instructions[current_index].split(" ", 1)

    if opcode == "hlf":
        registry[args] //= 2
    elif opcode == "tpl":
        registry[args] *= 3
    elif opcode == "inc":
        registry[args] += 1
    elif opcode == "jmp":
        current_index += int(args)
        continue
    elif opcode == "jie":
        r, offset = args.split(", ")
        if registry[r] % 2 == 0:
            current_index += int(offset)
            continue
    elif opcode == "jio":
        r, offset = args.split(", ")
        if registry[r] == 1:
            current_index += int(offset)
            continue

    current_index += 1

print(registry["b"])
