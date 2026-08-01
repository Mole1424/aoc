from functools import cache
from pathlib import Path


# pls say this sequence cycles
@cache
def calcualte_next(previous):
    return (previous * 252533) % 33554393


with Path("input.txt").open() as f:
    x, y = map(int, f.readline().strip().split(" "))

row = 1
column = 1
current = 20151125
while not (row == x and column == y):
    print(row, column)
    if row == 1:
        row = column + 1
        column = 1
    else:
        row -= 1
        column += 1

    current = calcualte_next(current)

print(current)
