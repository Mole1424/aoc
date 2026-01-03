from pathlib import Path
import re

with Path("input.txt").open() as f:
    json = f.read().strip()

numbers = re.findall(r"-?\d+", json)
print(sum(int(n) for n in numbers))
