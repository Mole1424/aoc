from pathlib import Path

with Path("input.txt").open() as f:
    rooms = f.read().splitlines()

sector_ids = 0

for room in rooms:
    name, metadata = room.rsplit("-", 1)
    sector_id, checksum = metadata.split("[")

    checksum = checksum.replace("]", "")
    name = name.replace("-", "")

    # sort by count, then alphabet
    sorted_name = "".join(sorted(name, key=lambda c: (-name.count(c), c)))
    # remove duplicates
    sorted_name = "".join(dict.fromkeys(sorted_name))

    if sorted_name[:5] == checksum:
        sector_ids += int(sector_id)

print(sector_ids)
