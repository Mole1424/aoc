from pathlib import Path

with Path("input.txt").open() as f:
    rooms = f.read().splitlines()


def ceaser_cipher(encryped_name, shift):
    decrypted_name = ""

    for i in range(len(encryped_name)):
        if encryped_name[i] == "-":
            decrypted_name += " "
        else:
            decrypted_name += chr((ord(encryped_name[i]) + shift - 97) % 26 + 97)

    return decrypted_name


for room in rooms:
    name, metadata = room.rsplit("-", 1)
    sector_id, checksum = metadata.split("[")

    checksum = checksum.replace("]", "")

    # sort by count, then alphabet
    sorted_name = "".join(
        sorted(name.replace("-", ""), key=lambda c: (-name.count(c), c))
    )
    # remove duplicates
    sorted_name = "".join(dict.fromkeys(sorted_name))

    if sorted_name[:5] == checksum:
        decrypted_name = ceaser_cipher(name, int(sector_id))
        if (
            "north" in decrypted_name
            or "pole" in decrypted_name
            or "object" in decrypted_name
        ):
            print(decrypted_name, sector_id)
