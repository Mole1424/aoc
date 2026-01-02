from pathlib import Path
from functools import cache

circuit = {}
with Path("input.txt").open() as f:
    for line in f.read().splitlines():
        expression, target = line.split(" -> ")
        circuit[target] = expression


@cache
def compute(value) -> int:
    if value.isdigit():
        return int(value)

    expression = circuit[value].split()

    if len(expression) == 1:
        return compute(expression[0])
    elif len(expression) == 2:
        return (~compute(expression[1])) & 0xFFFF  # gah

    lhs, op, rhs = expression
    if op == "AND":
        return compute(lhs) & compute(rhs)
    elif op == "OR":
        return compute(lhs) | compute(rhs)
    elif op == "LSHIFT":
        return compute(lhs) << compute(rhs)
    else:
        return compute(lhs) >> compute(rhs)


print(compute("a"))
